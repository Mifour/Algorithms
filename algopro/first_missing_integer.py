def first_missing_integer(array):
	mini = set(array)
	i = 1
	while i in mini:
		i+=1
	return i
