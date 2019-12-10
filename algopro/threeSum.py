def twoSum(array, target):
	res = []
	p1 = 0
	p2 = len(array)-1

	while p1 != p2:
		if array[p1] + array[p2] < target:
			p1 +=1
		if array[p1] + array[p2] = target:
			res.append([p1,p2])
		if array[p1] + array[p2] > target:
			p2 -=1
	return res

def threeSum(array):
	res = []
	array = sorted(array)
	for elem in range(len(array)-2):
		res += [[array(elem),ts[0], ts[1]] for ts in twoSum(array[elem:],array[elem]) ]
	returnres