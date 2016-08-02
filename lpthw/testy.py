"""print "Input a word"
input = raw_input("> ")
print input
print input.lower()
print input.split(" ")
print list(input)


print list(input)[0].lower()
"""
def ask_perm():
  while 1 == 1:
    print "\n\nEnter yes or No"
    a = list(raw_input("> "))[0].lower()
    if a == "y":
      print "YEESS!!!!"
      return (a)
    elif a == "n":
      print "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoooooooooo!!"
      print a
      return (a)
    print "Try again\n\n"

ans1 = ask_perm()
ans2 = ask_perm()
print "%s and %s" % (ans1, ans2)
