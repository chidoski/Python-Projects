name = 'Martin Luther'
age = 27 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
cent = 2.54
kilos = 2.2
centimeters = cent * height
kilograms = weight / kilos
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "This is my height in centimeters %d." %centimeters
print "This is my weigh in kilograms %d." %kilograms
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
