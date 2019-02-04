class Animal(object):
	pass
class Dog(Animal):
	def __init__(self,name):
		self.name = name
class Person(object):
	def __init__(self,name):
		self.name = name
		self.pet = None
class Employee(Person):
	def __init__(self,name,salary):
		super(Employee,self).__init__(name)
		self.salary = salary
rover = Dog("Rover")
mary = Person("Mary")
frank = Employee("frank",1000)
frank.pet = rover
print(rover)
print(mary)