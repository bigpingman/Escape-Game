"""
    Davis After Dark
    main.py is the main entry ppint into the game
"""
# import pygame as p
#have collision that forces convo with bruce
import sys as s
import random as r
import turtle as t
# from all_levels.level2.memory import*
from all_levels.Stargame.starGame import starGameMain
from all_levels.Minesweeper.main import playGame4
from pattern import level1Pattern
from all_levels.Highway.wrongWayHighway import highwayMain
from all_levels.Matching.main import playMatch
from common import*
import pygame as py
import random as r

# some constants (plz move)
WON_GAME = 0
LOST_GAME = 1
EXITED_GAME = 2
SECOND = 1
MINUTE = 60 * SECOND
TICKS_PER_SECOND = 60

# DavisAfterDark is the main game state object
# oh hail the God object pattern (DONT ever do this in production)
# read more:
# https://en.wikipedia.org/wiki/God_object
class DavisAfterDark:
    def __init__(self):
        # ---------------------- PYGAME STUFF ----------------------------- #
        py.init()
        pygame.mixer.init()
        py.display.set_caption("Davis After Dark") 

        # ---------------------- ASSETS ----------------------------- #
        self.screenAssets = {}
        
        # background asset
        self.screenAssets["background"] = py.image.load("./assets/Enviroment.png").convert_alpha()

        #Start Screen and others
        self.screenAssets["Start Screen"] = py.image.load("./assets/startscreen1.png").convert_alpha()
        self.screenAssets["Tutorial Screen"] = py.image.load("./assets/Tutorialslide.png").convert_alpha()
        self.screenAssets["Win Screen"] = py.image.load("./assets/End1.png").convert_alpha()
        self.screenAssets["Lose Screen"] = py.image.load("./assets/End2.png").convert_alpha()
        self.screenAssets["Credits Screen"] = py.image.load("./assets/credits.png").convert_alpha()

        #Story Images 
        self.screenAssets["Story Screen 1"] = py.image.load("./assets/Story1.png").convert_alpha()
        self.screenAssets["Story Screen 2"] = py.image.load("./assets/Story2.png").convert_alpha()
        self.screenAssets["Story Screen 3"] = py.image.load("./assets/Story2pt5.png").convert_alpha()
        self.screenAssets["Story Screen 4"] = py.image.load("./assets/Story3.png").convert_alpha()

        bigImg1 = py.image.load("./assets/Story4.png").convert_alpha()
        bigImg1 = py.transform.scale(bigImg1, (770, 770))
        self.screenAssets["Story Screen 5"] = bigImg1

        bigImg2 = py.image.load("./assets/Story5.png").convert_alpha()
        bigImg2 = py.transform.scale(bigImg2, (770, 770))
        self.screenAssets["Story Screen 6"] = bigImg2

        # player asset
        player = py.image.load("./assets/MainSpriteWalking1.png").convert_alpha()
        player = py.transform.scale(player,(40,80))
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
            103 - Retry
        """
        self.gamestate = 0
        self.storySlide = 1 #see drawStory
        
        self.gamesleft = 1 # tasks left to win
        self.gameover = False

        #True if the task is won
        self.patternDone = False
        self.minesweeperDone = False
        self.starGameDone = False
        self.matchingDone = False
        self.highwayDone = False

        #True once all tasks are complete and the player can ESCAPE DAVIS
        self.canEscape = False

        #colors
        self.re = 140
        self.g = 200
        self.b = 17
        self.brown = (150,75,0)
        self.playercolor  = (self.re,self.g,self.b)
        self.taskColorMatch = (15, 205, 155)
        self.taskColorPattern = (15, 205, 155)
        self.taskColorStarGame = (15, 205, 155)
        self.taskColorMinesweeper = (15, 205, 155)
        self.taskColorHighway = (15, 205, 155)

        #player pos
        self.playerX = 200
        self.playerY = 600
        self.playerpos = [self.playerX,self.playerY]
        
        self.psize = 50 #player size

        # player dimensions
        self.ph = 157
        self.pw = 64
        
        #screen dimensions
        self.width = 720
        self.height = 720
        self.screen = py.display.set_mode((self.width,self.height))
        
        # clock
        self.clock = py.time.Clock()
        self.clockInitialized = False
        self.tick = TICKS_PER_SECOND
        self.timeLeft = 30 * MINUTE

    def drawBackground(self, playerpos):
        # background
        self.screen.blit(self.screenAssets["background"], (0, 0))
        
        if not self.matchingDone:        
            # Davis 102 -- MATCHING
            py.draw.rect(self.screen, (15, 0, 0), (20 - 2.5, 500 - 2.5, 105, 75))
            # Davis 102 -- MATCHING
            py.draw.rect(self.screen, self.taskColorMatch, (20, 500, 100, 70))
        
        if not self.minesweeperDone:
            # Davis 101 -- MINESWEEPER
            py.draw.rect(self.screen, (15, 0, 0), (575 - 2.5, 575 - 2.5, 105, 105))
            # Davis 101 -- MINESWEEPER
            py.draw.rect(self.screen, self.taskColorMinesweeper, (575, 575, 100, 100))
        
        if not self.patternDone:
            # Davis 117 -- PATTERN
            py.draw.rect(self.screen, (0, 0, 0), (550-2.5, 100-2.5, 105, 65))
            # Davis 117 -- PATTERN
            py.draw.rect(self.screen, self.taskColorPattern, (550, 100, 100, 60))
        
        if not self.starGameDone:
            # Prof Offices -- STAR GAME
            py.draw.rect(self.screen, (15, 0, 0), (0 - 2.5, 200 - 2.5, 90, 100))
            # Prof Offices -- STAR GAME
            py.draw.rect(self.screen, self.taskColorStarGame, (0, 200, 85, 95))

        if not self.highwayDone:
            # Robotics lab -- HIGHWAY
            py.draw.rect(self.screen, (0, 0, 0), (550-2.5, 200-2.5, 105, 65))
            # Robotics lab -- HIGHWAY
            py.draw.rect(self.screen, self.taskColorHighway, (550, 200, 100, 60))
        
        # player
        self.screen.blit(self.screenAssets["player"], (playerpos[0] ,playerpos[1] - 20))
        
        #top bar with 30 mins timer
        drawTopBar(self.screen, self.timeLeft)
        
        py.display.update()
    
    def drawStartScreen(self): 
        self.screen.blit(self.screenAssets["Start Screen"], (0, 0))
        py.display.update()
    
    def drawTutorial(self):
        self.screen.blit(self.screenAssets["Tutorial Screen"], (0, 0))
        py.display.update()
    
    def drawCredits(self): 
        self.screen.blit(self.screenAssets["Credits Screen"], (0, 0))
        py.display.update()

    def drawWinScreen(self):
        self.screen.blit(self.screenAssets["Win Screen"], (0, 0))
        py.display.update()

    def drawLoseScreen(self):
        self.screen.blit(self.screenAssets["Lose Screen"], (0, 0))
        py.display.update()
    
    #If the player wins the gamestate is set to 101.
    def winFunction(self):
        if self.gamesleft == 0:
            py.draw.rect(self.screen, (255, 0, 0), ((350 -35.3553390593), 650, 75, 75), 2)
            py.display.update()

    def playPatternGame(self):
        result = level1Pattern()

        # 0 : win | 1 : lose | 2 : quit
        if result == 0:
            return WON_GAME
        elif result == 1:
            return LOST_GAME
        else:
            return EXITED_GAME

    def playStarGame(self):
        result = starGameMain()
        
        # 0 : win | 1 : lose | 2 : quit
        if result == 0:
            return WON_GAME
        elif result == 1:
            return LOST_GAME
        else:
            return EXITED_GAME
        
    def playMinesweeperGame(self):
        result = playGame4() 

        # 0 : win | 1 : lose | 2 : quit
        if result == 0:
            return WON_GAME
        elif result == 1:
            return LOST_GAME
        else:
            return EXITED_GAME

    def playMatchingGame(self):
        result = playMatch()

        # 0 : win | 1 : lose | 2 : quit
        if result == 0:
            return WON_GAME
        elif result == 1:
            return LOST_GAME
        else:
            return EXITED_GAME
    
    def playHighwayGame(self):
        numberOfHits = highwayMain() #number of hits from game to be translated into time to be deducted from the overall game clock
        return numberOfHits 

    #Draws the story slides 
    def drawStory(self): 
        #Story State: Slides 1 - 6 are assigned numbers 1 through 6 respectively. 
        keys = py.key.get_pressed()
        if keys[py.K_1]:
            self.storySlide = 1 
        elif keys[py.K_2]: 
            self.storySlide = 2
        elif keys[py.K_3]: 
            self.storySlide = 3
        elif keys[py.K_4]: 
            self.storySlide = 4
        elif keys[py.K_5]: 
            self.storySlide = 5
        elif keys[py.K_6]:
            self.storySlide = 6

        #Updates the Screen 
        if self.storySlide == 1: 
            self.screen.blit(self.screenAssets["Story Screen 1"], (0, 0))
        if self.storySlide == 2: 
            self.screen.blit(self.screenAssets["Story Screen 2"], (0, 0))
        if self.storySlide == 3: 
            self.screen.blit(self.screenAssets["Story Screen 3"], (0, 0))
        if self.storySlide == 4: 
            self.screen.blit(self.screenAssets["Story Screen 4"], (0, 0))
        if self.storySlide == 5: 
            self.screen.blit(self.screenAssets["Story Screen 5"], (0, 0))
        if self.storySlide == 6: 
            self.screen.blit(self.screenAssets["Story Screen 6"], (0, 0))
        if self.storySlide > 6: 
            self.storySlide = 1
        py.display.update()

    def tickTime(self):
        self.tick -= 1
        if self.tick <= 0:
            self.timeLeft -= 1
            self.tick = TICKS_PER_SECOND

    def start(self):
        while True:
            self.clock.tick(60)
            #GAME LOOP -- GAME NOT OVER
            while self.gamestate < 100:
                self.clock.tick(30)
                # move me plz V
                self.tickTime()
                
                # STATE 0 : START
                if self.gamestate == 0:
                    self.drawStartScreen()
                    for event in pygame.event.get():
                        if event.type == py.QUIT:
                            sys.exit()
                        elif event.type == py.KEYDOWN:
                            if event.key == py.K_RETURN:
                                self.gamestate = 1 
                                self.clockInitialized = True
                            elif event.key == py.K_t: 
                                self.gamestate = 7
                            elif event.key == py.K_s: 
                                self.gamestate = 8
                            elif event.key == py.K_c: 
                                self.gamestate = 9 

                # STATE 1 : MAIN HUB
                elif self.gamestate == 1:
                    py.display.set_caption("Davis After Dark")
                    self.drawBackground(self.playerpos)
                    self.controls()
                    keys = py.key.get_pressed()

                    # if self.clockInitialized == True:

                    if self.gamesleft == 0:
                        self.winFunction()
                        self.canEscape = True

                    # step on matching game
                    if self.collision(self.playerpos, 20, 500, 100, 70):
                        if self.matchingDone == False: #checks if the game has not been completed yet
                            self.taskColorMatch = (125, 0, 255)
                            py.display.update()
                            if keys[py.K_n]:
                                pygame.mixer.music.load("./music/Select.wav")
                                pygame.mixer.music.play(0)
                                self.taskColorMatch = (15, 205, 155)
                                py.display.update()
                                self.gamestate = 5

                    # step on minesweeper
                    elif self.collision(self.playerpos, 575, 575, 100, 100):
                        if self.minesweeperDone == False: #checks if the game has not been completed yet
                            self.taskColorMinesweeper = (125, 0, 255)
                            py.display.update()
                            if keys[py.K_n]:
                                #pygame.mixer.music.load('./music/Se.wav')
			                    #pygame.mixer.music.play(0)
                                self.taskColorMinesweeper = (15, 205, 155)
                                py.display.update()
                                self.gamestate = 3
                    
                    # step on pattern game
                    elif self.collision(self.playerpos, 550, 100, 100, 60):
                        if self.patternDone == False: #checks if the game has not been completed yet
                            self.taskColorPattern = (125, 0, 255)
                            py.display.update()
                            if keys[py.K_n]:
                                #
                                self.taskColorPattern = (15, 205, 155)
                                py.display.update()
                                self.gamestate = 2
                                       
                    # step on star game
                    elif self.collision(self.playerpos, 0, 200, 85, 95): 
                        if self.starGameDone == False: #checks if the game has not been completed yet
                            self.taskColorStarGame = (125, 0, 255)
                            py.display.update()
                            if keys[py.K_n]:
                                #pygame.mixer.music.load('./music/Select.wav')
			                    #pygame.mixer.music.play(0)
                                self.taskColorStarGame = (15, 205, 155)
                                py.display.update()
                                self.gamestate = 4

                    # step on highway game
                    elif self.collision(self.playerpos, 550, 200, 100, 60): 
                        if self.highwayDone == False: #checks if the game has not been completed yet
                            self.taskColorHighway = (125, 0, 255)
                            py.display.update()
                            if keys[py.K_n]:
                                self.taskColorHighway = (15, 205, 155)
                                py.display.update()
                                self.gamestate = 6
                    
                    #step on exit door
                    elif self.canEscape == True and self.collision(self.playerpos, (375 -35.3553390593), 650, 75, 75):
                        if keys[py.K_n]:
                            self.gamestate = 101 #sets to win screen

                    #not stepping on anything
                    else:
                        self.taskColorMatch = (15, 205, 155)
                        self.taskColorMinesweeper = (15, 205, 155)
                        self.taskColorHighway = (15, 205, 155)
                        self.taskColorPattern = (15, 205, 155)
                        self.taskColorStarGame = (15, 205, 155)
                        py.display.update()

                # STATE 2 : PATTERN
                elif self.gamestate == 2:
                    py.display.set_caption("Memory Pattern")
                    result = self.playPatternGame()

                    if result == WON_GAME:
                        self.gamesleft -= 1
                        self.patternDone = True
                    if result == LOST_GAME:
                        self.timeLeft -= 30 #decrements by 30 sec if they lose

                    self.gamestate = 1

                # STATE 3 : MINESWEEPER
                elif self.gamestate == 3:
                    py.display.set_caption("Nuestro Sweeper")
                    result = self.playMinesweeperGame()

                    if result == WON_GAME:
                        self.gamesleft -= 1
                        self.minesweeperDone = True
                    if result == LOST_GAME:
                        self.timeLeft -= 30 #decrements by 30 sec if they lose

                    self.gamestate = 1
                    
                # STATE 4 : STAR GAME
                elif self.gamestate == 4:
                    py.display.set_caption("Star Game")
                    result = self.playStarGame()
                    
                    if result == WON_GAME:
                        self.gamesleft -= 1
                        self.starGameDone = True
                    if result == LOST_GAME:
                        self.timeLeft -= 30 #decrements by 30 sec if they lose

                    self.gamestate = 1

                # STATE 5 : MATCHING
                elif self.gamestate == 5:
                    py.display.set_caption("Matching Game")
                    result = self.playMatchingGame()
                    
                    if result == WON_GAME:
                        self.gamesleft -= 1
                        self.matchingDone = True
                    if result == LOST_GAME:
                        self.timeLeft -= 30 #decrements by 30 sec if they lose
                    
                    self.gamestate = 1
                    
                # STATE 6 : HIGHWAY
                elif self.gamestate == 6:
                    py.display.set_caption("Wrong Way Highway")
                    
                    #time in seconds to deduct from overall clock
                    timeToDeduct = self.playHighwayGame() * 5 
                    self.timeLeft -= timeToDeduct #decrements by timeToDeduct sec if they lose

                    self.highwayDone = True
                    self.gamesleft -= 1
                    self.gamestate = 1
                
                # STATE 7 : TUTORIAL
                elif self.gamestate == 7:
                    py.display.set_caption("Davis After Dark")
                    self.drawTutorial()
                    for event in py.event.get():
                        if event.key == py.K_BACKSPACE: 
                            self.gamestate = 0 

                # STATE 8 : STORY
                elif self.gamestate == 8:
                    py.display.set_caption("Davis After Dark")
                    self.drawStory()
                    for event in py.event.get():
                        if event.key == py.K_BACKSPACE: 
                            self.gamestate = 0 

                # STATE 9 : CREDITS
                elif self.gamestate == 9:
                    py.display.set_caption("Davis After Dark")
                    self.drawCredits()
                    for event in py.event.get():
                        if event.key == py.K_BACKSPACE: 
                            self.gamestate = 0 
            
            #GAME OVER LOOP -- END SCREENS
            while self.gamestate > 100:
                
                # STATE 101 : END SCREEN WIN
                if self.gamestate == 101:
                    self.drawWinScreen()

                # STATE 102 : END SCREEN LOSE
                elif self.gamestate == 102:
                    self.drawLoseScreen()

                self.clock.tick(30)
        

    def controls(self):
        # py.mixer.music.load("./music/Step.wav")
        keys = py.key.get_pressed()
        for event in py.event.get():
            if event.type == py.QUIT:
                s.exit()


            # mouse clicks on back button
            [mouseX, mouseY] = pygame.mouse.get_pos()
            if mouseX > 0 and mouseX < 210 and mouseY > 0 and mouseY < 70:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.gamestate = 0

        x = self.playerpos[0]
        y = self.playerpos[1]

        if keys[py.K_a]: # move left
            # py.mixer.music.play(1)
            x -= 2

        if keys[py.K_d]: # move right
            # py.mixer.music.play(1)
            x += 2

        if keys[py.K_s]: # move down
            # py.mixer.music.play(1)
            y += 2

        if keys[py.K_w]: # move up
            # py.mixer.music.play(1)
            y -= 2

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


    #objectX, objectY, objectWidth, objectHeight
    def collision(self, playerpos, oX, oY, oW, oH):
        pX = playerpos[0]
        pY = playerpos[1]
        eX = oX
        eY = oY

        if (pX + 10) > eX >= pX or (eX + oW) > pX >= eX:
            if (pY + 20) > eY >= pY or (eY + oH) > pY >= eY:
                return True
            return False