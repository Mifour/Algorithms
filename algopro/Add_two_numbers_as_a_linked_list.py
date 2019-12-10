"""
add two linked list element wyse 

 243 =>  3->4->2
+165 => +5->6->1
=418 =>  8->1->4
"""


class Node(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  def append(self, x):
  	y = self
  	while y.next:
  		y= y.next
  	y.next = Node(x)


def add(a, b):
	reminder = 0
	res = Node()
	while a is not None and b is not None:
		elem = (a or 0) + (b or 0) + reminder
		if elem > 9:
			reminder = 1
			elem -= 10
		else:
			reminder = 0
		res.append(elem)
		a = a.next
		b = b.next
	return res