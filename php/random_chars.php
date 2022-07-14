<?php
/*
PHP How to generate a string of random characters
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
https://youtu.be/51qCBY17LKo
*/
$char_string = '0123456789abcdefghijklmnopqrstuvwxyz';
$length = 16;
$string ='';
while(strlen($string) < $length){
    $string .= $char_string[random_int(0,strlen($char_string))];
}
print($string);
?>
