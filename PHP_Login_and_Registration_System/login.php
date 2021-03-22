<html>
<head>
<title>
Login Page
</title>
</head>
<body>
<?php
  // https://www.youtube.com/watch?v=Lm-jPySiLUI&t=848s&ab_channel=AsimCode
session_start();
require("logininfo.php");
if(is_logged_in()){
    header("Location: index.php");
    exit(0);
}
//check login
if(isset($_POST["username"]) && isset($_POST["password"])){
    require("db.php");
    $user = $_POST["username"];
    $pass = $_POST["password"];
	password_verify($password, $row['password'])
    $select_query = "SELECT PASSWORD from users WHERE USERNAME='".$conn->real_escape_string($user)."'";
    $result = $conn->query($select_query) or die(mysqli_error($conn));
    $row = $result->fetch_assoc();
   // if($pass == $row["PASSWORD"]){
   if (password_verify($pass, $row['PASSWORD'])) {
        $_SESSION["user"] = $conn->real_escape_string($user);
        if(isset($_POST["remember"])){
            setcookie("user",$conn->real_escape_string($user), time()+ 60*60*24,"/");
        }
        header("Location: index.php");
    }
    else{
        echo "Invalid username or password<br/>";
    }
}
?>
<form action="login.php" method="post">
Username: <input type="text" name="username" /><br />
	Password: <input type="password" name="password" /><br />
	Remember me <input type="checkbox" name="remember" /><br />
	<input type="submit" />
</form>
<br />
<br />
<a href="index.php">Home</a><br />
<a href="register.php">Click here to register</a>

</body>
</html>
