import time
import sys, pygame
import random

#main function
def endScreen(time=300, loser=True):
	size=width,height=720,720
	notReady=True
	frame=0

	#checks the loser variable to determine which screen to use
	if loser==True:
		background=pygame.image.load("./assets/End2.png")

	else:
		background=pygame.image.load("./assets/End1.png")

	#creates the screen
	backgroundRect=background.get_rect()
	screen=pygame.display.set_mode(size)
	black=(0,0,0)
	screen.fill(black)
	pygame.init()
	font = pygame.font.SysFont("helvetica", 50)

	#this calls the fixTime function to generate the time value
	timer=fixTime(time)
	
	
	screen.blit(background,backgroundRect)
	text = font.render(timer, True, (0,0,0))
	screen.blit(text,(300,270))
	pygame.display.flip()

	#main loop
	#ends when you hit enter
	while(True):
		frame+=1
		pygame.event.pump()
		key=pygame.key.get_pressed()
		if key[pygame.K_RETURN]==1:
			sys.exit()
		
	#converts from seconds to minutes and seconds into a list
def fixTime(time):
	minutes=time/60
	minutes=int(minutes)
	seconds=time%60
	timer=[minutes,seconds]
	timer[0]=str(timer[0])
	timer[1]=str(timer[1])
	finalTime=(timer[0]+"' "+timer[1]+'"')
	return finalTime

if __name__ == "__main__":
	endScreen()
    