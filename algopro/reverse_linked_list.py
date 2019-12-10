class Node:
	def __init__(self, x):
		self.value = x
		self.next = None



def reverse(linked_list):
	p1, p2 = None, linked_list
	while p2 is not None:
		p3 = p2.next
		p2.next = p1
		p1 = p2
		p2 = p3
