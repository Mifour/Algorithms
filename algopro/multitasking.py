def multitasking(array, cooldown):
	# given an array of jobs to do and a cooldown time, return the time amount needed to proceed these jobs.
	# Same jobs have to wait the previous cooldown.
	# I.E. [1,1,2,1], cooldown=2 => 7
	# 1,_,_,1,_,_,1,_,_
	#         2,_,_
	# O(n) time & space

	dico = {job:-1 for job in array}
	time = 0
	while array:
		job = array[0]
		if dico[job] <  time :
			dico[job] = time + cooldown
			array.remove(job)
		time+=1
	return time

print(multitasking([1,1,2,1], 2))
print("expected: 7")
print(multitasking([1, 1, 1, 2, 2, 2], 2))
print("expected: 14")
