#!/usr/bin/python

from sys import argv 

script, file = argv
text = open(file)

print "I'm now going to open a file for you"
print file
print "\n\n"

print text.read()
