def fib(n):
	"""
	O(2**n) time and space
	"""
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

def fib(n):
	"""
	O(n) time
	O(1) space
	"""
	first = 0
	second = 1
	for i in range(2,n+1):
		tmp = first+second
		first=second
		second = tmp
	return second