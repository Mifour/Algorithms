import sys
import numpy as np

def parse_tuple(string):
  return tuple(map(int, string[1:-1].split(",")))
      
poly, point = sys.stdin.read().split("' '")

point = parse_tuple(point[:-1])
poly = list(map(parse_tuple, poly[2:-1].split()))
"""
On a 2d geometric pla, is a point at (x,y) inside a polygon?
"""
def get_equation(p1,p2):
	dx = p2[0]-p1[0] or 0.000001
	a = (p2[1]-p1[1])/dx
	b = p1[1] - a*p1[0]
	return (a,b)
  
def is_in_poly(poly, point):
	# because the poly is convex, there is only need to check if 
	# there is a segment on both side of the point for the same y-value.
	equations = []
	right = False
	left = False
	for n in range(len(poly) -1):
		(a,b) = get_equation(poly[n], poly[n+1])
		if a != 0:
			x = (point[1]-b)/a
			if min(poly[n][0], poly[n+1][0])< x and x < max(poly[n][0], poly[n+1][0]):
				if x < point[0]:
					left = True
				if x >= point[0]:
					# do not considering case the point IS on the edge
					right = True
		else:
			#flat line
			if min(poly[n][0], poly[n+1][0])< x and x < max(poly[n][0], poly[n+1][0]):
				right = True
				left = True
	# compute also the edge between the first and last summits
	(a,b) = get_equation(poly[0], poly[-1])
	if a != 0:
		x = (point[1]-b)/a
		if min(poly[0][0], poly[-1][0])< x and x < max(poly[0][0], poly[-1][0]):
			if x < point[0]:
				left = True
			if x > point[0]:
				# do not considering case the point IS on the edge
				right = True
	else:
		#flat line
		if min(poly[n][0], poly[n+1][0])< x and x < max(poly[n][0], poly[n+1][0]):
			right = True
			left = True
            
	return right and left
print(is_in_poly(poly, point))
