<?php
// https://www.youtube.com/watch?v=Lm-jPySiLUI&t=848s&ab_channel=AsimCode
session_start();
function is_logged_in(){
    if(!isset($_SESSION["user"]) && isset($_COOKIE["user"])){
        $_SESSION["user"] = $_COOKIE["user"];
    }
    return isset($_SESSION["user"]);
}
function logout(){
    unset($_SESSION["user"]);
    setcookie("user","",0,"/");
    header("Location: index.php");
}
?>
