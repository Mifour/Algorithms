class LinkedList:
	def __init__'self, val:
		self.val = val
		self.next = None

def intersection_liked_lists(a,b):
"""
return the intersection of 2 linked_lists
ex: 1->2->3->4->7
    1->2->3->5
    return 1->2->3
O(min(len(a),len(b))) time and space
"""	s1 = []
	s2 = []

	while a.val:
		s1.append(a.val)
		a= a.next
	while b.val:
		s1.append(b.val)
		b= b.next
	
	resA = s1.pop()
	resB = s2.pop()
	while resA == resB:
		res = resA
		resA = s1.pop()
		resB = s2.pop()

	return res
