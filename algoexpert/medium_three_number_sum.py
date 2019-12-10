"""
find every triplet that sum up to the target
"""
def threeNumberSum(array, targetSum):
    # Write your code here.
	res = []
	for i in range(len(array)):
		for j in range(len(array)):
			for k in range(len(array)):
				if array[i] + array[j] + array[k] == targetSum and (i != j and i != k and j != k):
					tmp = sorted([array[i] , array[j] , array[k]])
					if tmp not in res:
						res.append(tmp)
	return sorted(res)
