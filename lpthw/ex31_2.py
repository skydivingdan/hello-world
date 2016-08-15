def choice(n):
  while 1 == 1:
    userin = raw_input('> ')
    try:
      if 1 <= int(userin) <= n:
        return(int(userin))
      else:
        print "%d isn't a valid option" % int(userin)
    except ValueError:
      print "Please pick a NUMBER between 1 and %d" % n

print "Pick a nuber between 1 and 2"
num = choice(2)
print num

print "Pick a number between 1 and 5"
num2 =choice(5)
print num2
