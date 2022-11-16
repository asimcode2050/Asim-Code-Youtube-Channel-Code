<?php
 /*
  How to Add a Value to the front and end of an a array in PHP
  https://youtu.be/-E9zHBZYpvw
  https://www.youtube.com/@AsimCode
 */
 $programming_languages = array("PHP");
 array_unshift($programming_languages,"Python","C++");
 print_r($programming_languages);
 array_push($programming_languages,"JAVA");
 print_r($programming_languages);
?>
