<?php
require_once 'vendor/autoload.php';
$faker = Faker\Factory::create();
echo $faker->name;
echo "\n";
echo $faker->address;
?>
