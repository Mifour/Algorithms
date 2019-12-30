class Node:
	def __init__(self, val, next=None):
		self.value = val
		self.next = next

def merge_linked_lists(l1, l2):
"""
O(max(len(a), len(b))) time and space
"""
	if l1.value < l2.value:
		res= Node(l1.value)
		l1 = l1.next
	else:
		res= Node(l2.value)
		l2 = l2.next

	head = res

	while l1.value or l2.value:
		if l1.value and l2.value:
			if l1.value<l2.value:
				res.next= Node(l1.value)
				res= res.next
				l1 = l1.next
			else:
				res.next= Node(l2.value)
				res = res.next
				l2 = l2.next
		elif l1.value:
			res.next= Node(l1.value)
			res = res.next
			l1 = l1.next
		elif l2.value:
			res.next= Node(l2.value)
			res = res.next
			l2 = l2.next

	return head
