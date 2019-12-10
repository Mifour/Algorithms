def intersection_of_arrays_EZ(l1,l2):
	return set(l1).intersection(set(l2))

def intersection_of_arrays(l1,l2):
	"""
		O(n) time
		O(n) space
	"""
	set1 = set()
	for elem in l1:
		set1.add(elem)
	set2 = set()
	for elem in l2:
		set1.add(elem)

	res = []
	for elem in set1:
		if elem in set2:
			res.append(elem)
	return res