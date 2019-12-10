def partition(number):
	answer = set()
	answer.add((number, ))
	for x in range(1, number):
		for y in partition(number - x):
			answer.add(tuple(sorted((x, ) + y)))
	return answer


def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	res = 0
	for solution in partition(n):
		if all(elem in denoms  for elem in solution):
			res += 1
	return res
			
