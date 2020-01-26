import os

def mini_git(first, second):
	"""
		Mini git that transform a first file into a second by removing and inserting lines
		O(max(m,n)) time for word of n and m lines
		O(m+n) space
	"""
	if os.path.isfile(first):
		first = open(first).read()
	if os.path.isfile(second):
		second = open(second).read()

	res = []
	first = first.split('\n')
	first_dico = {} 
	second = second.split('\n')
	second_dico = {}
	for line in first:
		first_dico[line] = first_dico[line]+1 if line in first_dico else 1  
	for line in second:
		second_dico[line] = second_dico[line]+1 if line in second_dico else 1  

	index1 = 0
	index2 = 0

	while index1 < len(first) and index2 < len(second):
		line1 = first[index1]
		line2 = second[index2]
		if line1 == line2:
			first_dico[line1] -= 1 
			second_dico[line2] -= 1
			index1+=1
			index2+=1

		else:
			if line1 in second_dico and second_dico[line1] > 0:
				# insertion
				res.append(str(index2)+' + ' + line2)
				second_dico[line2] -= 1
				index2+=1
			else:
				# deletion
				res.append(str(index1)+' - ' + line1)
				first_dico[line1] -= 1
				index1+=1
	return res



print(mini_git('hello\naudi\nis a \ngerman\ncar manufacturer', 'hello\nlada\nis a \ncool\nrussian\ncar manufacturer'))
# expect [
# 	'hello',
# 	'- audi',
#	'+ lada',
#	'- is a germain',
# 	'+ is a russian',
# 	'car manufacturer'
# ]
print(mini_git("hello\nis it\nme\nyou're\nlooking\nfor?", "hello\nNO YOU'RE NOT\nLEAVE ME ALONE\nis it\nme\nyou're\nlooking\nfor?"))
print(mini_git("cannibals.py", "cannibals2.py"))