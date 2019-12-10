def merge_intervals(array):
	"""
	return overlapping intervals
	ex: [[1,6], [2,6], [8,10]] -> [[1,6],[8,10]]

	O(nlog(n)) time
	O(n) space
	"""
	array = sorted(array, key = lambda elem: elem[0])
	res = []

	for elem in array:
		if not res or elem[0] > res[-1][1]:
			res.append(elem)
		else:
			res[-1][1] = max(elem[1], res[-1][1])
	return res 