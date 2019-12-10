class stack:
	"""
	O_time(n)
	O_space(n)
	"""

	def __init__(self):
		self.values = []
	
	def put(self,x):
		self.values.append(x)
	
	def pop(self):
		res = self.values[-1]
		self.values = self.values[:-1]
		return res

	def max(self):
		maxi = float('-inf')
		tmp = stack()
		while self.values:
			elem = self.pop()
			if maxi < elem:
				maxi = elem
			tmp.put(elem)

		while tmp.values:
			self.put(tmp.pop())

		return maxi

class super_stack:
	"""
	O_time(1)
	O_space(1)
	"""
	def __init__(self):
		self.values = []
		self.max = float('-inf')

	def put(self,x):
		self.values.append(x)
		self.max =max(self.max, x)
	
	def pop(self):
		res = self.values[-1]
		self.values = self.values[:-1]
		return res
