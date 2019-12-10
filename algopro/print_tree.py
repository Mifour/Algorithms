class Tree:
	def __init__(self, val, children=[]):
		self.val=val
		self.children = children

def print_tree(tree):
	"""
	print a tree level by level with unlimited children nodes
	O(n) time
	O(n) space
	"""
	list_nodes = []
	next_nodes = []
	list_nodes.append(tree)
	while list_nodes:
		print(''.join([str(node.val) for node in list_nodes]))
		index = len(list_nodes)
		for node in list_nodes:
			for child in node.children:
				next_nodes.append(child)
		list_nodes = next_nodes
		next_nodes = []
