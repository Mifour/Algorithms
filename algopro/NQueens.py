import numpy as np

def Nqueens(k):
	"""
	Give a solution for the NQueens problem
	O(n) time
	O(n**2) space, no addictionnal space
	"""
	matrix = np.full((k,k),'.')
	for i in range(k):
		myj = (i*2 % k)+1 if not k %2 and i*2 >= k else i*2 %k
		matrix[i,myj] = 'Q'
	return matrix

print(Nqueens(5))
print(Nqueens(8))
