#!/usr/bin/ruby -w
require 'cgi';
require 'bigdecimal';
cgi = CGI.new;

print "X-Complexity: Easy\n";
print "Content-type: text/html \n\n";
print "<!doctype html>";
print  "<html><head><title>Hello Ruby based world </title></head>" ;
h = cgi.params;
m1 = Integer(h['magicnumber'][0]);


while m1 > 0 do
 print "<h1>Hello " +  h['username'][0] + "with a password of " + h['password'][0] + "!</h1>";
 m1 = m1 - 1;
end

print "</body></html>";
