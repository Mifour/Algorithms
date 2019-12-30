"""
	for an array of n integers >1, return an array where result[i] = product of array elems except i
	O(n) time and space
"""


def product_of_array_except_itself(array):
	prod = 1
	for elem in array:
		prod *= elem

	res = []
	for elem in array:
		res.append(prod/elem)

	return res
