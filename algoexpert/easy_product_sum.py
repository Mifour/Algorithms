"""
a function that sum the elem multiplited by their depth
"""
def function_a(vector, depth):
	elems = []
	for elem in vector:
		if isinstance(elem, int):
			elems.append(elem)
		else:
			tmp = (depth+1)*function_a(elem, depth+1)
			elems.append(tmp)
	return sum(elems)
	
def productSum(array):
	depth = 1
	res = function_a(array, depth=depth)
	return res
