<?php
/*
 * Project     : ex-db-con
 * Script      : index.php
 * Description : Main page
 * Author      : DOMINGUES PEDROSA Samuel
 * Date        : 2023.01.19, V1.0
 */

require('./lib/databse.inc.php');
 
$dbCon = new DatabseController();

$time = filter_input(INPUT_POST, 'time', FILTER_SANITIZE_STRING);
$value = filter_input(INPUT_POST, 'value', FILTER_VALIDATE_FLOAT);

if ($time && $value) {
    $dbCon->insert($time, $value);
}
?>
<!DOCTYPE html>
<html> 
    <head>
        <meta charset="utf-8">
        <title>Title</title>
        <link rel="stylesheet" href="main.css">
    </head>

    <body>
    </body>
</html>