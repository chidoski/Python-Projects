from sys import argv
import operator

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

print rewind(current_file)

print "Let's print all three lines:"


print "find another way to accumulate"
new_current_line = 1
print_a_line(new_current_line, current_file)
new_current_line += 1
print_a_line(new_current_line, current_file)
new_current_line += 1
print_a_line(new_current_line, current_file)
current_file.close()

#imported operator module to accumulate
current_file_1 = open(input_file)
current_line = 1
print_a_line(current_line, current_file_1)

current_line = operator.iadd(current_line, 1)
print_a_line(current_line, current_file_1)

current_line = operator.iadd(current_line, 1)
print_a_line(current_line, current_file_1)

'''
the orginal accumlator form
current_line = 1
#current_line = current_line + 1
print_a_line(current_line, current_file)
'''
