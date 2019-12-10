def question43(array, target):
	"""
		for a array and a positive integer, find the minimun length
		of a contigous subarray that sums up to the integer
	"""
	max_sum = float('-inf')
	length = 1
	while max_sum < target:
		for i in range(len(array)-length+1):
			max_sum == sum(array[i:i+length+1])

		length +=1

	return length