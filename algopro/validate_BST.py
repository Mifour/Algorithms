class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left= None
		self.right = None

def validate_BST(root):
"""
O(n) time and space
"""
	def helper(node, lower, upper):
		if not node:
			return True
		if node.val < lower or node.val> upper:
			return False
		if not helper(node.left, lower, node.val):
			return False
		if not helper(node.right, node.val, upper):
			return False
		return True
	return helper(root, float('-inf'), float('inf'))
 
