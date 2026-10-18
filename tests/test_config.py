import os
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
PHP = os.environ.get("PHP_BINARY") or shutil.which("php")


@unittest.skipUnless(PHP, "PHP CLI is required")
class ConfigurationTests(unittest.TestCase):
    def run_php(self, code, **values):
        env = {k: v for k, v in os.environ.items()
               if not k.startswith(("OHSAILOR_", "PMA_", "STUB_"))}
        env.update(values)
        result = subprocess.run([PHP, "-n", "-r", code], cwd=ROOT,
                                env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def database(self, **values):
        # -n leaves mysqli unloaded; these stand-ins never open a network connection.
        code = """
define('MYSQLI_REPORT_OFF', 0);
function mysqli_report($flags) {}
function mysqli_connect($host, $user, $password, $name) {
    if ($host !== 'localhost' || $user !== 'synthetic-user' ||
        $password !== 'synthetic-password' || $name !== 'synthetic-db') {
        throw new RuntimeException('Unexpected configuration');
    }
    return getenv('STUB_FAIL') ? false : (object) array();
}
register_shutdown_function(function () { echo '|status=' . http_response_code(); });
require 'web/database.php';
echo 'connected';
"""
        return self.run_php(code, **values)

    def test_missing_or_empty_credentials_fail_closed(self):
        good = dict(OHSAILOR_DB_USER="synthetic-user",
                    OHSAILOR_DB_PASSWORD="synthetic-password", OHSAILOR_DB_NAME="synthetic-db")
        for key in good:
            for value in (None, ""):
                values = dict(good)
                if value is None:
                    del values[key]
                else:
                    values[key] = value
                output = self.database(**values)
                self.assertEqual(output, "Database is not configured.|status=503")

    def test_credentials_are_forwarded_and_connection_failure_is_generic(self):
        values = dict(OHSAILOR_DB_USER="synthetic-user",
                      OHSAILOR_DB_PASSWORD="synthetic-password", OHSAILOR_DB_NAME="synthetic-db")
        self.assertTrue(self.database(**values).startswith("connected"))
        output = self.database(STUB_FAIL="1", **values)
        self.assertEqual(output, "Database connection unavailable.|status=503")
        self.assertNotIn(values["OHSAILOR_DB_PASSWORD"], output)

    def test_phpmyadmin_requires_a_separate_32_character_secret(self):
        code = """
register_shutdown_function(function () { echo '|status=' . http_response_code(); });
require 'web/mydbadmin/config.inc.php';
if ($cfg['blowfish_secret'] !== getenv('PMA_BLOWFISH_SECRET')) {
    throw new RuntimeException('Secret was not injected');
}
echo 'configured';
"""
        for value in (None, "", "a" * 31, "a" * 33):
            env = {} if value is None else {"PMA_BLOWFISH_SECRET": value}
            self.assertEqual(self.run_php(code, **env), "phpMyAdmin secret is not configured.|status=503")
        self.assertTrue(self.run_php(code, PMA_BLOWFISH_SECRET="a" * 32).startswith("configured"))

    def test_changed_php_files_parse(self):
        for path in ("web/database.php", "web/mydbadmin/config.inc.php",
                     "web/ohsailor/index.php", "web/ohsailor/view/index.php",
                     "web/ohsailor/write/index.php"):
            result = subprocess.run([PHP, "-n", "-l", str(ROOT / path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
