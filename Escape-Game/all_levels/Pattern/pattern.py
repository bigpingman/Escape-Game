import pygame
import random
import time
from common import initScreenAndGameClock, drawTopBar

''' 
Pattern game with a n x m grid in which the player must recreate a pattern in
the squares that is shown briefly to them at the beginning then disappears
'''

SCREEN_X = 720
SCREEN_Y = 720

topLX = 100
topLY = 100
bottomRX = 620
bottomRY = 620
sqLen = (bottomRX - topLX) / 4 #divided by 4 for level 1 with the 4x4 grid
numTrue = 4 #for level 1


#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

#background
sky = pygame.image.load("sky.png")
screen.blit(sky, (0,0))

#Initializes the grid with x number of TRUE squares assigned to random positions
def createGrid(n, m, x):  # (rows, cols, number of TRUE squares)
    grid = []
    totalSq = n * m

    counter = 0
    # loops through grid and randomly assigns x number of TRUE squares
    for j in range(n):
        row = []
        for i in range(m):
            tOrF = random.random()
            y = x
            h = (1.0 * y) / (n * m)

            # percentage chance of the square being TRUE using the ratio of x to the total num of squares
            if tOrF < h and x > 0:  # if ratio is true and there are still more TRUE squares to be assigned
                row.append(True)
                x -= 1
                counter += 1

            elif tOrF >= h and x > 0:  # if ratio is false and there are still more TRUE squares to be assigned
                if totalSq - counter <= x:  # if number of sq remaining is <= number of TRUE squares to be assigned
                    row.append(True)
                    x -= 1
                else:
                    row.append(False)
                counter += 1
            else:  # if false and all TRUE squares have been assigned
                row.append(False)
                counter += 1

        grid.append(row)

    return grid


#Player picks a square to recreate the pattern
def pickSquare():
    
    picked = False
    while picked == False:
        mouseX, mouseY = pygame.mouse.get_pos()
        event = pygame.event.wait()
    
        #col 0
        for i in range(4):
            if mouseX > topLX and mouseX < topLX + sqLen and mouseY > topLY + sqLen*i and mouseY < topLY + sqLen*(i+1): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    picked = True
                    return [0,i]
    
        #col 1            
        for i in range(4):
            if mouseX > topLX + sqLen and mouseX < topLX + sqLen*2 and mouseY > topLY + sqLen*i and mouseY < topLY + sqLen*(i+1): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    picked = True
                    return [1,i]
    
        #col 2
        for i in range(4):
            if mouseX > topLX + sqLen*2 and mouseX < topLX + sqLen*3 and mouseY > topLY + sqLen*i and mouseY < topLY + sqLen*(i+1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    picked = True
                    return [2,i]
    
        #col 3
        for i in range(4):
            if mouseX > topLX + sqLen*3 and mouseX < topLX + sqLen*4 and mouseY > topLY + sqLen*i and mouseY < topLY + sqLen*(i+1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    picked = True
                    return [3,i]

#Grid display in terminal for debugging
def displayGrid(grid):
    for row in grid:
        string = ""
        for square in row:
            if square == False:
                string += " O "
            else:
                string += " X "
        print(string)

#draws grid onto screen
def drawGrid(screen):
    
    # outline of grid
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY), (bottomRX-topLX, bottomRY-topLY)), 3) 

    #sq00
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY), (sqLen, sqLen)), 2)
    #sq01
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY + sqLen), (sqLen, sqLen)), 2)
    #sq02
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY + 2*sqLen), (sqLen, sqLen)), 2)
    #sq03
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY + 3*sqLen), (sqLen, sqLen)), 2)
    
    #sq10
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + sqLen, topLY), (sqLen, sqLen)), 2)
    #sq11
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + sqLen, topLY + sqLen), (sqLen, sqLen)), 2)
    #sq12
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + sqLen, topLY + 2*sqLen), (sqLen, sqLen)), 2)
    #sq13
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + sqLen, topLY + 3*sqLen), (sqLen, sqLen)), 2)

    #sq20
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 2*sqLen, topLY), (sqLen, sqLen)), 2)
    #sq21
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 2*sqLen, topLY + sqLen), (sqLen, sqLen)), 2)
    #sq22
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 2*sqLen, topLY + 2*sqLen), (sqLen, sqLen)), 2)
    #sq23
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 2*sqLen, topLY + 3*sqLen), (sqLen, sqLen)), 2)

    #sq30
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 3*sqLen, topLY), (sqLen, sqLen)), 2)
    #sq31
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 3*sqLen, topLY + sqLen), (sqLen, sqLen)), 2)
    #sq32
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 3*sqLen, topLY + 2*sqLen), (sqLen, sqLen)), 2)
    #sq33
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 3*sqLen, topLY + 3*sqLen), (sqLen, sqLen)), 2)

