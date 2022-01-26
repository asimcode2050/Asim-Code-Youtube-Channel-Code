<?php
$arr[0] = "Hello";
$arr[1] = "World";
$var["Monday"] = 1;
$var["Tuesday"] = 2;
foreach($var as $key=>$value){
    echo "$var[$key]=$value\n";
    echo "Key: $key\n";
    echo "Value: $value\n";
}
?>
