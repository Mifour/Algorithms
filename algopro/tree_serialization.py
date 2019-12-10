class Tree:
	def __init__(self,val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def tree2array_serizalization(tree):
	"""
	O(n) time
	O(n) space
	"""
	res = []
	if tree is None:
		return res
	if tree.left:
		res+= tree_serizalization(tree.left)
	res += [tree.val]
	if tree.right:
		res+= tree_serizalization(tree.right)
	return res

def array2tree_serialization(array, tree=Tree()):
	"""
	O(n) time
	O(n) space
	"""
	if len(array) == 0:
		return None
	if len(array) == 1:
		return 	Tree(val=array[0])

	tree.val = array(int(len(array)/2))
	tree.left = array2tree_serialization(array[:int(len(array)/2)]) 
	if len(array) > 2:
		tree.right = array2tree_serialization(array[int(len(array)/2)+1:])

	return tree

#################### solution
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    result = ''
    result += str(self.val)
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
    return result


def serialize(node):
  if node == None:
    return '#'
  return str(node.val) + ' ' + serialize(node.left) + ' ' + serialize(node.right)


def deserialize(str):
  def deserialize_helper(values):
    value = next(values)
    if value == '#':
      return None
    node = Node(int(value))
    node.left = deserialize_helper(values)
    node.right = deserialize_helper(values)
    return node
  values = iter(str.split())
  return deserialize_helper(values)