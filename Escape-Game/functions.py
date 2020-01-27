
from variables import*
import pygame as py
import sys as s


def controls():
    # py.mixer.music.load("./music/Step.wav")
    keys = py.key.get_pressed()
    for event in py.event.get():
        if event.type == py.QUIT:
            s.exit()

    

    x = playerpos[0]
    y = playerpos[1]
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
    playerpos[0] = x
    playerpos[1] = y

    # collision data

    if 0 > playerpos[0]:
        playerpos[0] = 2

    if playerpos[0] > width - 50:
        playerpos[0] = width - 52

    if playerpos[1] > height - 50:
        playerpos[1] = height - 52

    if playerpos[1] < 0:
        playerpos[1] = 2


   
    

def collision(playerpos, oX, oY, oW, oH):

    pX = playerpos[0]
    pY = playerpos[1]
    eX = oX
    eY = oY

    if (pX + 10) > eX >= pX or (eX + oW) > pX >= eX:
        if (pY + 20) > eY >= pY or (eY + oH) > pY >= eY:
            return True
        return False
