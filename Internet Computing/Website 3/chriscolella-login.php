<?php
// Written by Chris Colella 10/30/2022

// Getting variables from the form via the post method
$incomingpassword = $_POST['pswd'];
$incomingusername = $_POST['userName'];

// Printing out the users username and password
echo 'Thank you ';
echo $_POST['userName'];
echo ' your password is ';
echo $_POST['pswd'];
?>
