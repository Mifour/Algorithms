import numpy as np

def mini_git(first, second):
	"""
		Mini git that transform a first file into a second by removing and inserting lines
		O(nm) time & space for word of n and m lines
	"""
	first = first.split('\n')
	second = second.split('\n')
	n = len(first)
	m = len(second)
	matrix = np.zeros((n+1,m+1))
	modif = []
	# pseudo levenshtein on each sequence of lines
	for i in range(n):
		for j in range(m):
			if first[i] != second[j]:
				matrix[i+1,j+1] = matrix[i,j]+1
			else:
				matrix[i+1,j+1] = max(matrix[i,j+1], matrix[i+1,j])
	res = []
	i,j = n,m
	print(matrix)
	while i > 0 and j > 0:
		if matrix[i,j] == matrix[i-1,j]:
			i-=1
			res.append('- '+first[i])
		elif matrix[i,j] == matrix[i,j-1]:
			j-=1
			res.append('+ '+second[i])
		else:
			i-=1
			j-=1
			res.append(first[i])
	return res[::-1]

print(mini_git('hello\naudi\nis a german\ncar manufacturer', 'hello\nlada\nis a russian\ncar manufacturer'))
# expect [
# 	'hello',
# 	'- audi',
#	'+ lada',
#	'- is a germain',
# 	'+ is a russian',
# 	'car manufacturer'
# ]