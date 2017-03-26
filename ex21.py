def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b

def multiplication(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b

def division(a,b):
	print "DIVIDE %d / %.2f" % (a,b)
	return a / b

def modulus(a,b):
	print "FIND THE MODULOUS OF %d %% %d" % (a,b)
	return a % b

print "Let's do some math"
age = add(20,7)
weight = subtract(170,15)
height = multiplication(35,2)
IQ = division(500,2.5)
Days_Until_YC = modulus(10,3)

print "This is your information:\n"
print "Age:%d , Height:%d, Weight:%d, IQ:%.2f, Days Until YC:%d" % (age,height,weight,IQ,Days_Until_YC)  

print "Here is a puzzle"

what = add(age, subtract(weight, multiplication(height, division(IQ, modulus(Days_Until_YC, 2)))))

print "That becomes: ", what, "Can you do it by hand?" 
