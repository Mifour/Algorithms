import numpy as np 

stream = np.random.randint

def find_mean_from_stream(p=100):
	"""
	 O(1) time and space
	"""
	mean = None
	nb = 0
	while True:
		data = stream(p)
		if not mean:
			mean = data
		else:
			mean = (mean*nb + data)/(nb+1)
		nb+=1
		print(mean)

def find_stddev_from_stream(p=100):
	"""
	O(1) time and space
	"""
	mean = None
	total_sum = 0
	total_square = 0
	nb = 0
	stddev = 0
	while True:
		data = stream(p)
		nb+=1
		if not mean:
			mean = data
		else:
			mean = (mean*(nb-1) + data)/(nb)
			stddev = (
				(total_square+data**2)/nb 
				- 2*(total_sum+data)/nb
				+ 2*mean
				+ mean**2
			)
		print(stddev)

def hash_median_from_stream(p=100):
	"""
	O(n) time and space, worst case
	converging O(len(set(n))) time and space
	"""
	dico = {}
	nb = 0
	while True:
		data = stream(p)
		if data in dico:
			dico[data] = dico[data] + 1
		else:
			dico[data] = 1
			sorted_keys = list(sorted(dico.keys()))
		nb+=1
		tmp = 0
		for key in sorted_keys:
			tmp += dico[key]
			if tmp> nb/2:
				median = key
				print(median)
				break



def find_median_from_stream(p=100):
	# WIP
	left = None
	right = None
	median = None
	nb_left = 0
	nb_right = 0
	real = []
	while True:
		data = stream(p)
		real.append(data)
		if not left or not right or not median:
			if not median:
				median = data
			elif data < median:
				left = data
				nb_left+=1
			else:
				right=data
				nb_right+=1
		else:
			if data < median:
				nb_left+=1
				if nb_left > nb_right +1:
					right = median
					median = left
					if data < left:
						left-= (right-median)
					else:
						left+= (right-median)/2
			else:
				nb_right+=1
				if nb_right > nb_left +1:
					left = median
					median = right
					if data > right:
						right+= (median-left)
					else:
						right-= (median-left)/2
			print(f"{median}, error={median - np.median(real)}")
