#!/usr/bin/ruby -w

colors = Array["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"];

time = Time.new;


print "Content-type: text/html \n\n";
print "<!doctype html>";
print "<html>\n<head>\n<title>Hello Ruby World!!!!</title>\n</head>\n";
print "<body style=background-color:"+ colors.sample  + ">\n";
print "<h1>Hello World from Ruby @ " + time.strftime("%Y-%M-%D | %H:%M:%S")+ "</h1>\n";
print "</body>\n</html>";
