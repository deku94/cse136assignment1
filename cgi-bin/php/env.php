<?php
$arr = ksort($_SERVER);
$req = array();
header("Content-type: text/html");
print "<!doctype html>";
print "<html><head><title>Environment Var PHP</title></head><body>";
print "<h1>Variables Sent By Server</h1>";
print "<table><tr><th>Variable</th><th>Value</th></tr>";
foreach($_SERVER as $key=>$val)
{
 if(strpos($key,"REQUEST_")===false)
 {
   print "<tr><td>".$key."</td><td>".$val."</td></tr>";
 }
 else
 {
   $req[$key] = $val;
 }
}
print "</table>";
print "<h1>Variables Sent By Browser</h1>";
print "<table><tr><th>Variable</th><th>Value</th></tr>";
foreach($req as $key=>$val)
{
   print "<tr><td>".$key."</td><td>".$val."</td></tr>";
}
print "</table></body></html>";
?>
