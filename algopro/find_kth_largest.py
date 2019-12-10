import heapq

def findKthLargest(array, k):
	array = [-val for val in array]
	heapq.heapify(array)
	for i in range(0, k - 2):
		heapq.heappop(array)
		
	return -heapq.heappop(array)