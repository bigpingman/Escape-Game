import pygame as py
import random as r

py.init()
gamestate = 1
game1ready = False
game2ready = False
game3ready = False
gametype = 0
re = 140
psize = 50
g = 200
gamesleft = 3
clock = py.time.Clock()
b = 17
playercolor  = (re,g,b)
playerX = 200
playerY = 600
memH = 70
memW = 100
playerpos = [playerX,playerY]
width = 1000
height = 1000
screen = py.display.set_mode((width,height))
gameover = False
brown = (150,75,0)
memX = 0
memY = 500
# player dimensions
ph = 157
pw = 64