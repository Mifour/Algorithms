def solve(array):
	counts = {}

	for elem in array:
		counts[elem] = 1+ counts.get(elem) or 0

	for key,value in counts.items():
		if value ==1:
			return key

def solve2(array):
	unique = 0
	for n in array:
		unique ^= n
	return unique