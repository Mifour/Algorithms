def histogram_of_water(array):
	"""
		Given an array (of positive integers) representing a histogram, imagine it starts raining on that histogram.
		The water will fill up the bar until the water falls on a edge.
		Return the amount of water that stay in the histogram.
		O(n) time & space

									    #
							          # #  #
									 ## #  # #
		1,2,3,1,4,0,1,3,0,2,0,1		##### ## # #    -> 10

	"""
	begin = 0
	begin_prev = 0
	end = len(array)-1
	end_prev = 0
	surface = [0 for _ in range(len(array))]

	"""
		Two pointers that create a monotonic increasing/decreasing
		array that represent the surface.
	"""
	while begin <= end:
		if begin_prev >= array[begin]:
			surface[begin] = begin_prev
		else:
			begin_prev = array[begin]
		if end_prev >= array[end]:
			surface[end] = end_prev
		else:
			end_prev = array[end]

		begin +=1
		end -=1

	# water leveraging
	for index in range(len(surface)-1):
		if surface[index] != surface[index+1] and surface[index] !=0 and surface[index+1] !=0:
			surface[index] = min(surface[index], surface[index+1])


	res = 0
	for index in range(len(array)):
		res += max(0, surface[index]-array[index])
	return res

print(histogram_of_water([1,2,3,1,4,0,1,3,0,2,0,1]))
# 10