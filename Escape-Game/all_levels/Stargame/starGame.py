"""
Bullet Hell Task
January 10 2020

Dodge the Stars for 25 seconds to win the game!
"""

import random as r
import time as t
import pygame as py
import common as cm 
py.init()

# Creates a screen
screen = py.display.set_mode((720, 720))
py.display.set_caption("Dodge the Stars to Win the Game!") 

#Draws the background
def backgroundImg(x, y):
    bgImg = py.image.load("./assets/bulletGameBackground.png")
    screen.blit(bgImg,(x, y))
    return bgImg

#Draws the start screen
def startImage(x, y):
    startImg = py.image.load("./assets/Startforbullets.png")
    return startImg

#Draws the death screen
def deathScreen():
    lose_img = py.image.load("./assets/loseScreen.png")
    screen.blit(lose_img, (0,0))

#Creates the player
def player(x, y):
    playerImg = py.image.load("./assets/spaceship.png").convert_alpha()
    screen.blit(playerImg, (x, y))
    return playerImg

#This function uses the distance formula 
def impDistanceFormula(x, y, j, k, hitbox):
    playerHb = 15
    alive = True
    d = distance(x + hitbox, y + hitbox, j + playerHb, k + playerHb)
    if d < hitbox + 10 or d < hitbox - 10:
        alive = False
    return alive

#Returns the distance between the bullet and the player
def distance(x, y, j, k):
    df = ( (x-j)**2 + (y-k)**2 )**0.5
    return df

#Creates a horizontal line of bullets, returns if the player is alive or not. 
def bulletLine(x, y, pX, pY, hitbox):

    for i in range(10):
        bullets = py.image.load("./assets/starBullet.png")
        screen.blit(bullets, (i*75 + x, y))
        alive = impDistanceFormula(i*75 + x, y, pX, pY, hitbox)
        if alive == False: 
            return alive

#Creates a verticle line of bullets 
def bulletSide(x, y, pX, pY, hitbox): 

    for i in range(10):
        bullets = py.image.load("./assets/starBullet.png").convert_alpha()
        screen.blit(bullets, (x, i*75 + y))
        alive = impDistanceFormula(x, i*75 + y, pX, pY, hitbox)
        if alive == False: 
            return alive

#Draws a big bullet
def bulletCircle(x, y, pX, pY, hitbox):
    bullets = py.image.load("./assets/Meteor.png").convert_alpha()
    screen.blit(bullets, (x, y))
    alive = impDistanceFormula(x, y, pX, pY, hitbox)
    if alive == False: 
        return alive

#Creates bullets in an arrow. 
def bulletArrow(x, y, pX, pY, hitbox): 

    for i in range(6):
        b1 = py.image.load("./assets/starBullet.png").convert_alpha()
        b2 = py.image.load("./assets/starBullet.png").convert_alpha()
        b3 = py.image.load("./assets/starBullet.png").convert_alpha()
        screen.blit(b1, (x, i*75 + y))
        screen.blit(b2, (i*75 + x, y))
        screen.blit(b3, (i*75 + x, i*75 + y))
    
        a1 = impDistanceFormula(i*75 + x, y, pX, pY, hitbox)
        a2 = impDistanceFormula(x, i*75 + y, pX, pY, hitbox)
        a3 = impDistanceFormula(i*75 + x, i*75 + y, pX, pY, hitbox)

        if a1 == False:  
            return a1
        if a2 == False: 
            return a2
        if a3 == False: 
            return a3

#Draws the bullets in a square. 
def bulletSquare(x, y, pX, pY, hitbox): 

    for i in range(5):
        b1 = py.image.load("./assets/starBullet.png").convert_alpha()
        b2 = py.image.load("./assets/starBullet.png").convert_alpha()
        b3 = py.image.load("./assets/starBullet.png").convert_alpha()
        b4 = py.image.load("./assets/starBullet.png").convert_alpha()

        screen.blit(b1, (x, i*60 + y))
        screen.blit(b1, (i*60 + x, y))
        screen.blit(b1, (i*60 + x, y + 240))
        screen.blit(b1, (x + 240, i*60 + y))

        a1 = impDistanceFormula(x, i*60 + y, pX, pY, hitbox)
        a2 = impDistanceFormula(i*60 + x, y, pX, pY, hitbox)
        a3 = impDistanceFormula(i*60 + x, y + 240, pX, pY, hitbox)
        a4 = impDistanceFormula(x + 240, i*60 + y, pX, pY, hitbox)

        if a1 == False:  
            return a1
        if a2 == False: 
            return a2
        if a3 == False: 
            return a3
        if a4 == False: 
            return a4

