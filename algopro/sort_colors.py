def sort_colors(array):
	"""
		O(n) time
		O(n) space
	"""
	red = []
	white = []
	blue = []

	for elem in array:
		if elem == 0:
			red.append(red)
		if elem == 1:
			white.append(elem)
		if elem == 2:
			blue.append(elem)

	return red+white+blue