<?php
/**
* All directives are explained in documentation
* at <https://docs.phpmyadmin.net/en/latest/config.html>.
*/
 
$i = 0;
$cfg = array();
 
$cookieSecret = getenv('PMA_BLOWFISH_SECRET');
if ($cookieSecret === false || strlen($cookieSecret) !== 32) {
    http_response_code(503);
    exit('phpMyAdmin secret is not configured.');
}
$cfg['blowfish_secret'] = $cookieSecret;
$cfg['NavigationTreeEnableGrouping'] = false;
$cfg['MaxNavigationItems'] = '200';
$cfg['FirstLevelNavigationItems'] = '200';
$cfg['ShowDatabasesNavigationAsTree'] = false;
$cfg['NumRecentTables'] = 0;
 
$i++;
$cfg['Servers'][$i]['auth_type'] = 'cookie';
$cfg['Servers'][$i]['host'] = getenv('OHSAILOR_DB_HOST') ?: 'localhost';
