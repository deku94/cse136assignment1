#!/usr/bin/ruby -w

print "Content-type: text/html \n\n";
print "<!doctype html>";
print "<html><head><title>Environment Var PHP</title></head><body>";
print "<h1>Variables Sent By Server</h1>";
print "<table><tr><th>Variable</th><th>Value</th></tr>";


ENV.sort.each do |key, val|
 if(key.index("REQUEST_") ===nil) 
   print "<tr><td>" + key  + "</td><td>" + val  + "</td></tr>";
 end
end


print "</table>";
print "<h1>Variables Sent By Browser</h1>";
print "<table><tr><th>Variable</th><th>Value</th></tr>";

ENV.sort.each do |key, val|
 if(key.index("REQUEST_") != nil) 
   print "<tr><td>" + key  + "</td><td>" + val  + "</td></tr>";
 end
end
print "</table>"
print "</body>\n</html>";
