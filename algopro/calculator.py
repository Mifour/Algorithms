"""
A pseudo calculator
"""
def calcul(entry):

	entry = [c for c in entry if c != ' ']

	res = 0
	mem = 1

	if entry.count('(') != entry.count(')'):
		print("Error syntax, invalid string")
		return 0

	for c in range(len(entry)):
		if entry[c] == '(':
			end = entry[c+1:].index(')')
			res += calcul(entry[c+1: c+1+end])
		elif c == '+':
			mem = 1
		elif c == '-':
			mem = -1
		res += mem*float(
				entry[
					c: c+min(
						entry[c:].index('-'), min(
							entry[c:].index('+'), min(
								entry[c:].index('('), entry[c:].index(')')
							)
						)
					)
				]
			)
		mem = 1


	return res

print(calcul('1+ 2 - (5-8)')
# 6

"""
Solution for Joma on AlgoPro

class Solution(object):
  def __eval_helper(self, expression, index):
    op = '+'
    result = 0
    while index < len(expression):
      char = expression[index]
      if char in ('+', '-'):
        op = char
      else:
        value = 0
        if char.isdigit():
          value = int(char)
        elif char == '(':
          (value, index) = self.__eval_helper(expression, index + 1)
        if op == '+':
          result += value
        if op == '-':
          result -= value
      index += 1
    return (result, index)

  def eval(self, expression):
    return self.__eval_helper(expression, 0)[0]

print(Solution().eval('(1 + (2 + (3 + (4 + 5))))'))
# 15
"""
