#Tells the program that we want to include an argument passed at time of the command being run
from sys import argv 

#this assigns the variables.  script is it's own name, filename is the first parameter passed to the program. 
script, filename = argv 
#txt will be given the value of the contents of file
txt = open(filename)

#Prints the name of the file
print "Here's your file %r:" % filename
#prints the contents of the file useing the .read() 
print txt.read()

#Prints a message asking for the file name a second time.  Or a different file.  I mean its not like we verify its the same. 
print "Type the filename again:"
#reads the input
file_again = raw_input (">")

#assigns the variable the contents of the file
txt_again = open(file_again)

#prints the contents of the variable. 
print txt_again.read()
