"""
	This is just a fun play with classes and recursion

	'We are what we eat'
	Then only cannibals that eat humans are human? 
	Only if the human himself ate another cannibal
	that ate another cannibal that ate another...

	This create such class and try to get a Human object 
	that is human according to this criteria.
"""

def insertion(args):
	print('this function is an insertion')

class Human:
	def __init__(self,name=None, food=None):
		self.name = name
		self.food = food
		
	def is_human(self, food=None):
		if self == food:
			return True
		if isinstance(self.food, Human):
			return self.food.is_human(food=food or self.food)
		return False

alice = Human(name='alice')
bob = Human(name='bob')
charlie = Human(name='charlie')
alice.food = bob
bob.food = charlie
charlie.food = bob
print(alice.is_human()) # True