def drawPattern(screen, grid):
    
    # list of TRUE squares
    trueSquares = []
    n = 0
    m = 0
    for row in grid:  # loops through rows
        m = 0
        for col in row:  # loops through cols
            if col == True:  # if square is TRUE
                trueSquares.append([m, n])
            m += 1
        n += 1
    
    for i in trueSquares:
        if i == [0, 0]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX, topLY), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY), (sqLen, sqLen)), 2)
        elif i == [0, 1]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX, topLY + sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY + sqLen), (sqLen, sqLen)), 2)
        elif i == [0, 2]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX, topLY + 2*sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY + 2*sqLen), (sqLen, sqLen)), 2)
        elif i == [0, 3]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX, topLY + 3*sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX, topLY + 3*sqLen), (sqLen, sqLen)), 2)
        elif i == [1, 0]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + sqLen, topLY), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + sqLen, topLY), (sqLen, sqLen)), 2)
        elif i == [1, 1]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + sqLen, topLY + sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + sqLen, topLY + sqLen), (sqLen, sqLen)), 2)
        elif i == [1, 2]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + sqLen, topLY + 2*sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + sqLen, topLY + 2*sqLen), (sqLen, sqLen)), 2)
        elif i == [1, 3]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + sqLen, topLY + 3*sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + sqLen, topLY + 3*sqLen), (sqLen, sqLen)), 2)
        elif i == [2, 0]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + 2*sqLen, topLY), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 2*sqLen, topLY), (sqLen, sqLen)), 2)
        elif i == [2, 1]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + 2*sqLen, topLY + sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 2*sqLen, topLY + sqLen), (sqLen, sqLen)), 2)
        elif i == [2, 2]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + 2*sqLen, topLY + 2*sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 2*sqLen, topLY + 2*sqLen), (sqLen, sqLen)), 2)
        elif i == [2, 3]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + 2*sqLen, topLY + 3*sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 2*sqLen, topLY + 3*sqLen), (sqLen, sqLen)), 2)
        elif i == [3, 0]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + 3*sqLen, topLY), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 3*sqLen, topLY), (sqLen, sqLen)), 2)
        elif i == [3, 1]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + 3*sqLen, topLY + sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 3*sqLen, topLY + sqLen), (sqLen, sqLen)), 2)
        elif i == [3, 2]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + 3*sqLen, topLY + 2*sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 3*sqLen, topLY + 2*sqLen), (sqLen, sqLen)), 2)
        elif i == [3, 3]:
            pygame.draw.rect(screen, (255, 255, 51), pygame.Rect((topLX + 3*sqLen, topLY + 3*sqLen), (sqLen, sqLen)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((topLX + 3*sqLen, topLY + 3*sqLen), (sqLen, sqLen)), 2)

#plays game
def playGame(screen, grid, numTrue):

    while True:
    
        # player picks numTrue number of squares
        squaresPicked = []
        for i in range(numTrue):
            ps = pickSquare()
            psX = int(ps[0])
            psY = int(ps[1])
            squaresPicked.append([psX, psY])
    
        # list of TRUE squares
        trueSquares = []
        n = 0
        m = 0
        for row in grid:  # loops through rows
            m = 0
            for col in row:  # loops through cols
                if col == True:  # if square is TRUE
                    trueSquares.append([m, n])
                m += 1
            n += 1
    
        # loops through all the true pairs of coordinates and checks against each square picked
        counterCorrect = 0
        for sqP in squaresPicked:
            for sqT in trueSquares: 
                if sqP == sqT:
                    counterCorrect += 1

        if counterCorrect == numTrue:
            return True
        else:
            return False
    

def level1():
    
    grid = createGrid(4, 4, 4)
    state = 0    
    gameOver = False
    failsCounter = 0
    won = False
    loseT = False

    while True:
        drawTopBar(screen, 0)
        pygame.display.update()

        #shows pattern
        t1 = pygame.time.get_ticks()
        drawGrid(screen)
        drawPattern(screen, grid)
        pygame.display.update()
        
        while pygame.time.get_ticks() < (t1+1000):
            for event in pygame.event.get(20):
                if event.type == pygame.QUIT:
                    exit()
        
        #returns to blank grid
        screen.blit(sky, (0,0))
        drawTopBar(screen,0)
        drawGrid(screen)  
        pygame.display.update()
        
        #outcome texts
        textFont = pygame.font.SysFont("Arial", 70, True)
        pickFont = pygame.font.SysFont("Arial", 35, True)
        winText = textFont.render('You win!', False, (255, 255, 51))
        loseText = textFont.render('You lose!', False, (255, 255, 51))
        retryText = textFont.render('Try Again!', False, (255, 255, 51))
        
        pickText = pickFont.render('Pick 4 squares to recreate the pattern', False, (0, 0, 0))

        if gameOver == False:
            screen.blit(pickText, (105, 615))
            pygame.display.update()
            
            while failsCounter < 3 and won == False: #plays until a win or three losses
                outcome = playGame(screen, grid, 4)
                
                if outcome == False: #lose
                    failsCounter+=1
                    
                    if failsCounter < 3: #retry
                        tFail = pygame.time.get_ticks()
                        screen.blit(retryText, (200, 640))
                        
                        #displays pattern again briefly
                        drawPattern(screen, grid)
                        pygame.display.update()
                        
                        while pygame.time.get_ticks() < (tFail+1000):
                            for event in pygame.event.get(20):
                                if event.type == pygame.QUIT:
                                    exit()
                        
                        #redraws blank grid
                        screen.blit(sky, (0,0))
                        drawTopBar(screen,0)
                        drawGrid(screen)  
                        pygame.display.update()
                        
                        #pick 4 
                        screen.blit(pickText, (105, 615))
                        pygame.display.update()
                        
                    else: #no more retries
                        screen.blit(sky, (0,0))
                        screen.blit(loseText, (200, 640))
                        drawPattern(screen, grid)
                        pygame.display.update()
                
                else: #win
                    won = True
                    screen.blit(sky, (0,0))
                    screen.blit(winText, (200, 640))
                    pygame.display.update()
            
            gameOver = True

def level2():
    
    grid = createGrid(4, 4, 6)
    state = 0    
    gameOver = False
    failsCounter = 0
    won = False
    loseT = False

    while True:
        drawTopBar(screen, 0)
        pygame.display.update()

        #shows pattern
        t1 = pygame.time.get_ticks()
        drawGrid(screen)
        drawPattern(screen, grid)
        pygame.display.update()
        
        while pygame.time.get_ticks() < (t1+800):
            for event in pygame.event.get(20):
                if event.type == pygame.QUIT:
                    exit()
        
        #returns to blank grid
        screen.blit(sky, (0,0))
        drawTopBar(screen,0)
        drawGrid(screen)  
        pygame.display.update()
        
        #outcome texts
        textFont = pygame.font.SysFont("Arial", 70, True)
        pickFont = pygame.font.SysFont("Arial", 35, True)
        winText = textFont.render('You win!', False, (255, 255, 51))
        loseText = textFont.render('You lose!', False, (255, 255, 51))
        retryText = textFont.render('Try Again!', False, (255, 255, 51))
        
        pickText = pickFont.render('Pick 6 squares to recreate the pattern', False, (0, 0, 0))

        if gameOver == False:
            screen.blit(pickText, (105, 615))
            pygame.display.update()
            
            while failsCounter < 3 and won == False: #plays until a win or three losses
                outcome = playGame(screen, grid, 6)
                
                if outcome == False: #lose
                    failsCounter+=1
                    
                    if failsCounter < 3: #retry
                        tFail = pygame.time.get_ticks()
                        screen.blit(retryText, (200, 640))
                        
                        #displays pattern again briefly
                        drawPattern(screen, grid)
                        pygame.display.update()
                        
                        while pygame.time.get_ticks() < (tFail+800):
                            for event in pygame.event.get(20):
                                if event.type == pygame.QUIT:
                                    exit()
                        
                        #redraws blank grid
                        screen.blit(sky, (0,0))
                        drawTopBar(screen,0)
                        drawGrid(screen)  
                        pygame.display.update()
                        
                        #pick 4 
                        screen.blit(pickText, (105, 615))
                        pygame.display.update()
                        
                    else: #no more retries
                        screen.blit(sky, (0,0))
                        screen.blit(loseText, (200, 640))
                        drawPattern(screen, grid)
                        pygame.display.update()
                
                else: #win
                    won = True
                    screen.blit(sky, (0,0))
                    screen.blit(winText, (200, 640))
                    pygame.display.update()
            
            gameOver = True

level1() #add conditional to determine whether to call level 1 or 2!!!!!!