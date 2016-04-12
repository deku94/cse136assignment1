<?php
 $colors = array("aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon","navy", "olive", "purple", "red", "silver","teal", "white", "yellow");
date_default_timezone_set('America/Los_Angeles');
 
 header( "Content-type: text/html") ;
 print  "<html><head><title>Hello C Based CGI World</title></head>" ;
 print "<body style='background-color: ".$colors[array_rand($colors)]."'><h1>Hello World from PHP @ ".date("Y-m-d | h:i:sa")."</h1>";
 print "</body></html>";
?>
