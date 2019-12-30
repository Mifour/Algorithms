"""
return the depth of a tree
O(n) time and space
"""
class Tree:
	def __init__(self, val, left= None, right=None):
		self.val = val
		self.left = left
		self.right = right

def max_depth(tree):
	depth_left = max_depth(tree.left) if tree.left else 0
	depth_right = max_depth(tree.right) if tree.right else 0

	return max(depth_left, depth_right)+1

	
