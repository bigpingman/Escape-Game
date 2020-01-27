import pygame as py
from variables import*
def startdisp():
    func = True
    while func:
        startscreen = py.image.load("./assets/startscreen1.png").convert_alpha()
        screen.blit(startscreen,(0,0))
        keys = py.key.get_pressed()
        if keys[py.K_RETURN]:
            start = False
            break
        
        if keys[py.K_s]:
            print("Storyline fr")
            break

        
        if keys[py.K_t]:
            print("talk to dese niggas fr!!!")
            break

        if keys[py.K_c]:
            print("roll dem mf credits")
            break

startdisp()
