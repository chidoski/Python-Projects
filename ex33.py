i = 0
numbers = []
#print "How large do you want the array to be?"
#x = raw_input(' > ')
for i in range(6):	
	print "At the top i is %d" % i
	numbers.append(i)

	#i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num

for i in numbers:
	print i
