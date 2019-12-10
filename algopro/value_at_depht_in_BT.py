class Tree():
	def __init__(self, val, left=None, right=None):
		self.value = val
		self.left = left
		self.right = right
		
def value_at_depht_in_BT(tree, depth):
	"""
		O(n) time
		O(n) space
	"""
	if depth == 0:
		return [tree.value]
	if tree.left and tree.right:
		return []+value_at_depht_in_BT(tree.left, depth-1)+value_at_depht_in_BT(tree.right, depth-1)
	if tree.left:
		return []+value_at_depht_in_BT(tree.left, depth-1)
	if tree.right:
		return []+value_at_depht_in_BT(tree.right, depth-1)
	
	