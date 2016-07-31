#!/usr/bin/python
from sys import argv
from os.path import exists
script, from_file, to_file = argv

if exists(to_file) == True:
  print "WARNING! %s already exists. Would you like to overwrite?" % to_file
  consent = raw_input("Y or N:(Y)  ")
  if consent == "N": 
    quit()
print "Copying from %s to %s" % (from_file, to_file) 
indata = open(from_file).read() 
open(to_file, 'w').write(indata)
print "Copied %d bytes to %s \n\n\n\t So long, and thanks for all the fish!" % (len(indata), to_file)
