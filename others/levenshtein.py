import numpy as np

def levenshtein(first, second):
	"""
		O(nm) time & space for word of n and m characters
	"""
	n = len(first)
	m = len(second)

	matrix = np.array([np.arange(m)+i+1 for i in range(n)])
	for i in range(1, n):
		for j in range(1, m):
			matrix[i,j] = min(
					matrix[i-1, j] +1,
					matrix[i, j-1] +1,
					matrix[i-1, j-1] + int(first[i-1] != second[j-1])
				)
	return matrix[n-1,m-1]

print(levenshtein('audi', 'lada'))
# expect 3 
print(levenshtein('totoro', 'ototoro'))
# expect 1