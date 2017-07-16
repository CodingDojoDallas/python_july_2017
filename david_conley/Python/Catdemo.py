class Cat(object):
	#initialize method
	def __init__(self, name, age, weight, claws=True): # initialize
		self.name = name
		self.age = age
		self.weight = weight
		self.claws = claws

	def emote(self):
		print "meow"	

	def __str__(self):
		return "Name: {} Age: {} "	.format(
#string interpolation
			self.name,
			self.age,
			self.weight,
			
		)	

cat = Cat("Killa", 29, 1)	

print cat #<cat obect number in terminal

print cat.emote #<function at number in terminal....function

""" inheritance:
class Animal(obect):

class Cat(Animal):
so the obect is Animal and cat is inhereting the attributes and arguments from animal
whatever the object class is the inheritor inherits those attributes.
super refers to an obect base class     super(Cat, self).emote()
method chaining: 	
#function is outside of class, and method is gefined insidde a class
#variable is outside a class, and attribute is defined inside a class