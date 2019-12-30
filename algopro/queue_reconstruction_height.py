"""
a list of tuple that represents a queue of people
each guy is (height, the number of guy taller or equal as him in front of him)

[(7,0),(4,4),(7,1),(5,0),(6,1),(5,2)]

"""


def resolve(people):
	res = []
	people = sorted(people, key = lambda x: (-x[0],x[1]))

	for guy in people:
		res.insert(guy[1], guy)

	return res
