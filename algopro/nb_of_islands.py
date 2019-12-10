import numpy as np
def nb_of_islands(matrix):
	"""
		O(n**2) time
		O(1) space, no additionnal space
	"""
	nb = 2
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			if matrix[i,j] == 1:
				linked = []
				for x in range(0,3,2):
					if matrix[min(max(i+x-1, 0), matrix.shape[0]),j] == 1:
						linked.append((min(max(i+x-1, 0), matrix.shape[0]),j))
					if matrix[i, min(max(j+x-1, 0), matrix.shape[1])] == 1:
						linked.append((i, min(max(j+x-1, 0), matrix.shape[0])))
				while linked:
					col, row = linked.pop()
					matrix[col, row] = nb
					for x in range(0,3,2):
						if matrix[min(max(col+x-1, 0), matrix.shape[0]),row] == 1:
							linked.append((min(max(col+x-1, 0), matrix.shape[0]),row))
						if matrix[col, min(max(row+x-1, 0), matrix.shape[1])] == 1:
							linked.append((col, min(max(row+x-1, 0), matrix.shape[1])))
				nb+=1
	return nb - 2

class Solution:
  def numIslands(self, grid):
    def sinkIsland(grid, r, c):
      if grid[r][c] == '1':
        grid[r][c] = '0'
      else:
        return
      if r + 1 < len(grid):
        sinkIsland(grid, r + 1, c)
      if r - 1 >= 0:
        sinkIsland(grid, r - 1, c)
      if c + 1 < len(grid[0]):
        sinkIsland(grid, r, c + 1)
      if c - 1 >= 0:
        sinkIsland(grid, r, c - 1)
    counter = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == '1':
          counter += 1
          sinkIsland(grid, i, j)
    return counter