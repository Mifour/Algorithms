def direct_path(string):
	"""
	Given a Linux Path "/users/john/documents/../desktop/./../"
	return the direct equivalent path "/users/john/"
	O(n) time
	O(n) space
	"""

	pile = []
	for directory in string.split('/'):
		if directory:
			if directory == '.':
				pass
			else:
				if directory == '..':
					pile.pop()
				else:
					pile.append(directory)
	return '/' + '/'.join(pile) + '/'