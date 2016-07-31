#!/usr/bin/python
def print_two(*args):
  arg1, arg2 = args
  print "arg1: %s, arg2: %s" % (arg1,arg2)

def print_2_again(arg1, arg2):
  print "arg1: %s, arg2: %s" % (arg1, arg2)

def print_one(arg1):
  print "arg1: %s" % arg1

def print_none():
  print "I got nothin'."

Zed = raw_input("Enter a name: ")
print_two(Zed,"Shaw")
print_2_again("Shaw", Zed)
print_one("First!")
print_none()
