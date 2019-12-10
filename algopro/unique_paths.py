import math

def unique_paths(m,n):
	return math.fatorial(m-1 + n-1)/(math.factorial(m-1)*math.factorial(m-1))