class Hero:
	'''
	A hero who is allergic to apples
	'''
	def __init__(self,name):
		self.name = name
		self.health = 100

	def eat(self, food):
		if(food == 'apple'):
			self.health -= 100
		elif(food == 'ham'):
			self.health += 20

Kalu = Hero('Kalu')
print Kalu.name
print Kalu.health

Kalu.eat('apple')
print Kalu.health
