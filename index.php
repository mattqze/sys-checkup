<?php
header("refresh: 2.5;");
include "main/header.php";
?>
<?php
function checkup(){
    $output=shell_exec('checkup.py');
    return $output;
    }
?>
<b><pre><?php echo checkup(); ?></pre></b>
