class node:
	def __init__(self, val):
		self.val = val
		self.next = None

	def add(self, val):
		while self.next != None:
			self= self.next
		self.next = node(val)


def remove_k_last_elem(linked_list):

	late = Queue.queue()
	tmp= linked_list

	while tmp.next != None:
		if len(late) < k+1:
			late.push(tmp)
		else :
			late.pop()
			late.push(tmp)
		tmp = tmp.next

	late.pop().next = late.pop().next

	return linked_list
