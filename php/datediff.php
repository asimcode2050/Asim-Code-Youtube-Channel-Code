<?php
/*
Computing the difference between two dates in PHP
https://youtu.be/a9-hIpeDVnw
YouTube Channel : Asim Code
*/
$first_date = new dateTime('2001-05-14');
$second_date = new DateTime('2022-12-09');
$interval = $second_date->diff($first_date);
print $interval->format('%y years %d days');
?>
