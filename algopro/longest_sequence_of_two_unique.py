def longest_sequence_of_two_unique(array):
	lenght = 0 
	max_length = 0
	tmp = []

	for elem in array:
		if len(tmp) < 2:
			if elem not in tmp:
				tmp.append(elem)
			lenght +=1
			max_length +=1

		if len(tmp) == 2:
			if elem not in tmp:
				tmp[0] = tmp[1]
				tmp[1] = elem
				lenght = 0
			else:
				lenght += 1
			max_length = max(max_length, lenght)

	return max_length