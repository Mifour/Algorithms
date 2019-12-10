def invertBinaryTree(tree):
    # Write your code here.
	tmp = tree.left
	tree.left = tree.right
	tree.right = tmp
	
	if tree.left is not None:
		invertBinaryTree(tree.left)
	if tree.right is not None:
		invertBinaryTree(tree.right)
		
	return tree
