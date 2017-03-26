the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apriocts']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#the first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

#same as above
for fruit in fruits:
	print "These are the fruit %s" % fruit

#Going through mixed lists
#notice we have to use %r since we dont know what's in this list
for i in change:
	print "I got %r" % i

#lists can also be built, start with an empty one
elements = []

#then use the range funtion to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)

#now we will print them out
for i in elements:
	print "Elements was: %d" % i

my_list = ['one', 'two', 'three', 'four']
my_list_len = len(my_list)
for i in range(0, my_list_len):
	print "Element is: %s" % i
	#in order to print the elements use the list plus the elements
	print (my_list[i])

multi_dim = [1 ,2, 3, 4, 5],[6, 7, 8, 9, 10]
print multi_dim

