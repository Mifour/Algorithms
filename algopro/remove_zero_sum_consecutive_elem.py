class node:
	def __init__(self, val):
		self.val = val
		self.next = None

def remove_zero_sum_consecutive_elem(linked_list):
	ex = None
	exex= None
	head = linked_list
	ok = False
	checked = False


	while not ok:
		checked = True
		while pnt.next != None:
			if ex:
				if exex:
					if pnt.val + ex.val == 0:
						exex.next = pnt.next
						checked = False
					else:
						exex = ex
						ex = pnt
				if not exex:
					if pnt.val + ex.val == 0:
						head = pnt.next
						checked = False
					else:
						exex = ex
						ex = pnt
		if checked == True:
			ok = True
	return head