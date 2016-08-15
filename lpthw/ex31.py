print "You enter a dark room with two doors.  Would you like to go through door 1 or 2?"
door = raw_input('> ')

if door == "1":
  print "There is a giant bear eating some cheesecake.  What do you do?"
  print "1.  Take Cheese Cake"
  print "2.  Scream at bear"

  bear = raw_input('> ')
  
  if bear == "1":
    print "The bear eats your face off... Good job!"
  elif bear == "2":
    print "The bear eats your legs off... Good job!"
  else:
    print "Well doing %s is probably better... The bear runs away" % bear

elif door == "2":
  print "You stare into an endless abyss..."
  print "Blueberries"
  print "Yellow Jackets"
  print "Windbreakers understand what umbrellas feel like"
  insanity = raw_input('> ')
  if insanity == "1":
    print "your brain melts into Jello... but your body survives.... Good Job"
  elif insanity == "2":
    print "Your eyes turn into liquid and then explode some how... Good Job!"
  else:
    print "You back slowly away, and trip on your knife. Killing yourself... Good Job!"

else:
  print "play nice now"
