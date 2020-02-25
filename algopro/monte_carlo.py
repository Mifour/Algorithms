import numpy as np

"""
	monte carlo algorithm
	O(n) time for n points
	O(1) space
"""

def monte_carlo():
	inside = 1
	total = 1
	while True:
		x,y = np.random.rand(2)
		if x**2 + y**2 <= 1:
			inside +=1
		total +=1
		print((inside*4)/total)
		#surface_circle = pi*(1**2) = pi
		#total_square = (2*1)**2
		#pi = surface_circle * 4/total_square
		