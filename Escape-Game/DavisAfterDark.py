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
from all_levels.Matching.main import*
# from all_levels.level2.memory import*
from all_levels.Minesweeper.main import*
# from all_levels.Pattern.main import*
# from start import startdisp

from common import*

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
        self.screenAssets["Start Screen"] = py.image.load("./assets/startscreen1.png").convert_alpha()

        
        # player asset
        player = py.image.load("./assets/MainSpriteWalking1.png").convert_alpha()
        player = py.transform.scale(player,(10,20))
        self.screenAssets["player"] = player

        # ---------------------- GLOBALS ----------------------------- #
        """
           State
            0 - start
            1 - main hub
            2 - pattern
            3 - minesweeper
            4 - star game
            5 - matching
            6 - wrong way highway
            7 - Tutorial Screen 
            8 - Story 
            9 - Credits
            101 - End Screen Win
            102 - End Screen Lose
        """
        self.gamestate = 0
        self.game1ready = False
        self.game2ready = False
        self.game3ready = False
        self.gametype = 0
        
        self.gamesleft = 3
        self.clock = py.time.Clock()
        self.gameover = False

        #colors
        self.re = 140
        self.g = 200
        self.b = 17
        self.brown = (150,75,0)
        self.playercolor  = (self.re,self.g,self.b)
        
        #player pos
        self.playerX = 200
        self.playerY = 600
        self.playerpos = [self.playerX,self.playerY]
        
        self.psize = 50 #player size?

        # player dimensions
        self.ph = 157
        self.pw = 64
        
        #screen dimensions
        self.width = 720
        self.height = 720
        self.screen = py.display.set_mode((self.width,self.height))
        
        #memory game
        self.memX = 0
        self.memY = 500
        self.memH = 70
        self.memW = 100


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
        #top bar with 30 mins timer
        drawTopBar(screen, 1800)
        
        py.display.update()
    
    #Draws the start screen 
    def drawStartScreen(self): 
        self.screen.blit(self.screenAssets["Start Screen"], (0, 0))
        py.display.update()

    def drawWinScreen(self):
        # code here
        return

    def drawLoseScreen(self):
        # code here
        return

    def playPatternGame(self):
        # code here
        return

    def playStarGame(self):
        # code here
        return
        
    def playMinesweeperGame(self):
        # code here
        return

    def playMatchingGame(self):
        #code here
        return
    
    def playHighwayGame(self):
        #code here
        return

    def drawTutorial(self): 
        
        return 

    def start(self):
        while True:

            #GAME LOOP -- GAME NOT OVER
            while self.gamestate < 100:
                
                # STATE 0 : START
                if self.gamestate == 0:
                    self.drawStartScreen()
                    for event in py.event.get():
                        if event.type == py.QUIT:
                            sys.exit()
                        elif event.type == py.KEYDOWN:
                            if event.key == py.K_RETURN:
                                self.gamestate = 1 
                            elif event.key == py.K_t: 
                                self.gamestate = 7
                            elif event.key == py.K_s: 
                                self.gamestate = 8
                            elif event.key == py.K_c: 
                                self.gamestate = 9 

                # STATE 1 : MAIN HUB
                if self.gamestate == 1:
                    self.drawBackground(self.playerpos)
                    self.controls()
                    keys = py.key.get_pressed()

                    # step on matching game
                    if self.collision(self.playerpos, self.memX, self.memY, 64, 157):
                        self.playercolor = (255,0,0)
                        if keys[py.K_n]:
                            self.gamestate = 5

                    # step on minesweeper
                    elif self.collision(self.playerpos, 575, 575, 100, 100):
                        self.playercolor = (255,0,0)
                        if keys[py.K_n]:
                            self.gamestate = 3

                    # step on pattern game
                    elif self.collision(self.playerpos, 550, 100, 100, 60):
                        self.playercolor = (255,0,0)
                        if keys[py.K_n]:
                            self.gamestate = 2

                    # otherwise no stepping on anything
                    else:
                        self.playercolor = (0,255,0)

                # STATE 2 : PATTERN
                if self.gamestate == 2:
                    self.playPatternGame()

                # STATE 3 : MINESWEEPER
                if self.gamestate == 3:
                    self.playMinesweeperGame()
                    
                # STATE 4 : STAR GAME
                if self.gamestate == 4:
                    self.playStarGame()

                # STATE 5 : MATCHING
                if self.gamestate == 5:
                    self.playMatchingGame()
                    
                # STATE 6 : HIGHWAY
                if self.gamestate == 6:
                    self.playHighwayGame()
                
                if self.gamestate == 7:
                    self.playHighwayGame()
            
            #GAME OVER LOOP -- END SCREENS
            while self.gamestate > 100:
                
                # STATE 101 : END SCREEN WIN
                if self.gamestate == 101:
                    self.drawWinScreen()

                # STATE 102 : END SCREEN LOSE
                if self.gamestate == 102:
                    self.drawLoseScreen()
        

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
            x -= 1

        if keys[py.K_d]:
            # py.mixer.music.play(1)
            x += 1

        if keys[py.K_s]:
            # py.mixer.music.play(1)
            y += 1

        if keys[py.K_w]:
            # py.mixer.music.play(1)
            y -= 1

        if keys[py.K_p]:
            s.exit()
        self.playerpos[0] = x
        self.playerpos[1] = y

        # collision data

        if 0 > self.playerpos[0] + 2:
            self.playerpos[0] = 2

        if self.playerpos[0] > self.width - 10:
            self.playerpos[0] = self.width - 10

        if self.playerpos[1] > self.height - 10:
            self.playerpos[1] = self.height - 10

        if self.playerpos[1] < 0 + 20:
            self.playerpos[1] = 20

    def collision(self, playerpos, oX, oY, oW, oH):
        pX = playerpos[0]
        pY = playerpos[1]
        eX = oX
        eY = oY

        if (pX + 10) > eX >= pX or (eX + oW) > pX >= eX:
            if (pY + 20) > eY >= pY or (eY + oH) > pY >= eY:
                return True
            return False