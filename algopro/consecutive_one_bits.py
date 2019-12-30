def consecutive_one_bits(n):
	n = numberToBase(n,2)
	nb = 0
	longest = 0
	for index in range(len(n)):
		if n[index] == 1:
			nb +=1
		else:
			nb = 0
		longest = max(nb, longest)
	return longest

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b)) # modulo
        n //= b # entire divison
    return digits[::-1]
    

# solution from the Techlead on Algropro
def longest_run(n):
  longest_run = 0
  current_run = 0
  BITMASK = 1

  while n != 0:
    if n & BITMASK == 0:
      longest_run = max(longest_run, current_run)
      current_run = 0
    else:
      current_run += 1
    n = n >> 1
  longest_run = max(longest_run, current_run)
  return longest_run

print(longest_run(242))
# 4