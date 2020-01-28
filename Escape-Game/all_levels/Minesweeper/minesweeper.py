import random

# for some square, get the coordinates of all of its valid pairs on the board
def getNeighbors(i, j, board):
    neighbors = []

    if i > 0:
        neighbors.append([i-1, j])
        if j > 0:
            neighbors.append([i-1, j-1])
        if j < len(board[0]) - 1:
            neighbors.append([i-1, j+1])

    if j > 0:
        neighbors.append([i, j-1])

    if i < len(board) - 1:
        neighbors.append([i+1, j])
        if j > 0:
            neighbors.append([i+1, j-1])
        if j < len(board[0]) - 1:
            neighbors.append([i+1, j+1])

    if j < len(board[0]) - 1:
        neighbors.append([i, j+1])

    return neighbors

    

def getNumberOfNearbyBombs(i, j, board):
    count = 0
    for neighbor in getNeighbors(i, j, board):
        [x, y] = neighbor
        if board[x][y] == -1:
            count += 1

    return count

# we will generate easy boards with 8 x 8 and 10 bombs for now
def generateBoard():
    # this n is hardcorded... see above
    n = 8

    # generate an empty board
    board = []
    for i in range(n):
        board.append([0] * n)

    # generate bombs
    for loc in random.sample(range(0, n * n - 1), 10):
        x = loc // n
        y = loc % n
        board[x][y] = -1

    # calculate nearby bomb counts
    for i in range(n):
        for j in range(n):
            if board[i][j] != -1:
                board[i][j] = getNumberOfNearbyBombs(i, j, board)

    # translate to objects
    # Properties:
    # 1. isFlipped (bool)
    # 2. isBomb (bool)
    # 3. count (int)
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                board[i][j] = {
                    "isFlipped": False,
                    "isBomb": True,
                    "isFlagged": False,
                    "count": 0,
                }
            else:
                board[i][j] = {
                    "isFlipped": False,
                    "isBomb": False,
                    "isFlagged": False,
                    "count": board[i][j]
                }

    return board
        

