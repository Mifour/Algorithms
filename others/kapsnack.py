def knapsnak_brute(capacity, values, weights):
	"""
		brute force of knapsack problem
		O(2**n) time and space, for n objects
	"""
	def increment(binary):
		index = -1
		if binary[index] == 0:
			binary[index] = 1
			return binary
		while binary[index] == 1:
			binary[index] = 0
			index-=1
		binary[index] = 1
		return binary
	n = len(values)
	combi = [0 for _ in range(n)]
	res = {}
	for i in range(2**n):
		key = ''.join([str(bit) for bit in combi])
		total_weight = sum([combi[i] * weights[i] for i in range(n)])
		total_value = sum([combi[i] * values[i] for i in range(n)])
		res[key] = (total_weight,total_value)
		combi = increment(combi)
	max_weight = 0
	max_value = 0
	best_sol = ''
	for k,w,v in res.items():
		if w <= capacity:
			if v > max_value:
				max_value = v 
				max_weight = w
				best_sol = k 
	print(f"best solution is {best_sol} with value: {max_value} and weight: {max_weight}")




def kapsnack_0(capacity, values, weights):
	"""
		Kapsnack problem
		for a total wieght < capacity, return the set of objects with greatest value sum.
	"""

	res = []
	tmp = []

	if len(values) < 2 and sum(weights) > capacity:
		# backpack is full
		return ([], 0)

	if sum(weights) <= capacity:
		# can take everything, no choice to do
		return ([i for i in range(len(values))], sum(values))

	else: 
		# the problem is choice
		for objekt in len(values):
			tmp.append( 
				kapsnack(capacity - weights[objekt], values.copy().remove(objekt), weights.copy(objekt))
			)
		max_value = max([sol[1] for sol in tmp ])
		best_choice = [sol for sol, value in tmp if value == max_value][0]
		sub_sol = 
		return [elem for elem in a if elem < n ] + [n] + [elem+1 for elem in a if elem >=n]

def knapsack_sol(p,v, cmax):
	n =len(p)
	opt = [[0] * (cmax+1) for _ in range(n+1)]
	sel = [[False] * (cmax+1) for _ in range(n+1)]
	for cap in range(p[0], cmax+1):
		opt[0][cap] = v[0]
		sel[0][cap] = True
	for i in range(1, n):
		for cap in range(cmax+1):
			if cap >= p[i] and opt[i-1][cap - p[i]] +v[i] > opt[i-1][cap]:
				opt[i][cap] = opt[i-1][cap-p[i]] + v[i]
				sel[i][cap] = True
			else:
				opt[i][cap] = opt[i-1][cap]
				sel[i][cap] = False
	cap = cmax
	sol = []
	for i in range(n-1,-1,-1):
		if sel[i][cap]:
			sol.append(i)
			cap-= p[i]
	return (opt[n-1][cmax], sol)

