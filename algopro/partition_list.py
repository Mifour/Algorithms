def partition_list(array, pivot):
	"""
	Given an unsorted list and a pivot integer, partition the list in two depending if the elements are smaller or greater than the pivot.
	O(n) time & space
	"""
	smaller = []
	bigger = []
	for element in array:
		if element < pivot:
			smaller.append(element)
		else:
			bigger.append(element)
	return [smaller, bigger]


print(f"{partition_list([8,9,2,4,1,0], 3)}, expected [[2,1,0], [8,9,4]]")

def partition_list_swap(array, pivot):
	"""
	O(n) time 
	O(1) space
	"""
	nb_smaller = 0
	for index in range(len(array)-1, -1, -1):
		if array[index] >= pivot:
			element = array[index]
			del array[index]
			array.append(element)
		else:
			nb_smaller+=1
	return [array[:nb_smaller], array[nb_smaller:]]


print(f"{partition_list_swap([8,9,2,4,1,0], 3)}, expected [[2,1,0], [4,9,8]]")