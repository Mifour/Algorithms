def is_non_decresing(array):
	max_tmp =  float('-inf')
	for elem in array:
		if elem >= max_tmp:
			max_tmp = elem
		else:
			# is decreasing
			return False
	return True

def solve(array):
	max_tmp = float('-inf')

	for n in range(len(array)):
		if array[n] >= max_tmp:
			max_tmp = array[n]
		else:
			return is_non_decresing(array[n+1])
	return True

def other_solve(array):
	nb_decrease = 0
	max_tmp= float('-inf')

	for elem in array:
		if elem >= max_tmp:
			max_tmp= elem
		else:
			# decreasing
			nb_decrease += 1

		if nb_decrease > 1:
			return False

	return True


class Solution:
  def checkPossibility(self, nums):
    idx = None
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        # if there's two dip or more
        if idx is not None:
          return False
        idx = i
    # if there's no dip
    if idx is None:
      return True
    # if there's only one dip
    if idx == 0:
      return True
    if idx == len(nums) - 2:
      return True
    if nums[idx] <= nums[idx + 2]:
      return True
    if nums[idx - 1] <= nums[idx + 1]:
      return True
    return False