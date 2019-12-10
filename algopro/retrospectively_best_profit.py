def retrospectively_best_profit(array):
	"""
	given an array of recored stocks during a period, 
	what the best profit possible on that period?

	O(n**2) time
	"""
	best_profit = 0
	for buy_day in array:
		profit = max(array[buy_day:]) - buy_day
		best_profit = max(best_profit, profit)

	return best_profit

def retrospectively_best_profit2(array):
	"""
	given an array of recored stocks during a period, 
	what the best profit possible on that period?

	O(n) time
	O(n) space
	"""
	maxes = [0 for n in range(len(array))]
	maxes[-1] = array[-1] 
	for elem in range(len(array)-2, 0, -1):
		maxes[elem] = max(array[elem], maxes[elem+1])
	
	best_profit = 0
	for i in range(len(array)):
		profit = maxes[i] - array[i]
		best_profit = max(best_profit, profit)

	return best_profit

