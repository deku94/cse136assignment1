#!/usr/bin/python

from random import randrange
from datetime import datetime
from pytz import timezone

colors = ["aqua", "black", "blue", "fuchsia",
        "gray", "green", "lime", "maroon",
        "navy", "olive", "purple", "red",
        "silver", "teal", "white", "yellow"]

fmt = "%Y-%m-%d %H:%M:%S"
time = datetime.now(timezone('America/Los_Angeles'))


print "Content-type: text/html \n\n";
print "<!doctype html>"
print ""
print "<html>"
print "<head><title>Hello Python Based CGI World!</title></head>"
print "<body style='background-color: " + colors[randrange(len(colors))] + "'>"
print "<h1>Hello World from Python @ " + time.strftime(fmt) + "</h1>"
print "</body>"
print "</html>"
