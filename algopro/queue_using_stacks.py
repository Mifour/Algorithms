class Queue(object):
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def put(self, val):
		self.s1.append(val)

	def pop(self):
		while(self.s1):
			self.s2.append(self.s1.pop())

		self.s2.pop()

		while(self.s2):
			self.s1.append(self.s2.pop())
	
