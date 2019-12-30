
def valid_parenthesis(array):
"""
check the validity of a sequence of parenthesis
O(n) time and space
"""
	def inverse(c):
		if c == '(':
			return ')'
		if c == ')':
			return '('
		if c == '{':
			return '}'
		if c =='}':
			return '{'
		if c == '[':
			return ']'
		if c ==']':
			return '['
		return None

	mem = []

	mem.append(array[0])

	for i in range(1, len(array)):
		if array[i] != inverse(mem[-1]):
			mem.append(array[i])
		else:
			mem.pop()

	if not mem:
		return True
	return False