#Draws one star.
def soloBullet(x, y, pX, pY, hitbox): 
    bullets = py.image.load("./assets/starBullet.png").convert_alpha()
    screen.blit(bullets, (x, y))
    alive = impDistanceFormula(x, y, pX, pY, hitbox)
    if alive == False: 
        return alive

#Draws 3 bullets at random.
def randomBullets(x, y, pX, pY, hitbox):
    for i in range(3):
        bullets = py.image.load("./assets/starBullet.png").convert_alpha()
        screen.blit(bullets, (x, y + i*80))
        alive = impDistanceFormula(x, i*80 + y, pX, pY, hitbox)
        if alive == False: 
            return alive

#GameLoop function, returns victory as true if the player wins and fasle otherwise.
def starGameMain():

    #Bullet Coordinates
    bulletX = 25
    bulletY = 25 

    bulletX2 = 25
    bulletY2 = 25
    bulletX2a = 0 
    bulletY2a = 0 

    #Coords for the big bullets
    bulletCx = 25
    bulletCy = 25

    bulletBx = 360
    bulletBy = 25

    bulletLx = 680
    bulletLy = 25

    squareX = 25
    squareY = 25

    centerX = 275
    centerXa = 275
    centerXb = 275
    centerY = 275
    centerYa = 275
    centerYb = 275
    centerConstant = 275

    randX = 25
    randY = r.randint(25, 720)
    randXa = r.randint(25, 720)
    randYa = 25

    constantX = 275
    constantY = 275
    constantXa = 275
    constantYa = 275
    constantXb = 275
    constantYb = 275

    #Player starting coordinates.
    playerX = 500
    playerY = 500

    #bullet speed and hitboxes
    bS = 4
    smallHb = 15 #use 15
    bigHb = 46 #use 46  

    #time
    timer = 0
    endTime = 25000

    #The speed at which the player and enemy move around. 
    playerSpeed = 6

    startImg = py.image.load("./assets/Startforbullets.png")
    button = py.Rect(15, 12, 226, 73)

    #Actual game loop  
    movement = True # if this is false the player cannot move anymore.
    victory = False # if this is true the player wins
    active = False # makes the while the loop run or not 
    start = False # if false the start screen will be displayed 
    py.mixer.Channel(0).play(py.mixer.Sound('./music/BulletHell_theme.wav'))
    while start == False: 
        screen.blit(startImg, (0, 0))
        py.display.update()
        for event in py.event.get():
            if event.type == py.KEYDOWN: 
                start = True
                active = True
        while(active):
            #Checks if the "X" has been pressed and if the back button is pressed. 
            for event in py.event.get():
                if event.type == py.QUIT:
                    active = False
                if event.type == py.MOUSEBUTTONDOWN: 
                    mouse = event.pos
                    if button.collidepoint(mouse): 
                        py.mixer.pause()
                        return 2 #Press the back button the game will return 2 
            
            #Checks for keypresses
            if movement: 
                if event.type == py.KEYDOWN:
                    if event.key == py.K_w:
                        playerY -= playerSpeed
                    if event.key == py.K_s:
                        playerY += playerSpeed
                    if event.key == py.K_d:
                        playerX += playerSpeed
                    if event.key == py.K_a:
                        playerX -= playerSpeed

            #Boundries of the window
            if playerX <= 10: 
                playerX = 10
            if playerX >= 680: 
                playerX = 680
            if playerY <= 10: 
                playerY = 10
            if playerY >= 680: 
                playerY = 680

            #The timer
            if timer <= endTime: 
                timer += 25 #25 for john's PC
                backgroundImg(0, 0)
            if timer >= endTime and movement != False:
                victory = True
                screen.blit(py.image.load("./assets/WinScreen.png"), (0,0))  
                py.mixer.pause()
                return 0 #if you win the game, it will return 0 

            cm.drawTopBar(screen, timer/1000)
    
            #Draws the bullets at the top of the screen and has them move down. 
            if movement and victory == False: 
                if bulletY <= 720:  
                    b1 = bulletLine(bulletX, bulletY, playerX, playerY, smallHb)
                    if b1 == False: 
                        movement = False
                    bulletY += bS
                if bulletX2 <= 720:  
                    b2 = bulletSide(bulletX2, bulletY2, playerX, playerY, smallHb)
                    if b2 == False: 
                        movement = False
                    bulletX2 += bS
                if bulletY >= 720 and bulletCx <= 720: 
                    b3 = bulletCircle(bulletCx, bulletCy, playerX, playerY, bigHb)
                    if b3 == False: 
                        movement = False
                    bulletCx += bS
                    bulletCy += bS
                if bulletCx >= 360 and bulletBy >= 0: 
                    b4 = bulletCircle(bulletBx, bulletBy, playerX, playerY, bigHb)
                    if b4 == False: 
                        movement = False
                    bulletBy += bS
                if bulletBy >= 720: 
                    b5 = bulletCircle(bulletLx, bulletLy, playerX, playerY, bigHb)
                    if b5 == False: 
                        movement = False
                    bulletLy += bS
                if bulletLy >= 720: 
                    b6 = bulletArrow(bulletX2a, bulletY2a, playerX, playerY, smallHb)
                    if b6 == False: 
                        movement = False
                    bulletX2a += bS
                    bulletY2a += bS 
                    if squareX < 160 and squareY < 160: 
                        b7 = bulletSquare(squareX, squareY, playerX, playerY, smallHb)
                        if b7 == False: 
                            movement = False
                        squareX += bS
                        squareY += bS
                    if squareX >= 160 and squareY >= 160: 
                        b8 = bulletSquare(squareX, squareY, playerX, playerY, smallHb)
                        if b8 == False: 
                            movement = False
                        b9 = bulletCircle(275, 275, playerX, playerY, bigHb)
                        if b9 == False: 
                            movement = False
                        if bulletX2a >= 720 and centerX < 720:
                            b10 = bulletCircle(centerX, centerY, playerX, playerY, bigHb)
                            if b10 == False: 
                                movement = False
                            centerX += bS
                            b11 = bulletCircle(centerX, centerYa, playerX, playerY, bigHb)
                            if b11 == False: 
                                movement = False
                            b12 = bulletCircle(centerConstant, centerYa, playerX, playerY, bigHb)
                            if b12 == False: 
                                movement = False
                            centerYa += bS
                            b13 = bulletCircle(centerXa, centerYa, playerX, playerY, bigHb)
                            if b13 == False: 
                                movement = False
                            b14 = bulletCircle(centerXa, centerConstant, playerX, playerY, bigHb)
                            if b14 == False: 
                                movement = False
                            centerXa -= bS
                            b15 = bulletCircle(centerConstant, centerYb, playerX, playerY, bigHb)
                            if b15 == False: 
                                movement = False
                            b16 = bulletCircle(centerXa, centerYb, playerX, playerY, bigHb)
                            if b16 == False: 
                                movement = False
                            centerYb -= bS
                            b17 = bulletCircle(centerX, centerYb, playerX, playerY, bigHb) 
                            if b17 == False: 
                                movement = False                 
                if randX >= 720:
                    randY = r.randint(25, 720)
                    randX = 25
                b18 = randomBullets(randX, randY, playerX, playerY, smallHb)
                if b18 == False: 
                    movement = False
                randX += bS
                if randYa >= 720:
                    randXa = r.randint(25, 720)
                    randYa = 25
                b19 = bulletCircle(randXa, randYa, playerX, playerY, bigHb)
                if b19 == False: 
                    movement = False
                randYa += bS 
                
                player(playerX, playerY)

            if movement == False: 
                deathScreen()
                py.mixer.pause()
                return 1 #if you lose the game will return 1

            py.display.update()
    