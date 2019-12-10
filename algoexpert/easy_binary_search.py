"""
a functionn that the index of a target in a array, else -1, using dichotmous technique
"""
def binarySearch(array, target):
    # Write your code here.
	if array[int(len(array)/2)] == target:
		return int(len(array)/2)
	if array[int(len(array)/2)] < target and int(len(array)/2) > 0:
		res = binarySearch(array[int(len(array)/2):], target)
		return int(len(array)/2) + res if res != -1 else -1
	elif array[int(len(array)/2)] > target and int(len(array)/2) > 0:
		return binarySearch(array[:int(len(array)/2)], target)
	else:
		return -1
