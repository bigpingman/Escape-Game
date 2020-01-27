import pygame, random

"""
    A board is an N x M array of cards where each card exists exactly twice.
    The placement of the cards will be shuffled randomly.
"""
def generateBoard(n, m):
    # since we are generating n x m cards, we want (n x m) / 2 unique numbers
    # and thus should throw if the board dimensions do not allow this
    if (n * m) % 2 == 1:
        raise ValueError("Board dimension must require even number of cards.")

    # note: range is exclusive on the upper limit
    deck = list(range(1, 1 + (n * m) // 2)) + list(range(1, 1 + (n * m) // 2))
    random.shuffle(deck)

    board = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(deck[(i * m) + j])
        board.append(row)

    return board

"""
    Game States:
        1. Waiting for first card to be flipped
        2. Waiting for second card to be flipped
        3. figure out if the cards match and if they won
        4. Briefly displaying cards
        5. Game over - win
        6. Game over - time is up
"""
STATE_FIRST_DRAW = 1
STATE_SECOND_DRAW = 2
STATE_ANALYZE_DRAW = 3
STATE_DISPLAY_DELAY = 4
STATE_WIN = 5
STATE_LOSE = 6

DECK_OF_CARDS = [
    pygame.image.load("./all_levels/level1/assets/aceClubs.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/aceDiamonds.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/aceHearts.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/jackClubs.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/jackDiamonds.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/jackHearts.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/jackSpades.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/kingClubs.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/kingDiamonds.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/kingHearts.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/kingSpades.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/queenClubs.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/queenDiamonds.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/queenHearts.png").convert_alpha(), 
    pygame.image.load("./all_levels/level1/assets/queenSpades.png").convert_alpha(), 
]