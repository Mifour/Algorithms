class Tree():
	def __init__(self, val, left=None, right=None):
		self.value = val
		self.left = left
		self.right = right

def nb_unival_subtree(tree):
	if not tree:
		return 0
	if tree.value in (tree.left, None) and tree.value in (tree.right, None):
		return nb_unival_subtree(tree.left) + nb_unival_subtree(tree.right) + 1	
	return nb_unival_subtree(tree.left) + nb_unival_subtree(tree.right)


a = Tree(0)
a.left = Tree(1)
a.right = Tree(0)
a.right.left = Tree(1)
a.right.right = Tree(0)
a.right.left.left = Tree(1)
a.right.left.right = Tree(1)
