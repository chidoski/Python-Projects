def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "That's not enough for the party!"
	print "Get a blanket!\n"

print "We can give the function numbers directly!"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can also do math inside the function"
cheese_and_crackers(5 + 7, 4 + 5)

print "And we can combine the two, variables and math"
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 43)
