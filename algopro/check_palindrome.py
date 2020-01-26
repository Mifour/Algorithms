def check_palindrome(string):
	"""
		Check if the given string can be rearange as a palidnrome 
		and if so, give a palidrome
		O(n) time for n long string
		O(n) space, worst case
	"""

	dico = {}
	for letter in string:
		dico[letter] = dico[letter]+1 if letter in dico else 1
	palindrome = ''
	even = ''
	for k,v in dico.items():
		if v % 2 ==1:
			even+=k
			if len(even) > 1:
				return False
		palindrome = k*int(v/2) + palindrome + k*int(v/2)
	if even != '':
		palindrome = palindrome[:int(len(palindrome)/2)] + even + palindrome[int(len(palindrome)/2):]
	return palindrome

print(f"abc: {check_palindrome('abc')}")
print(f"abababab: {check_palindrome('abababab')}")
print(f"ababababc: {check_palindrome('ababababc')}")
