def fisrt_and_last(array, value):
	"""
	O_time(log(n))
	O_space(1)
	"""

	p1 = int(len(array)/2)
	p2 = p1

	b1 = (0, len(array)-1)
	b2 = (0, len(array)-1)
	while b1[0] != b1[1]-1:
		if array[p1] < value:
			b1[0] = p1
			p1 = int(p1/2)
		if array[p1] >= value:
			b1[1] = p1
			p1 = int(len(array)-(len(array)-p1)/2)
	while b2[0] != b2[1]-1:
		if array[p2] <= value:
			b2[0] = p2
			p2 = int(p2/2)
		if array[p2] > value:
			b2[1] = p2
			p2 = int(len(array)-(len(array)-p2)/2)

	return [p1,p2]

