"""
	A language tool with a dictionnary as a tree.
	It can check for the spell of a word.
	O(n) time for a n characters long word
	O(log(m)) space for a m words dictionnary
"""

class Tree:
	def __init__(self, letter='', is_word=False, children=None):
		self.letter = letter
		self.is_word = is_word
		self.children = children

def spell_check(word, tree):
	"""
	return True if the word is correctly spelled else False
	"""
	if not word or not tree:
		return False
	if tree.letter == '':
		res = False
		for child in tree.children:
			res = spell_check(word, child) or res
			if res:
				break
		return res
	else:
		if word[0] != tree.letter:
			return False
		else:
			if len(word) < 2 :
				return tree.is_word
			res = False
			for child in tree.children:
				res = spell_check(word[1:], child) or res
				if res:
					break
			return res	

a = Tree(
		letter='b',
		children=[
			Tree(letter='a',
				children=[
					Tree(letter='r', is_word=True),
					Tree(letter='t', is_word=True)	
				]
			),
			Tree(letter='o',
				children=[
					Tree(letter='b', is_word=True, children=[
						Tree(letter='o', is_word=True)
						]
					)	
				]
			),
		]
	)

print(f"bobo: {spell_check('bobo', a)}") # True
print(f"bar: {spell_check('bar', a)}") # True
print(f"zoro: {spell_check('zoro', a)}") # False