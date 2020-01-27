# import pygame as p
#have collision that forces convo with bruce
import sys as s
import random as r
import turtle as t
import pygame as pygame
from variables import*
from functions import*
from all_levels.level1.main import*
# from all_levels.level2.memory import*
from all_levels.level4.main import*
from all_levels.level5.starGame import*
# from start import startdisp

py.display.set_caption("Davis After Dark") 

while not gameover:
    grem = 3

    keys = py.key.get_pressed()
    screen.fill(brown)
    controls()


    if collision(playerpos, memX, memY, 64, 157):
        playercolor = (255,0,0)
        game1ready = True

        if game1ready:
            if keys[py.K_n]:
                playMatch()


    
    else:
        game1ready = False

    if collision(playerpos, 575, 575, 100, 100):
        playercolor = (255,0,0)    
        game2ready = True

        if game2ready:
            if keys[py.K_n]:
                playGame4()
                if result == 0:
                    print("loser!")

                if result == 1:
                    print("winner!")

                else:
                    result = 2
                    

    else:
        game2ready = False


    if collision(playerpos, 550, 100, 100, 60):
        playercolor = (255,0,0)    
        game3ready = True

        if game3ready:
            if keys[py.K_n]:
                gameLoop()
    
    else: 
        game3ready = False

    background = py.image.load("./assets/Enviroment.png").convert_alpha()
    brend = screen.blit(background,(0,0))
    centeroutline = py.draw.rect(screen, (0, 0, 0), ((375 -35.3553390593) - 2.5, (375 - 35.3553390593) - 2.5, 79.5,79.5))
    centerpiece = py.draw.rect(screen, (40, 176, 14), ((375 -35.3553390593), (375 - 35.3553390593), 75, 75))
    memoutline = py.draw.rect(screen, (15, 0, 0), (0 - 2.5, 500 - 2.5, 105, 75))
    # centerx = py.draw.rect(screen, (15, 0, 0), (0 , 375, 750, 2))
    # centery = py.draw.rect(screen, (15, 0, 0), (375, 0, 2, 750))
    g2o = py.draw.rect(screen, (15, 0, 0), (575 - 2.5, 575 - 2.5, 105, 105))
    g2c = py.draw.rect(screen, (15, 205, 155), (575, 575, 100, 100))
    mem = py.draw.rect(screen, (15, 255, 255), (memX, memY, memW, memH))
    mineoutline = py.draw.rect(screen, (0, 0, 0), (550-2.5, 100-2.5, 105, 65))
    mineped = py.draw.rect(screen, (15, 205, 155), (550, 100, 100, 60))
    # playeroutline = py.draw.rect(screen, (0, 0, 0),(playerpos[0] - 2.5, playerpos[1] - 2.5, psize + 5, psize + 5))
    playrobj = py.draw.rect(screen, playercolor, (playerpos[0], playerpos[1] - 20, 12, 24))
    # playrobj2 = py.draw.rect(screen, (0,0,0), (playerpos[0], playerpos[1], 1, 1))
    player = py.image.load("./assets/MainSpriteWalking1.png").convert_alpha()
    presize = py.transform.scale(player,(10,20))
    playerobj = screen.blit(presize,(playerpos[0] ,playerpos[1] - 20))
    playercolor = (re,g,b)
    py.display.update()
