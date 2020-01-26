class Linked_list:
	def __init__(self, val, next_ll=None):
		self.val=val
		self.next_ll = next_ll
	def __str__(self):
		if self.next_ll:
			return str(self.val) + str(self.next_ll)
		else:
			return str(self.val)
	def length(self):
		if self.next_ll:
			return self.next_ll.length()+1
		else:
			return 1

def unicity(linked_list):
	"""
	given a sorted linked list, remove all duplicate elements.
	O(n) time
	O(1) space
	"""
	prev = linked_list
	actual = linked_list.next_ll

	while actual:
		if actual.val == prev.val:
			if actual.next_ll:
				prev.next_ll = actual.next_ll
			else:
				prev.next_ll=None
		prev = actual
		if actual.next_ll:
			actual = actual.next_ll
		else:
			actual = None

	return linked_list

def unicity_unsorted(linked_list):
	"""
	given a linked list, remove all duplicate elements.
	O(n) time
	O(n) space
	"""
	seen = set()
	seen.add(linked_list.val)
	prev = linked_list
	actual = linked_list.next_ll
	while actual:
		if actual.val in seen:
			if actual.next_ll:
				prev.next_ll = actual.next_ll
			else:
				prev.next_ll=None
		else:
			seen.add(actual.val)
			prev = actual
		if actual.next_ll:
			actual = actual.next_ll
		else:
			actual = None

	return linked_list

linked_list = Linked_list(0,Linked_list(0,Linked_list(1,Linked_list(2,Linked_list(3,Linked_list(3))))))
print(unicity(linked_list))
linked_list = Linked_list(0,Linked_list(1,Linked_list(9,Linked_list(0,Linked_list(9,Linked_list(3,Linked_list(3,Linked_list(9,Linked_list(2)))))))))
print(unicity_unsorted(linked_list))