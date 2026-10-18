<?php
// Credentials are configured by the web server, never committed to this tree.
$dbHost = getenv('OHSAILOR_DB_HOST') ?: 'localhost';
$dbUser = getenv('OHSAILOR_DB_USER');
$dbPassword = getenv('OHSAILOR_DB_PASSWORD');
$dbName = getenv('OHSAILOR_DB_NAME');

if ($dbUser === false || $dbUser === '' ||
    $dbPassword === false || $dbPassword === '' ||
    $dbName === false || $dbName === '') {
    http_response_code(503);
    exit('Database is not configured.');
}

mysqli_report(MYSQLI_REPORT_OFF);
$connect = @mysqli_connect($dbHost, $dbUser, $dbPassword, $dbName);
if (!$connect) {
    http_response_code(503);
    exit('Database connection unavailable.');
}
