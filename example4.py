#the number of cars I own
cars = 100
#how spacious each car is
space_in_a_car = 4.0
#number of drivers that drive for the company
drivers = 30
#number of avg passengers we have each wk
passengers = 90
#how many cars are left over after all drivers take a car
cars_not_driven = cars - drivers
#number of cars being driven by drivers
cars_driven = drivers
#overall space of the total amount of cars
carpool_capacity = cars_driven * space_in_a_car
#avg amount of persons per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
