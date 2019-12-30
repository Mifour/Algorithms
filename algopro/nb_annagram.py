def nb_annagram(array):
	import collections
	def hash(string):
		hash = dict(collections.Counter(string))
		return hash

	hashes = set()
	hashing = {}

	for elem in array:
		key = hash(elem)
		hashing[elem] = key
		hashes.add(key)

	return [[key for key, hash in hashing.items() if hash==val ] for val in hashes]

"""
Solution from AlgoPro
"""
import collections

def hashkey(str):
  return "".join(sorted(str))

def hashkey2(str):
  arr = [0] * 26
  for c in str:
    arr[ord(c) - ord('a')] = 1
  return tuple(arr)

def groupAnagramWords(strs):
  groups = collections.defaultdict(list)
  for s in strs:
    groups[hashkey2(s)].append(s)

  return tuple(groups.values())

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# (['abc', 'cba'], ['bcd', 'cbd'], ['efg'])
