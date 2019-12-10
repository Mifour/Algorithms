def word_search(matrix, word):
	"""
	matrix being like:
	[
		[a, l, i, n, e],
		[a, l, i, n, e],
		[a, l, i, n, e],
		[a, l, i, n, e],
	]
	"""

	# search the first letter in the reduced matrix
	reduced_col, reduced_line = matrix.shape() - len(word)

	for i in range(len(reduced_line)):
		for j in range(len(reduced_col)):
			if matrix[i][j] == word[0]:
				if matrix[i][j:j+len(word)-1] == word:
					return True
				if matrix[i: i+len(word)-1][j] == word:
					return True
	return False
