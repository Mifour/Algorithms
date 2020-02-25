def character_mapping(string_a, string_b):
	"""
	Return a boolean of either it is possible to map every unique character from string a to string b with a one to one relation.
	O(n log n) time
	O(n) space
	"""

	dico_a = {}
	dico_b = {}

	for char in string_a:
		dico_a[char] = dico_a[char]+1 if char in dico_a else 1
	for char in string_b:
		dico_b[char] = dico_b[char]+1 if char in dico_b else 1

	count_a = sorted(dico_a.values(), reverse=True)
	count_b = sorted(dico_b.values(), reverse=True)

	return count_a == count_b and len(string_a) == len(string_b)

print(character_mapping("abc", "def")) #True
print(character_mapping("aac", "def")) #False
print(character_mapping("abc", "dee")) #False
print(character_mapping("abc", "deef")) #False