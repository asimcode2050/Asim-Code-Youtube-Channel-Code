<?php
/*
How to Connect MySQL Database with PHP. 
YouTube Channel : Asim Code
https://youtu.be/PyTVawfgISg
*/
try {
  $data_source = "mysql:host=localhost;dbname=demo";
  $db = new PDO($data_source, "tom", "tom123");
  print("Connected\n");
} catch (PDOException $ex) {
  die("Cannot connect to server\n");
}
$data_source = NULL;
print("Disconnected\n");
