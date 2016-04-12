#!/usr/bin/python

import os

print "Content-type: text/html \n\n";
print "<!doctype html>"
print "<html>"
print "<head><title>Hello Python Based CGI World!</title></head>"
print "<h1>Variables Sent By Server</h1>"
print "<table><tr><th>Variable</th><th>Value</th></tr>"

for p in sorted(os.environ.keys()):
  if p.startswith('REQUEST')==False:
    print "<tr><td>%20s</td><td> %s</td></tr>" % (p, os.environ[p])
print "</table>"
print "<h1>Variables Sent By Browser</h1>"
print "<table><tr><th>Variable</th><th>Value</th></tr>"
for p in sorted(os.environ.keys()):
  if p.startswith('REQUEST'):
    print "<tr><td>%20s</td><td> %s</td></tr>" % (p, os.environ[p])

print "</table>"
print "</body>"
print "</html>"
