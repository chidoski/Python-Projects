#create a dictionary of states
states = {
	'New York': 'NY',
	'South Carolina': 'SC', 
	'North Carolina': 'NC',
	'Florida': 'FL', 
	'California': 'CA'
}

#create a dictionary of cities
cities = {
	'NY': 'Harlem', 
	'SC': 'Orangeburg',
	'NC': 'Charlotte', 
	'FL': 'Orlando',
	'CA': 'Oakland'
}

#add more cities
cities['NY'] = 'Brooklyn'
cities['SC'] = 'Columbia'
cities['FL'] = 'Tampa'

#print out some cities
print '-' * 10
print "The city in NY is %s " % cities['NY']
print "The city in SC is %s " % cities['SC']

#print out some states
print '-' * 10
print "%s is the state in this dictionary" % states['New York']

#do it by using the state then city dicitionary
'''
states['New York'] has a value of 'NY' which turns the equation into cities['NY']
'''
print '-' * 10
print "A value within a value: %s" % cities[states['New York']]

#print out every state
print '-' * 10
for citystate, abbrev in states.items():
	print "%s and it's abbreviation %s " % (citystate,abbrev)

#print out every city
print '-' * 10
for abbrev, city in cities.items():
	print "%s the abbreviation and the city %s" % (abbrev,city)

#print both the city and the state
for state,abbrev in states.items():
	print "%s the state %s the abbrev %s the city" % (state, abbrev, cities[abbrev])

state = states.get('Texas')

if not state:
	print "Sorry state not available"

#get city with default value
city = cities.get('TX', 'Default Valut')
print "The city for the state 'TX' is: %s" % city 
