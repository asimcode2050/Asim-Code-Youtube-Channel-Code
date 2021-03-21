<html>
<head>
<title<Registration</title>
</head>
<body>
<?php
session_start();
// https://www.youtube.com/watch?v=Lm-jPySiLUI&t=848s&ab_channel=AsimCode
require("logininfo.php");
//check if user already logged in
if(is_logged_in()){
    header("Location: index.php");
    exit(0);
}
$success = false;
echo isset($_POST["username"]);
if(isset($_POST["username"]) && isset($_POST["password"])){
    require("db.php");
    $user = $conn->real_escape_string($_POST["username"]);
    $sql_query = "SELECT COUNT(*) FROM users WHERE USERNAME='$user'";
    $result = $conn->query($sql_query);
    
    
        $row = $result->fetch_assoc();
        if($row["COUNT(*)"]!=0){
            echo "The user already exists!<br/>";
        }
   
    else{
        
        $pass = $conn->real_escape_string($_POST["password"]);
        $phone = $conn->real_escape_string($_POST["phone"]);
        $insert_query = "INSERT INTO users VALUES ('$user','$pass','$phone')";
       
        if($conn->query($insert_query) === TRUE){
            echo "New record created successfully";
            $success = true;
        }
        else{
            echo "Error: ".$conn->error;
        }


    }
}
if(!$success){
    ?>
    <h1>Registration Form</h1><br/>
    <form action="register.php" method="post">
    Username: <input type="text" name="username" /><br/>
    Password: <input type="password" name="password" /><br/>
    Phone: <input type="text" name="phone" /><br/>
    <input type="submit">
    </form>
    <?php
    }
?>
</br>
<a href="index.php">Home</a><br />
<a href="login.php">Click here to login</a>
</body>
</html>
