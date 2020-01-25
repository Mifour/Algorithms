class Rectangle:
	"""docstring for rectangle"""
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
	def area(self):
		return ((self.p2[0]-self.p1[0])*(self.p2[1]-self.p1[1]))
	def is_valid(self):
		return self.p1[0] < self.p2[0] and self.p1[1] < self.p2[1]

def intersection_area(rect1, rect2):
	if not rect1.is_valid() or not rect2.is_valid():
		return False

	p1 = (0,0)
	P2 = (0,0)

	p1[0] = max(rect1.p1[0], rect2.p1[0])
	p1[1] = max(rect1.p1[1], rect2.p1[1])
	
	p2[0] = min(rect1.p2[0], rect2.p2[0])
	p2[1] = min(rect1.p2[1], rect2.p2[1])
	
	intersection = Rectangle(p1=p1, p2=p2)

	if not intersection.is_valid():
		return 0
	return intersection.area()

print(
	intersection_area(
		Rectangle(p1=(0,0),p2=(2,2)),
		Rectangle(p1=(1,1),p2=(3,3))
		)
	)
		
print(
	intersection_area(
		Rectangle(p1=(1,1),p2=(3,3)),
		Rectangle(p1=(1,1),p2=(3,4))
		)
	)
