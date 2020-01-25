def is_number(string):
	"""
		check if a string is a valid number or not
		O(n) time 
		O(1) space
	"""
	has_point = False
	has_e = False
	can_be_minus = True
	digits = {'0','1','2','3','4','5','6','7','8','9'}
	for c in string:
		if c == '-':
			if can_be_minus:
				can_be_minus=False
			else:
				return False
		elif c == ' ':
			return False
		elif c == 'e':
			if not has_e:
				has_e = True
				can_be_minus = True
			else:
				return False
		elif c == '.':
			if not has_point:
				has_point = True
			else:
				return False
		else: 
			if not c in digits:
				return False
	return True

print(f"3: {is_number('3')}")
print(f"-99999999.0: {is_number('-99999999.0')}")
print(f"9..10: {is_number('9..10')}")
print(f"2+3i: {is_number('2+3i')}")
print(f"-3.7e-12: {is_number('-3.7e-12')}")
print(f"-3.-7e12: {is_number('-3.-7e12')}")
print(f"7 3: {is_number('7 3')}")


