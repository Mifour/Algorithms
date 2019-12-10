def bubbleSort(array):
    # Write your code here.
	good = False
	swapped = False
	while not good:
		for n in range(len(array)-1):
			swapped = False		
			if array[n] > array[n+1]:
				tmp = array[n]
				array[n] = array[n+1]
				array[n+1] = tmp
				swapped = True
				break
		if swapped == False:
			good = True
	return array
			
