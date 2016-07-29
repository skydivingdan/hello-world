x = "There are %d types of people." % 10

binary = "binary"
do_not = "don't"
y = "Those who know %r and those who %s." % (binary, do_not) # the %r puts raw data out which encloses the string in ' '  Could be useful, %s is a proper string and therefore doesn't do that. 

print x
print y 

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False 
joke_eval = "Isn't that joke so funny?! %r" #I say it is.  Though I like the 11 variant of it better. 


print joke_eval % hilarious

w = "This is the left side of..."

e = "a string with a right side"

print w+e # string math.  This was made popular in the book stories from wayside school.  They would use their reading books to practice arithmetic. 


