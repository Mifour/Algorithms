class Tree():
	def __init__(self, val, left=None, right=None):
		self.value = val
		self.left = left
		self.right = right

def max_depth(tree):
	if not tree:
		return 0

	depth_rigth=max_depth(tree.right)
	depth_left=max_depth(tree.left)
	return max(depth_left, depth_rigth)+1	

def is_BST_balanced(tree):
	return abs(max_depth(tree.left) - max_depth(tree.right)) < 2

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def isBalanced(self, root):
    def isBalancedHelper(root):
      if root == None:
        return (True, 0)
      leftB, leftH = isBalancedHelper(root.left)
      rightB, rightH = isBalancedHelper(root.right)
      return (leftB and rightB and abs(leftH - rightH) <= 1, max(leftH, rightH) + 1)
    return isBalancedHelper(root)[0]