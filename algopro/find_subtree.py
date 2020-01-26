class Tree:
	def __init__(self, val=None, left=None, right=None):
		self.val=val
		self.left=left
		self.right=right

	def hash(self):
		hash_value = str(self.val)
		if isinstance(self.left, Tree):
			hash_value += self.left.hash()
		if isinstance(self.right, Tree):
			hash_value += self.right.hash()
		return hash_value

def find_subtree(t,s):
	"""
		Check if s in contained in t
		hashing trees into str then check strings matching using sliding windows
	"""
	hash_t = t.hash()
	hash_s = s.hash()
	index=0
	while index < len(hash_t):
		tmp=0
		while hash_t[index+tmp] == hash_s[tmp]:
			if tmp == len(hash_s)-1:
				return True
			tmp+=1
		index += max(tmp,1)
	return False 




a = Tree(1, Tree(4,3,2), Tree(5,4,-1))
a2 = Tree(1, Tree(4,Tree(4,3,2), 0), Tree(5,4,-1))
b = Tree(4,3,2)
c = Tree(2,7,8)

print(find_subtree(a,b))
print(find_subtree(a,c))
print(find_subtree(a2,b))