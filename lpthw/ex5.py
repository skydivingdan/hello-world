name = 'Inigo Montoya'
age = 35 
height = 71 # inches
weight = 195 # Pounds for pound signs... ha
eyes = 'Blue'
teeth = 'Mother of Pearl'
hair = "Error: Hair not found"

print "Let's talks about %s." % name # %s is for a string
print "He's %d inches tall." % height # %d is for an interger 
print "     which is %r centimeters tall" % (height * 2.54) # %r is for a lot of stuff is a string representation of what ever it is
print "He's %g pounds heavy." % weight # %g is for floating point format... uses decimals if needed... or not. 
print "He knows he's fat" # He really does
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s due to excessive coffee." % teeth

#this line is tricky
print "If I add %d, %d, and %d I get %f"% (age, height, weight, age + height + weight)
