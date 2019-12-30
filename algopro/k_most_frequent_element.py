def k_most_frequent_element(array, k):
"""
O(n) time and space
"""
	dico = {}
	for elem in array:
		dico[elem] = dico[elem]+1 if elem in dico else 1

	dico = sorted(dico, key = lambda k: dico[k], reverse= True)

	return dico[:k]

"""
Solution from AlgoPro
"""

def topKFrequent(self, nums, k):
    count = collections.defaultdict(int)
    for n in nums:
      count[n] += 1
    heap = []
    for key, v in count.items():
      heapq.heappush(heap, (v, key))
      if len(heap) > k:
        heapq.heappop(heap)
    res = []
    while len(heap) > 0:
      res.append(heapq.heappop(heap)[1])
    return res
