import math
def nb_parentheses_comb(nb_pairs):
	return math.factorial(2*nb_pairs-2)/(4*(math.factorial(nb_pairs-1))**2)


class Solution:
  def generateParentheses(self, n):
    res = []

    def backtrack(S, left, right):
      if len(S) == 2*n:
        res.append(S)
        return
      if left < n:
        backtrack(S+'(', left+1, right)
      if left > right:
        backtrack(S+')', left, right+1)
    backtrack('', 0, 0)
    return res


print(Solution().generateParentheses(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']