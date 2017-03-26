animals = "dogs cats horses bats racoons foxs"

print "Put ten items in the list"
new_animals = animals.split(' ')
fish = ["salmon", "bass", "tilapia", "shark", "dolphin", "shamoo"]

while len(new_animals) != 10:
	new_fish = fish.pop()
	print "Adding: ", new_fish
	new_animals.append(new_fish)
	print "There are %d animals in this list. " % len(new_animals)

print new_animals

	
