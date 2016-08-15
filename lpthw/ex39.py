# create a mapping of State abbreviations to the actual States. 
# It seems like a DICT could be used to make an arbitary Database... I'll have to look into reading/outputting into a csv...

states = {
  'Oregon' : 'OR',
  'Florida' : 'FL',
  'California' : 'CA',
  'New York': 'NY',
  'Michigan' : 'MI'
}

#Create a basic set of states and some cities in them....
cities = { 
  'CA' : 'San Diego', 
  'MI' : 'Detorit', 
  'FL' : 'Tampa'
}
#Print out some Cities...
print '-' * 15
print "Michigan' abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

cities['NY'] = 'New York'
cities['OR'] = 'Portlandia'

#print some cities out
print "NY State has: ", cities['NY']
print "has the city of ", cities['OR']

print "Michigan has: ", cities[states['Michigan']]
print "Florida has the city of ", cities[states['Florida']]
print states['Oregon']

print "-" * 15
for state, abbrev in states.items():
  print "%s is abbreviated %s" % (state, abbrev)

print "-" * 22
for state, abbrev in states.items():
  print "%s State is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])

print '-' * 17
state = states.get('Texas')
if not state:
  print "Sorry No Texas." 

city = cities.get('TX','Does not exist')
print "The city for the state 'TX' is : %s" % city

  
