"""
find the closest value in a BST, given that a node value > every values at left and < every values at right
"""
def findClosestValueInBst(tree, target):
    # Write your code here.
	if tree.value == target:
		return tree.value
	elif tree.value > target and tree.left:
		return findClosestValueInBst(tree.left, target)
	elif tree.value < target and tree.right:
		return findClosestValueInBst(tree.right, target)
	else:
		return tree.value
