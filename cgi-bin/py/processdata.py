#!/usr/bin/python

from random import randrange
from datetime import datetime
from pytz import timezone

import cgi
import cgitb

form = cgi.FieldStorage()

count = form.getvalue('magicnumber')
name = form.getvalue('username')
pw = form.getvalue('password')


print "X-Complexity: Easy"
print "Content-type: text/html"
print ""
print "<html>"
print "<head><title>Hello Python Based CGI World!</title></head>"
count = int(count) + 0

while (count > 0):
  count = count - 1
  print "<h1>Hello %s with a password of %s !</h1>" % (name, pw)

print "</body>"
print "</html>"
