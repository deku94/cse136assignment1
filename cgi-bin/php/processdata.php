<?php
 
 header( "Content-type: text/html") ;
 print "<!doctype html>";
 print  "<html><head><title>Hello C Based CGI World</title></head>" ;
 for($x = 0; $x < intval($_REQUEST["magicnumber"]); $x++)
 {
 print "<h1>Hello ".$_REQUEST["username"]." with a password of ".$_REQUEST["userpassword"]. "!</h1>";
 }
 print "</body></html>";
?>
