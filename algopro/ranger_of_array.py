def ranger_of_array(array):
	"""
		O(n) time
		O(n) space
 	"""
	res = []
	start = 0
	end = 0
	prev = array[0]

	for i in range(1, len(array)):
		if array[i] == prev+1:
			end = i
		else:
			res.append((array[start], array[end]))
			start = i
			end = i
		prev = array[i]

	return [str(start)+"->"str(end) if start != end else str(end) for elem in res]
