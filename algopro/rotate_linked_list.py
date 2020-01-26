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


class Queue:
	def __init__(self, values=[]):
		if isinstance(values, list):
			self.values = values
		else:
			self.values = [values]
	def add(self,value):
		self.values.append(value)
	def pop(self):
		to_pop = self.values[0] if self.values else None
		self.values = self.values[1:] if len(self.values) > 1 else []
		return to_pop
	def length(self):
		return len(self.values)

def rotate1_linked_list(linked_list):
	actual = linked_list
	while actual.next_ll:
		prev = actual
		actual = actual.next_ll
	actual.next_ll = linked_list
	prev.next_ll = None
	return actual

def dumb_rotate_linked_list(k, linked_list):
	"""
	O(kn) time
	O(1) space, no additionnal space
	"""
	for i in range(k):
		linked_list = rotate1_linked_list(linked_list)
	return linked_list

def rotate_linked_list(k, linked_list):
	"""
	O(n) time
	O(k) space
	"""
	k = k % linked_list.length() # modulo
	queue = Queue()
	actual = linked_list
	tail = None 
	#import pdb; pdb.set_trace()
	while actual:
		if queue.length() < k:
			queue.add(actual)
		else:
			tail = queue.pop()
			queue.add(actual)
		if actual.next_ll:
			actual= actual.next_ll
		else:
			break
	if k!=0:
		actual.next_ll = linked_list
	if tail:
		tail.next_ll = None
	return queue.pop()

linked_list = Linked_list(0,Linked_list(1,Linked_list(2,Linked_list(3))))
print(dumb_rotate_linked_list(6, linked_list))
linked_list = Linked_list(0,Linked_list(1,Linked_list(2,Linked_list(3))))
print(rotate_linked_list(6, linked_list))

linked_list = Linked_list(0,Linked_list(1,Linked_list(2,Linked_list(3))))
print(dumb_rotate_linked_list(3, linked_list))
linked_list = Linked_list(0,Linked_list(1,Linked_list(2,Linked_list(3))))
print(rotate_linked_list(3, linked_list))

n= 80
linked_list = eval('Linked_list(0,'*n + 'Linked_list(1)' + ')'*n)
print(dumb_rotate_linked_list(3, linked_list))
linked_list = eval('Linked_list(0,'*n + 'Linked_list(1)' + ')'*n)
print(rotate_linked_list(3, linked_list))