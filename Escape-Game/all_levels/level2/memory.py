import random

"""
    generateGrid creates an N x M matrix of zeroes, which represents an empty grid.
"""
def generateGrid(n, m):
    grid = []
    for i in range(n):
        grid.append([0] * m)
    return grid

"""
    given some grid, generate a pattern on that grid. We define a pattern as
    on and off, or 0 and 1. We don't use booleans incase of extension to
    different colors/types of squares.
"""
def generatePattern(grid):
    # unsure of what is a good frequency of squares...
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if random.randint(0, 5) >= 4:
                grid[i][j] = 1
    return grid

def playGame():
    # hard coded 5 x 5
    grid = generateGrid(5, 5)
    pattern = generatePattern(grid)
    for row in pattern:
        print(row)

playGame()
