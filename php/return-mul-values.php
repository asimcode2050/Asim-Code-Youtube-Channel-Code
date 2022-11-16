<?php
  /*
  How to return multiple values From a function in PHP
  https://youtu.be/J6ZHBn9UoAc
  https://www.youtube.com/@AsimCode
  */
    function getUserProfile()
    {
        $user[] = "Mike Tyson";
        $user[] = "mike@somemail.com";
        $user[] = "English";
        return $user;
    }
    list($name, $email, $language) = getUserProfile();
    echo "Name: $name, Email: $email, Language: $language";
?>
