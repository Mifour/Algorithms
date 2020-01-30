""" 
Super MasterMind game and solver
by Thomas Dufour, 21st dec 2019

rules: 
	the code is 5 digits from 0 to 9 (8 colors + None color)
	number of unique codes = 59049
	the score is :
		1 black for 1 color well placed
		1 white for 1 color misplaced
		there are no information about position
	the game ends when all 5 dots are guessed (score = 5 blacks, 0 whites)
"""
import numpy as np

class Code:
	def __init__(self, code = None):
		if code:
			self.code = code
		else:
			self.code = np.random.randint(9, size= 5).tolist()

	def __str__(self):
		return "[" + ",".join(str(e) for e in self.code) + "]"

	def __repr__(self):
		return "[" + ",".join(str(e) for e in self.code) + "]"

	def score(self, attempt):
		black = 0
		white = 0
		to_eval = self.code.copy()
		to_del = []
		for dot in range(5):
			if attempt[dot] == to_eval[dot]:
				black +=1
				to_del.append(dot)

		deleted = 0
		for dot in to_del:
			del to_eval[dot-deleted]
			del attempt[dot-deleted]
			deleted +=1

		for dot in attempt:
			if dot in to_eval:
				white +=1
				to_eval.remove(dot)

		return (black, white)

def brut_mind(code = Code(), display=False):
	"""
	Pseudo brut force
	determine the colors used then, try every combinaisons
	max number of tries = 129 
	O(m colors + n! positions)
	"""
	from itertools import permutations
	print(f"code is {code}")

	turn = 0
	completed = False
	used_colors = []
	while not completed:
		# 1st phase
		for color in range(9):
			if display:
				print(f'trying {color}')
			score  = code.score([color,color,color,color,color])
			used_colors+= [color for i in range(score[0])]
			if len(used_colors) == 5:
				break
		if display:
			print(f"colors found are {used_colors}")

		# 2nd phase
		for attempt in list(permutations(used_colors)):
			if display:
				print(f"attempt {attempt}")
			score  = code.score(list(attempt))
			completed = score == (5,0)
			if completed:
				break
			turn +=1
	print(f"the code was {attempt}")

	print(f"completed in {turn} turn(s)")

def master_mind(code = Code(), display=False, silent=False):
	"""
	Determine the colors used. 
	While searching for colors, try to get information about positions.
	Then, try every combinaisons that match both the dots we're sure about 
	and none of the impossible combinaisons.

	In phase 2, remove permutations that do not have the same score with the attemps than the attempts had themself
		This comes from the evaluation between two attemps has to be the same than the evaluation to the actual 
		code in order to be coherent. 
	
	Average observed score : 7.62
	Median score: 8 

	O(m colors + n! positions)
	"""
	from itertools import permutations
	if not silent:
		print(f"code is {code}")

	turn = 0
	completed = False
	used_colors = []
	certain = [None,None,None,None,None]
	impossible = []
	trace_attemps = {}
	to_pos_test = None
	bits = 0
	while not completed:
		# 1st phase
		# determine the used colors and get some information on their positions

		#import pdb; pdb.set_trace()

		for color in range(9):
			if to_pos_test is not None:
				# determining the next possible position to do the position test on
				# get all non-determined positions
				# remove the one where the color cannot be
				# get the first one or 0
				possible = [k for k,v in enumerate(certain) if v is None]
				for to_remove in [k for nope in impossible for k,v in enumerate(nope) if v == to_pos_test]:
					if to_remove in possible:
						possible.remove(to_remove)
				position = next(iter(possible), 0)
				attempt = [color for i in range(position)] + [to_pos_test] + [color for i in range(4-position)]
				if display:
						print(attempt)
						print(f'testing {color} and {to_pos_test} at {position}')
				score  = code.score(attempt.copy())
				if display:
					print(f"adding {attempt} to trace_attemps")
				trace_attemps[",".join([str(color) for color in attempt])]=score
				next_color = color if score[0]+score[1] > len(used_colors) else to_pos_test

				if display:
					print(score)
				if score[1] > 0: # 1 answer bit can be white (2 in some rare cases)
					used_colors+= [color for i in range(score[0] + score[1]-1)]
					impossible.append(
						[None for i in range(position)] + [to_pos_test] + [None for i in range(4-position)]
					)
					if display:
						print(f'color {to_pos_test} cannot be at position {position}')
				else:
					used_colors+= [color for i in range(score[0] - 1)]
					certain[position] = to_pos_test
					if display:
						print(f'color {to_pos_test} is certain to be at position {position}')
				to_pos_test = next_color

			else:
				if display:
						print(f'testing {color}')
				attempt = [color,color,color,color,color]
				if display:
					print(attempt)
				score  = code.score(attempt.copy())
				if display:
					print(f"adding {attempt} to trace_attemps")
				trace_attemps[",".join([str(color) for color in attempt])]=score
				if display:
					print(score)
				used_colors+= [color for i in range(score[0])]
				if score[0] > 0:
					to_pos_test = color
			if len(used_colors) == 5:
				break
			turn += 1

		if display:
			print(f"colors found are {used_colors}")
			print(f'certain : {certain}')
			print(f'impossible:')
			for nope in impossible:
				print(nope)
			print(f'trace_attemps:')
			for trace in trace_attemps:
				print(trace)

		# 2nd phase
		for attempt in list(permutations(used_colors)):
			attempt = list(attempt)
			coherent = True
			for trace in trace_attemps:
				if display:
					print(f"checkibg coherence with {trace}")
				if Code([int(color) for color in trace.split(',')]).score(attempt.copy()) != trace_attemps[trace]:
					coherent = False

			if (
				coherent 
				and attempt == [certain[i] or attempt[i] for i in range(5)] # must comply certain
				and not any([attempt[i] == nope[i] for nope in impossible for i in range(5)]) # must be completly different than impossible
			):
				if display:
					print(f"attempt {attempt}")
				score  = code.score(attempt.copy())
				trace_attemps[",".join([str(color) for color in attempt])]=score
				completed = score == (5,0)
				if completed:
					answer = attempt
					break
				turn +=1
	if not silent:
		print(f"the code was {answer}")
		print(f"completed in {turn} turn(s)")
	else:
		return turn
