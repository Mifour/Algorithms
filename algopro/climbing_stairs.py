def climbing_stairs(n):
	"""
	n, the number of stairs

	O(2**n) time and space
	"""
	if n < 2:
		return 1
	if n == 2:
		return 2
	return climbing_stairs(n-1) + climbing_stairs(n-2)

def climbing_stairs(n):
	"""
		O(n) time
		O(n) space
	"""
	dico = {0:1, 1:1}

	for i in range(2, n+1):
		dico[i] = dico[i-1] + dico[i-2]

	return dico[n]
