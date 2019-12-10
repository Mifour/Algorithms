"""
write a function that takes in a non empty array of distinct integers and a integer representing a target sum. If any two numbers in the input array
sum up to the target sum. If any two numbers in the input array sum up to the target sum, the function should return them in a sorted array. 
"""

def twoNumberSum(array, targetSum):
	res = []
	done = []
	for elem in array:
		for other in array:
			if other not in done and other != elem:
				print(f"checking {elem} and {other}")
				if elem + other == targetSum:
					print("found !!")
					res+= [elem, other]
		done.append(elem)
	print(f"res is {res}")
	return sorted(res)
