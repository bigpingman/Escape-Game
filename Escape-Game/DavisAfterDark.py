"""
    Davis After Dark
    main.py is the main entry ppint into the game
"""
# import pygame as p
#have collision that forces convo with bruce
import sys as s
import random as r
import turtle as t
import pygame as pygame
from all_levels.level1.main import*
# from all_levels.level2.memory import*
from all_levels.level4.main import*
from all_levels.level5.starGame import*
# from start import startdisp

import pygame as py
import random as r


# DavisAfterDark is the main game state object
# oh hail the God object pattern (DONT ever do this in production)
# read more:
# https://en.wikipedia.org/wiki/God_object
class DavisAfterDark:
    def __init__(self):
        # ---------------------- PYGAME STUFF ----------------------------- #
        py.init()
        py.display.set_caption("Davis After Dark") 

        # ---------------------- ASSETS ----------------------------- #
        self.screenAssets = {}
        
        # background asset
        self.screenAssets["background"] = py.image.load("./assets/Enviroment.png").convert_alpha()
        
        # player asset
        player = py.image.load("./assets/MainSpriteWalking1.png").convert_alpha()
        player = py.transform.scale(player,(10,20))
        self.screenAssets["player"] = player

        # ---------------------- GLOBALS ----------------------------- #
        self.gamestate = 1
        self.game1ready = False
        self.game2ready = False
        self.game3ready = False
        self.gametype = 0
        self.re = 140
        self.psize = 50
        self.g = 200
        self.gamesleft = 3
        self.clock = py.time.Clock()
        self.b = 17
        self.playercolor  = (self.re,self.g,self.b)
        self.playerX = 200
        self.playerY = 600
        self.memH = 70
        self.memW = 100
        self.playerpos = [self.playerX,self.playerY]
        self.width = 720
        self.height = 720
        self.screen = py.display.set_mode((self.width,self.height))
        self.gameover = False
        self.brown = (150,75,0)
        self.memX = 0
        self. memY = 500
        # player dimensions
        self.ph = 157
        self.pw = 64



    def drawBackground(self, playerpos):
        # background
        self.screen.blit(self.screenAssets["background"], (0, 0))
        # centeroutline
        py.draw.rect(self.screen, (0, 0, 0), ((375 -35.3553390593) - 2.5, (375 - 35.3553390593) - 2.5, 79.5,79.5))
        # centerpiece
        py.draw.rect(self.screen, (40, 176, 14), ((375 -35.3553390593), (375 - 35.3553390593), 75, 75))
        # memoutline
        py.draw.rect(self.screen, (15, 0, 0), (0 - 2.5, 500 - 2.5, 105, 75))
        # g2o
        py.draw.rect(self.screen, (15, 0, 0), (575 - 2.5, 575 - 2.5, 105, 105))
        # g2c
        py.draw.rect(self.screen, (15, 205, 155), (575, 575, 100, 100))
        # mem
        py.draw.rect(self.screen, (15, 255, 255), (self.memX, self.memY, self.memW, self.memH))
        # mineoutline
        py.draw.rect(self.screen, (0, 0, 0), (550-2.5, 100-2.5, 105, 65))
        # mineped
        py.draw.rect(self.screen, (15, 205, 155), (550, 100, 100, 60))
        # playrobj
        py.draw.rect(self.screen, self.playercolor, (playerpos[0], playerpos[1] - 20, 12, 24))
        # player
        self.screen.blit(self.screenAssets["player"], (playerpos[0] ,playerpos[1] - 20))
        
        py.display.update()

    def start(self):
        while not self.gameover:
            self.drawBackground(self.playerpos)
            grem = 3

            keys = py.key.get_pressed()
            self.screen.fill(self.brown)
            self.controls()


            if self.collision(self.playerpos, self.memX, self.memY, 64, 157):
                self.playercolor = (255,0,0)
                self.game1ready = True

                if self.game1ready:
                    if keys[py.K_n]:
                        playMatch()


            
            else:
                self.game1ready = False

            if self.collision(self.playerpos, 575, 575, 100, 100):
                self.playercolor = (255,0,0)    
                self.game2ready = True

                if self.game2ready:
                    if keys[py.K_n]:
                        playGame4()
                        if self.result == 0:
                            print("loser!")

                        if self.result == 1:
                            print("winner!")

                        else:
                            self.result = 2
                            

            else:
                self.game2ready = False


            if self.collision(self.playerpos, 550, 100, 100, 60):
                playercolor = (255,0,0)    
                self.game3ready = True

                if self.game3ready:
                    if keys[py.K_n]:
                        gameLoop()
            
            else: 
                self.game3ready = False

            
            


    def controls(self):
        # py.mixer.music.load("./music/Step.wav")
        keys = py.key.get_pressed()
        for event in py.event.get():
            if event.type == py.QUIT:
                s.exit()

        x = self.playerpos[0]
        y = self.playerpos[1]
        if keys[py.K_a]:
            # py.mixer.music.play(1)
            x -= 10

        if keys[py.K_d]:
            # py.mixer.music.play(1)
            x += 10

        if keys[py.K_s]:
            # py.mixer.music.play(1)
            y += 10

        if keys[py.K_w]:
            # py.mixer.music.play(1)
            y -= 10

        if keys[py.K_p]:
            s.exit()
        self.playerpos[0] = x
        self.playerpos[1] = y

        # collision data

        if 0 > self.playerpos[0]:
            self.playerpos[0] = 2

        if self.playerpos[0] > self.width - 50:
            self.playerpos[0] = self.width - 52

        if self.playerpos[1] > self.height - 50:
            self.playerpos[1] = self.height - 52

        if self.playerpos[1] < 0:
            self.playerpos[1] = 2

    def collision(self, playerpos, oX, oY, oW, oH):
        pX = playerpos[0]
        pY = playerpos[1]
        eX = oX
        eY = oY

        if (pX + 10) > eX >= pX or (eX + oW) > pX >= eX:
            if (pY + 20) > eY >= pY or (eY + oH) > pY >= eY:
                return True
            return False