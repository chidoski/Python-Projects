#sis is a package that says get the argv feature from the package
from sys import argv

script, filename = argv

#the open the filename that is passed
open_file  = open(filename)

#print the name of the file
print "Here is file %r " % filename

#read the file that was printed
print open_file.read()
open_file.close()

#reenter the name of the file
print "Enter the file name again"

#user inputs the name of file and assigns it to file_again
file_again = raw_input (" > ")

#Open file and assign to open_file_again
open_file_again = open(file_again)

#read opened file 
print open_file_again.read()
open_file_again.close()





'''
I prefer using the first example for writing this code because it tells you the name of the file that you are entering. All in all though they are still essentially the same.
'''
