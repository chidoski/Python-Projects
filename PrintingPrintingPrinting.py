days = "Mon Tue Wed Thurs Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
print '''There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
'''

print 'Didn\'t you see %r, that\'s %r ' % ("Michael\'s tops", "crazy")
print 'Didn\'t you see %s, that\'s %s ' % ("Michael\'s tops", "crazy\n")

age = raw_input("How old are you?")
print 'So your age is %r' %age
