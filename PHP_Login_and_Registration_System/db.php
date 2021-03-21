<?php
# https://www.youtube.com/watch?v=Lm-jPySiLUI&t=848s&ab_channel=AsimCode
$servername = "localhost";
$username = "tom";
$password = "tom123";
$dbname = "school";
$conn = new mysqli($servername,$username,$password,$dbname);
if($conn->connect_error)
    die("Connection failed: ".$conn->connect_error);
//echo "Connected successfully";
$sql = "CREATE TABLE IF NOT EXISTS users (USERNAME VARCHAR(20) NOT NULL, PASSWORD VARCHAR(20) NOT NULL, PHONE VARCHAR(10) NOT NULL, UNIQUE(USERNAME))";
if($conn->query($sql) === TRUE){
   /// echo "Table users created!";
}
/*
else{
    echo" Error in creating table ". $conn->error;
}*/
?>
