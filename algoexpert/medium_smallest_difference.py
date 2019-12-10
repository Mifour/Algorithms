"""
for two input arrays, find the closest two elements
"""
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	smallest = float("inf")
	res = []
	for eleone in arrayOne:
		for eletwo in arrayTwo:
			if abs(eleone -eletwo) < smallest:
				smallest = abs(eleone-eletwo)
				res = [eleone, eletwo]
	return res
