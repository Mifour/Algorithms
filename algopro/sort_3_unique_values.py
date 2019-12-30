"""
[3,3,2,1,3,2,1] -> [1,1,2,2,3,3,3]

O(n) time
O(1) space
"""
def sort_3_unique_values(array):
	counts = {}
	for n in array:
		counts[n] = 1 + counts.get(n,0) or 0
	keys = sorted(counts.keys())
	
	return ([keys[0] for n in range(counts[keys[0]])]
		+[keys[1] for n in range(counts[keys[1]])]
		+[keys[2] for n in range(counts[keys[2]])] 
	)
