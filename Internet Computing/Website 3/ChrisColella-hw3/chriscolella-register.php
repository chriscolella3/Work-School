<?php
// Written by Chris Colella 10/30/2022

$incomingnewpassword = $_POST['newPswd'];
$incomingnewusername = $_POST['newUserName'];
$duration = $_POST['membership'];

$duration = $duration * 25;

echo 'Welcome ';
echo $_POST['newUserName'];
echo ' to become a new member.';
echo ' Your password is ';
echo $_POST['newPswd'];
echo  nl2br ("\nYour membership length is ");
echo $_POST['membership'];
echo ' months.';
echo  nl2br ("\nThe total charge of your membership is $");
echo $duration;
echo '.';


?>
