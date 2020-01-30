import pygame, sys
from all_levels.Minesweeper.common import initScreenAndGameClock, drawTopBar, hashRect
from all_levels.Minesweeper.constant import X_DIMENSION, Y_DIMENSION, BOARD_M, BOARD_N, TOPBAR_RATIO, SQUARE_SPACING, WHITE
from all_levels.Minesweeper.minesweeper import generateBoard, getNeighbors

# initialize basic elements
[screen, gameClock] = initScreenAndGameClock()
afont = pygame.font.SysFont("Helvetica", 30, bold=False)
flag = pygame.image.load("./all_levels/Minesweeper/assets/flag.png").convert_alpha()
bomb = pygame.image.load("./all_levels/Minesweeper/assets/bomb.png").convert_alpha()
mineStart = pygame.image.load("./assets/Nuestrosweeper_tutorial.png").convert_alpha()

def drawTable(screen, area):
    [areax, areay] = area
    height = areay - ((Y_DIMENSION / TOPBAR_RATIO)) // 16
    width = areax - ((X_DIMENSION / TOPBAR_RATIO)) // 16

    x = (Y_DIMENSION / TOPBAR_RATIO) // 32
    y = (Y_DIMENSION / TOPBAR_RATIO) * 1.03125

    pygame.draw.rect(screen, (255, 144, 0),
                     pygame.Rect((x, y), (width, height)))

    # size of the table
    return [[x, y], [width, height]]


