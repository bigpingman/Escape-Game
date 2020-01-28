import pygame, sys
from all_levels.Matching.common import initScreenAndGameClock, drawTopBar
from all_levels.Matching.constant import X_DIMENSION, Y_DIMENSION, BOARD_M, BOARD_N, TOPBAR_RATIO, CARD_SPACING, WHITE
# import Room as r

# initialize basic elements
[screen, gameClock] = initScreenAndGameClock()
afont = pygame.font.SysFont("Helvetica", 30, bold=False)
from all_levels.Matching.match import generateBoard, STATE_FIRST_DRAW, STATE_SECOND_DRAW, STATE_ANALYZE_DRAW, STATE_DISPLAY_DELAY, STATE_WIN, STATE_LOSE, DECK_OF_CARDS

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

def drawCard(screen, x, y, width, height, number):
    if number > 0:
        text = ""
        textObject = afont.render(text, True, (0, 0, 0,))
        card = pygame.draw.rect(screen, (50, 144, 177),
                                pygame.Rect((x, y), (width, height)))
        screen.blit(textObject, (x - 10 + width // 2, y + height // 3))
    else:
        text = str(number * -1)
        textObject = afont.render(text, True, (0, 0, 0,))
        card = pygame.draw.rect(screen, (100, 144, 100),
                                pygame.Rect((x, y), (width, height)))
        screen.blit(textObject, (x - 10 + width // 2, y + height // 3))

        screen.blit(DECK_OF_CARDS[(number * -1) -1], (x + (width // 8), y))
    return card

def hashRect(rect):
    return hash(str(rect.x) + "|" + str(rect.y))

def drawCards(screen, n, m, tableCorner, tableArea, board):
    [tableCornerX, tableCornerY] = tableCorner
    [tableAreaX, tableAreaY] = tableArea

    # calculate card dimensions
    cardWidth = (tableAreaX - (CARD_SPACING * (n + 1))) // n
    cardHeight = (tableAreaY - (CARD_SPACING * (m + 1))) // m

    cards = {}
    rawCards = []
    for i in range(n):
        for j in range(m):
            x = tableCornerX + (CARD_SPACING * (i + 1)) + (cardWidth * i)
            y = tableCornerY + (CARD_SPACING * (j + 1)) + (cardHeight * j)
            card = drawCard(screen, x, y, cardWidth, cardHeight, board[i][j])
            cards[hashRect(card)] = [i, j]
            rawCards.append(card)

    # return a matrix of card active boxes for collisions, with an associated board index
    return [cards, rawCards, cardWidth, cardHeight]

def draw(screen, board, timeInSeconds):
    screen.fill((239, 180, 180))
    restOfArea = drawTopBar(screen, timeInSeconds)
    [tableCorner, tableArea] = drawTable(screen, restOfArea)
    [cards, rawCards, cardWidth, cardHeight] = drawCards(
        screen, 4, 4, tableCorner, tableArea, board)
    pygame.display.update()
    return [cards, rawCards, cardWidth, cardHeight]

def handleClick(cards, rawCards, board, cardWidth, cardHeight, currentlySelected=None):
    for card in rawCards:
        [mouseX, mouseY] = pygame.mouse.get_pos()
        cardX = card.x
        cardY = card.y

        # first see if a card was selected
        if cardX <= mouseX and (cardX + cardWidth) >= mouseX and cardY <= mouseY and (cardY + cardWidth) >= mouseY:
            # then check if that card was the card already selected
            if (currentlySelected != None and currentlySelected != card) or currentlySelected == None:
                # finally check to see if that card is already flipped
                [i, j] = cards[hashRect(card)]
                if board[i][j] > 0:
                    board[i][j] *= -1
                    # can return early because can only click in one place at time
                    return [board, card]

    return [board, None]

def playMatch():
    # keep track of the shit to refresh
    refresh = []
    keys = pygame.key.get_pressed()

    # initialize game state
    board = generateBoard(BOARD_N, BOARD_M)
    timeLeft = 60
    secondTimer = 30
    [cards, rawCards, cardWidth, cardHeight] = draw(screen, board, timeLeft)
    state = STATE_FIRST_DRAW  # start in the initial state
    currentlySelectedCard1 = None
    currentlySelectedCard2 = None
    delayTicker = 0
    flipCount = 0

    # begin main loop
    while True:


        if state == STATE_FIRST_DRAW:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    [board, card] = handleClick(
                        cards, rawCards, board, cardWidth, cardHeight)
                    # it is possible they don't actually click on a card or a valid card
                    if card == None:
                        continue
                    else:
                        currentlySelectedCard1 = card
                        [cards, rawCards, cardWidth,
                            cardHeight] = draw(screen, board, timeLeft)
                        state = STATE_SECOND_DRAW
                if event.type == pygame.KEYDOWN:
                            
                    if keys[pygame.K_4]:
                        print("working")
                        break
                
                if event.type == pygame.QUIT:
                  break

        elif state == STATE_SECOND_DRAW:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    [board, card] = handleClick(
                        cards, rawCards, board, cardWidth, cardHeight, currentlySelectedCard1)
                    # it is possible they don't actually click on a card or a valid card
                    if card == None:
                        continue
                    else:
                        currentlySelectedCard2 = card
                        [cards, rawCards, cardWidth,
                            cardHeight] = draw(screen, board, timeLeft)
                        state = STATE_ANALYZE_DRAW
                if event.type == pygame.QUIT:
                    sys.exit()

        elif state == STATE_ANALYZE_DRAW:
            [i1, j1] = cards[hashRect(currentlySelectedCard1)]
            [i2, j2] = cards[hashRect(currentlySelectedCard2)]

            if board[i1][j1] == board[i2][j2]:
                flipCount += 2
                if flipCount == BOARD_N * BOARD_M:
                    state = STATE_WIN
                else:
                    state = STATE_FIRST_DRAW
            else:
                state = STATE_DISPLAY_DELAY
            
        elif state == STATE_DISPLAY_DELAY:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            delayTicker += 1
            if delayTicker == 30:
                delayTicker = 0
                # flip them back over
                board[i1][j1] *= -1
                board[i2][j2] *= -1
                state = STATE_FIRST_DRAW
            
            [cards, rawCards, cardWidth, cardHeight] = draw(screen, board, timeLeft)

        elif state == STATE_WIN:
            if delayTicker == 0:
                screen.fill(WHITE)
                restOfArea = drawTopBar(screen, timeLeft)
                textObject = afont.render("Winner!", True, (0, 0, 0,))
                screen.blit(
                    textObject, ((X_DIMENSION // 2), Y_DIMENSION // 2))

                break
                pygame.display.update()

            delayTicker += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if delayTicker == 30:
                r.game1ready = False

        elif state == STATE_LOSE:
            if delayTicker == 0:
                screen.fill(WHITE)
                textObject = afont.render("You Lose - time is up!", True, (0, 0, 0,))
                screen.blit(
                    textObject, (10 + (X_DIMENSION // 2), Y_DIMENSION // 2))

                break
                pygame.display.update()

            delayTicker += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if delayTicker == 30:
                sys.exit()

        if state != 5 and state != 6:
            # update time
            secondTimer -= 1
            if secondTimer <= 0:
                secondTimer = 30
                timeLeft -= 1
                if timeLeft == 0:
                    state = STATE_LOSE
            
            [cards, rawCards, cardWidth, cardHeight] = draw(screen, board, timeLeft)

        pygame.display.update(refresh)
        refresh = []
        gameClock.tick(30)
