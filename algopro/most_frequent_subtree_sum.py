class Tree:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left=left
		self.right=right

def most_frequent_subtree_sum(node, dico = {}):
	"""
	Given a Binary Tree, return the most frequent subtree sum as val+left+right
	O(n) time & space
	"""

	left = most_frequent_subtree_sum(node.left, dico) if node.left else 0
	right = most_frequent_subtree_sum(node.right, dico) if node.right else 0

	total = node.val + left + right

	dico[total] = dico[total] +1 if total in dico else 1

	most_frequent = sorted(dico.items(), key= lambda k: k[0], reverse=True) 
	return most_frequent[0][1]

a = Tree(3, left=Tree(1), right=Tree(-3))

print(f"{most_frequent_subtree_sum(a)}, expected 1")


