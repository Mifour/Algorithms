def validateBst(tree):
    # Write your code here.
	def is_ok(tree, value):
		ok = True
		if tree.left:
			gauche = is_ok(tree.left, tree.value)
			ok = tree.left.value <= tree.value
		else:
			gauche = True
		if tree.right:
			droite = is_ok(tree.right, tree.value)
			ok = tree.right.value >= tree.value
		else:
			droite = True
		return ok and gauche and droite
	
	#return is_ok(tree, tree.value)

	def arraytizer(tree, array):
		if tree.left:
			array += arraytizer(tree.left, array)
		array += [tree.value]
		if tree.right:
			array += arraytizer(tree.right, array)
		return array
	res = arraytizer(tree, [])
	return res == sorted(res)
