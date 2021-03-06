import pygame, sys
from all_levels.Minesweeper.constant import X_DIMENSION, Y_DIMENSION, TOPBAR_RATIO, CLOCK_BORDER, CLOCK_SPACING, WHITE, BLACK

def initScreenAndGameClock():
    # initialize pygame
    pygame.init()

    # initialize the fonts
    try:
        pygame.font.init()
    except:
        sys.exit()

    # create a game clock
    gameClock = pygame.time.Clock()

    # create a screen
    screen = pygame.display.set_mode((X_DIMENSION, Y_DIMENSION))

    return [screen, gameClock]

def timeToString(timeInSeconds):
    if timeInSeconds < 0:
        timeInSeconds = 0
    timeInSeconds = int(timeInSeconds)
    seconds = timeInSeconds % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
    minutes = str(timeInSeconds // 60)
    return minutes + ":" + seconds

def drawClock(screen, timeInSeconds):
    width = (X_DIMENSION // CLOCK_SPACING) - (CLOCK_BORDER * 2)
    height = (Y_DIMENSION // TOPBAR_RATIO) - (CLOCK_BORDER * 2)

    x = X_DIMENSION - width - CLOCK_BORDER
    y = 0 + CLOCK_BORDER

    # background
    pygame.draw.rect(screen, (255,255,255), pygame.Rect((x , y), (width, height)))

    # numbers
    afont = pygame.font.SysFont("Helvetica", 60, bold=False)
    textObject = afont.render(timeToString(timeInSeconds), True, BLACK)
    screen.blit(textObject, (x + 50, 2 * y - 10))

def drawKeysLeft(screen, numKeysLeft):
    width = (X_DIMENSION // CLOCK_SPACING) - (CLOCK_BORDER * 2)
    height = (Y_DIMENSION // TOPBAR_RATIO) - (CLOCK_BORDER * 2)

    x = CLOCK_BORDER + width
    y = 0 + CLOCK_BORDER

    afont = pygame.font.SysFont("Helvetica", 30, bold=False)
    textObject = afont.render("Keys to collect: " + str(numKeysLeft), True, (0,0,0))
    screen.blit(textObject, (x + 25, 2 * y + 10))

def drawBackButton(screen):
    width = (X_DIMENSION // CLOCK_SPACING) - (CLOCK_BORDER * 2)
    height = (Y_DIMENSION // TOPBAR_RATIO) - (CLOCK_BORDER * 2)

    x = CLOCK_BORDER
    y = 0 + CLOCK_BORDER

    # background
    pygame.draw.rect(screen, (125, 0, 255), pygame.Rect((x , y), (width, height)))

    # font for back
    afont = pygame.font.SysFont("Helvetica", 60, bold=False)
    textObject = afont.render("back", True, (255,255,255))
    screen.blit(textObject, (x + 25, 2 * y - 10))

def drawTopBar(screen, timeInSeconds, includeClock=True, includeBackButton=True, includeKeysLeft=False, keys=5):
    pygame.draw.rect(screen, (0, 204, 204), pygame.Rect(
        (0, 0), (X_DIMENSION, Y_DIMENSION / TOPBAR_RATIO)))

    if includeBackButton:
        drawBackButton(screen)

    if includeClock:
        drawClock(screen, timeInSeconds)

    if includeKeysLeft:
        drawKeysLeft(screen, keys)

    # size of the rest of the screen below the topbar
    return [X_DIMENSION, Y_DIMENSION - (Y_DIMENSION / TOPBAR_RATIO)]

def hashRect(rect):
    return hash(str(rect.x) + "|" + str(rect.y))