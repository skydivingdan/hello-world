from sys import exit

def gold_room():
  print "This room is full of gold how much do you take?"

  choice = raw_input("> ")
  if "0" in choice or "1" in choice:
    how_much = int(choice)
  else:
    dead("Man, learn to type a number")

  if how_much < 50:
    print "Nice, you're not that greedy.  You Win!"
    exit(0)
  else: 
    dead("You greedy bastard")


def bear_room():
  print """
  There s a bear here
  The bear has a bunch of honey
  The fat bear is in front of another door
  How are you goin to move the bear? """

  bear_moved = False
  
  while True:
    choice = raw_input("> ")
    if choice == "take honey":
      dead("The bear looks at you then slaps your face off.")
    elif choice == "taunt bear" and not bear_moved:
      print "The bear has moved from the door, you can go through it now"
      bear_moved = True 
    elif choice == "taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your leg off.")
    elif choice == "open door" and bear_moved:
      gold_room()
    else:
      print "I got no idea what that means"

def cthulhu_room():
  print """
There you see the great evil Cthulhu.
He, is, whatever stares at you and you go insane.
Do you flee for you life or eat your head?: """

  choice = raw_input(">> ")
  if "flee" in choice:
    start()
  elif "head" in choice:
    dead("Well, that was tastey")
  else:
    cthulhu_room()

def start():
  print """
You're in a dark room
There is a dood to your right and left.
Which do you take? """
  choice = raw_input(">> ")
  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  else:
    dead("You stumble around and starve")
def dead(why):
  print why, "Good job" 
  exit()
start()
