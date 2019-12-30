# solution from the Techlead on Algopro
def romans_to_ints(string):
	dico = {"I": 1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
	prev = 0
	total = 0
	for i in string[::-1]:
		curr = dico[i]
		total += -curr if curr < prev else curr
		prev = curr
	return total