def drawSquare(screen, x, y, width, height, number):
    text = str(number["count"])

    if number["isFlagged"]:
        square = pygame.draw.rect(screen, (10, 255, 100), pygame.Rect((x, y), (width, height)))
        screen.blit(flag, (x + (width) // 2, y + (height) // 4))
    elif number["isFlipped"]:
        if number["isBomb"]:
            square = pygame.draw.rect(screen, (100, 144, 255), pygame.Rect((x, y), (width, height)))
            screen.blit(bomb, (x + (width) // 4, y + (height) // 4))
        else:
            square = pygame.draw.rect(screen, (200, 20, 100), pygame.Rect((x, y), (width, height)))
            textObject = afont.render(text, True, (0, 0, 0,))
            screen.blit(textObject, (x - 10 + width // 2, y + height // 3))
    else:
        square = pygame.draw.rect(screen, (100, 144, 100), pygame.Rect((x, y), (width, height)))
    return square

def drawSquares(screen, n, m, tableCorner, tableArea, board):
    [tableCornerX, tableCornerY] = tableCorner
    [tableAreaX, tableAreaY] = tableArea

    # calculate card dimensions
    squareWidth = (tableAreaX - (SQUARE_SPACING * (n + 1))) // n
    squareHeight = (tableAreaY - (SQUARE_SPACING * (m + 1))) // m

    squares = {}
    rawSquares = []
    for i in range(n):
        for j in range(m):
            x = tableCornerX + (SQUARE_SPACING * (i + 1)) + (squareWidth * i)
            y = tableCornerY + (SQUARE_SPACING * (j + 1)) + (squareHeight * j)
            square = drawSquare(screen, x, y, squareWidth, squareHeight, board[i][j])
            squares[hashRect(square)] = [i, j]
            rawSquares.append(square)

    # return a matrix of card active boxes for collisions, with an associated board index
    return [squares, rawSquares, squareWidth, squareHeight]

# main render/draw method
def draw(screen, board, timeInSeconds):
    screen.fill((239, 180, 180))
    restOfArea = drawTopBar(screen, timeInSeconds)
    [tableCorner, tableArea] = drawTable(screen, restOfArea)
    [squares, rawSquares, squareWidth, squareHeight] = drawSquares(screen, 8, 8, tableCorner, tableArea, board)
    return [squares, rawSquares, squareWidth, squareHeight]

def handleFlipping(i, j, board, count):
    isBomb = False
    if board[i][j]["isFlagged"]:
        return [board, isBomb, count]
    board[i][j]["isFlipped"] = True
    if board[i][j]["isBomb"]:
        isBomb = True
    else:
        if board[i][j]["count"] == 0:
            for neighbor in getNeighbors(i, j, board):
                tempTempCount = count
                [x, y] = neighbor
                if not board[x][y]["isFlipped"]:
                    [board, isBombTemp, tempCount] = handleFlipping(x, y, board, tempTempCount)
                    count += (tempCount - tempTempCount)
    return [board, isBomb, count + 1]

def handleFlagging(i, j, board, flagCount):
    if board[i][j]["isFlagged"]:
        board[i][j]["isFlagged"] = False
        return [board, flagCount - 1]
    elif flagCount < 7:
        board[i][j]["isFlagged"] = True
        return [board, flagCount + 1]
    else:
        return [board, flagCount]

def handleClick(squares, rawSquares, board, squareWidth, squareHeight, squaresLeft, isFlagging, flagCount, mouseX, mouseY):
    for square in rawSquares:
        squareX = square.x
        squareY = square.y

        # first see if a card was selected
        if squareX <= mouseX and (squareX + squareWidth) >= mouseX and squareY <= mouseY and (squareY + squareWidth) >= mouseY:
            # finally check to see if that card is already flipped
            [i, j] = squares[hashRect(square)]
            if board[i][j]["isFlipped"] == False or isFlagging:
                if isFlagging:
                    [board, flagCount] = handleFlagging(i, j, board, flagCount)
                    isBomb = False
                    count = 0
                else:
                    [board, isBomb, count] = handleFlipping(i, j, board, 0)
                # can return early because can only click in one place at time
                return [board, isBomb, squaresLeft - count, flagCount, True]

        elif mouseX > 0 and mouseX < 210 and mouseY > 0 and mouseY < 70:
            return [None, None, None, None, None]


    return [board, False, squaresLeft, flagCount, False]

def playGame4():
    # initialize game state
    timeLeft = 300
    secondTimer = 30
    board = generateBoard()
    squaresLeft = 64
    isFlagging = False
    flagCount = 0
    gamestate = 2
    victory = 1
    loss = 0
    result = 2
    initialClick = True
    didClickSquare = False

    [squares, rawSquares, squareWidth, squareHeight] = draw(screen, board, timeLeft)

    pygame.mixer.Channel(0).play(pygame.mixer.Sound('./music/ms_theme.wav'))

    # begin main loop
    start = False # if false the start screen will be displayed
    active = False 
    while start == False: 
        screen.blit(mineStart, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                start = True
                active = True 
        while active:
            [squares, rawSquares, squareWidth, squareHeight] = draw(screen, board, timeLeft)
            gameOver = False
            # deal with input
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        [mouseX, mouseY] = pygame.mouse.get_pos()
                        [board, isBomb, squaresLeft, flagCount, didClickSquare] = handleClick(squares, rawSquares, board, squareWidth, squareHeight, squaresLeft, isFlagging, flagCount, mouseX, mouseY)
                        if board == None and isBomb == None and squaresLeft == None and flagCount == None:
                            pygame.mouse.set_cursor(*pygame.cursors.arrow)
                            pygame.mixer.pause()
                            return 2
                        if isBomb:
                            if not initialClick:
                                gameOver = True 
                                gamestate = loss
                            else:
                                while isBomb:
                                    board = generateBoard()
                                    [board, isBomb, squaresLeft, flagCount, didClickSquare] = handleClick(squares, rawSquares, board, squareWidth, squareHeight, squaresLeft, isFlagging, flagCount, mouseX, mouseY)
                                    initialClick = False
                        elif didClickSquare and initialClick:
                            initialClick = False


                        elif (squaresLeft - flagCount) == 0 or squaresLeft == 7:
                            gameOver = True

                        [squares, rawSquares, squareWidth, squareHeight] = draw(screen, board, timeLeft)

                if event.type == pygame.KEYDOWN:
                    if isFlagging:
                        isFlagging = False
                        pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    else:
                        isFlagging = True
                        pygame.mouse.set_cursor(*pygame.cursors.diamond)
                if event.type == pygame.QUIT:
                    sys.exit()

            # update time
            secondTimer -= 1
            if secondTimer <= 0:
                secondTimer = 30
                timeLeft -= 1
            
            # check run out of time
            if timeLeft <= 0:
                return 1
        
            gameClock.tick(30)

            if gameOver:
                if gamestate == loss:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    pygame.mixer.pause()
                    return 1
                

                if (squaresLeft - flagCount) == 0 or squaresLeft == 7:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    pygame.mixer.pause()
                    return 0
                    
                # screen.fill(WHITE)
                # textObject = afont.render(text, True, (0, 0, 0,))
                # screen.blit(textObject, (10 + (X_DIMENSION // 2), Y_DIMENSION // 2))
                # break
                # pygame.display.update()
                # for event in pygame.event.get():
                #     if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                #         sys.exit()

            pygame.display.update()