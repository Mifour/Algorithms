import numpy as np

def nb_path_maze(maze):
	"""
	Given a maze with 0 as paths and 1 as walls, beginning at top left,
	with only possibilities to go down or right. Return the number of possible paths.

	O(n) time and space
	"""
	I,J = maze.shape
	sheet = np.zeros((I,J))

	sheet[0,0] = 1

	for i in range(I):
		for j in range(J):
			if maze[i,j] == 0 and (i,j) != (0,0) :
				sheet[i,j] = sheet[max(0,i-1),j] + sheet[i,max(0,j-1)]

	return sheet[i,j]

maze = np.array(
	[[0,1,0],
	 [0,0,1],
	 [0,0,0]]
	)
print(maze)
print(f"{nb_path_maze(maze)}, expected 2") 

maze = np.array(
	[[0,1,0,0],
	 [0,0,0,0],
	 [1,0,1,0],
	 [0,0,0,0]]
	)
print(maze)
print(f"{nb_path_maze(maze)}, expected 2") 

maze = np.array(
	[[0,0,1,0],
	 [0,0,0,0],
	 [1,0,1,0],
	 [0,0,0,0]]
	)
print(maze)
print(f"{nb_path_maze(maze)}, expected 4") 

maze = np.array(
	[[0,0,0,0],
	 [0,0,1,0],
	 [0,1,0,0],
	 [0,0,0,0]]
	)
print(maze)
print(f"{nb_path_maze(maze)}, expected 2") 
