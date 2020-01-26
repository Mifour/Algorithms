def first_repeting_char(string):
	"""
		O(n) time and space
	"""
	s = set()
	for c in string:
		if c in s:
			return c
		else:
			s.add(c)
	return None

print(first_repeting_char('azerrty'))
print(first_repeting_char('azerty'))
