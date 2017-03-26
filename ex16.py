from sys import argv

script, filename, = argv

print "We are going to erase %r." % filename
print "If you dont want to press CRTL - C(^C)."
print "Else press RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I need three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line1, line2, line3)
print "Now we are done"
target.close()

print "Actually we arent completely done yet! "
print "Here is your new file: ", filename
target =  open(filename, 'r')
print target.read()
target.close()
