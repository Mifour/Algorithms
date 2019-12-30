import math

def unique_paths(m,n):
"""
Count the number of unique paths on a grid starting from top left and going to bottom right
Only rigth and down moves are allowed
O(n) time, because of factorial
O(1) space
"""
	return math.fatorial(m-1 + n-1)/(math.factorial(m-1)*math.factorial(m-1))
