class Linked_list:
	def __init__(self, val, next=None):
		self.val=val
		self.next=next
	def __str__(self):
		if self.next:
			return str(self.val) +'->'+ str(self.next)
		else:
			return str(self.val)

def swap_every_two_nodes(linked_list):
	"""
		O(n) time
		O(1) no addictionnal space

	"""
	actual = linked_list
	next = actual.next
	index = 0

	while next:
		if not index % 2:
			tmp = next.val
			next.val = actual.val
			actual.val = tmp
		actual = next
		next = next.next
		index+=1
	return linked_list

linked_list = Linked_list(0,Linked_list(1,Linked_list(9,Linked_list(0,Linked_list(7,Linked_list(3,Linked_list(3,Linked_list(9,Linked_list(2)))))))))
print(linked_list)
print(swap_every_two_nodes(linked_list))
