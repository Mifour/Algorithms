def getNthFib(n):
    # Write your code here.
	if n == 0:
		return 0
	if n == 1:
		return 1
	res = getNthFib(n-1) + getNthFib(n-2)
	return res
