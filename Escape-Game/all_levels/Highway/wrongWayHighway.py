import time
import sys, pygame
import random

def startScreen(time=300,harder=False): #setting harder to true makes the cars move faster

#sets the screen dimensions and colors
	size=width,height=720,720
	notReady=True
	frame=0
	background=pygame.image.load("wrongWayInstructions.png")
	backgroundRect=background.get_rect()
	screen=pygame.display.set_mode(size)
	black=(0,0,0)
	screen.fill(black)
	pygame.init()

	#start screen loop
	while(notReady==True):
		

		screen.blit(background,backgroundRect)
		pygame.display.flip()
		
		frame+=1
		pygame.event.pump()
		key=pygame.key.get_pressed()
		if key[pygame.K_w]==1:
			notReady=False

	#returns the final time
	finalTime=main(time,harder)
	return finalTime

	#main game function
	#has a variable if you want to make the game harder
def main(time=300,harder=False):

	if harder==True:
		speed=20
	else:
		speed=15
	#sets the background and loads the images	
	start=-1000
	background= pygame.image.load("road1.png")
	backgroundRect=background.get_rect()
	green=(35, 125, 34)
	car= pygame.image.load("car.png")
	carHit=car.get_rect()
	pygame.init()
	size=width,height=720,720
	screen=pygame.display.set_mode(size)

	#sets some main game variables
	gameOver=False

	#list of enemies
	enemy=[]
	enemyHit=[]
	#dt=1/60
	num=0

	carHit=carHit.move(340,500)

	font = pygame.font.SysFont("comicsansms", 25)


	carSpawns=[]
	#creates the enemies list and determines their spawn locations
	for j in range(25):
		carSpawns.append(0)
	for j in range(len(carSpawns)):
		carSpawns[j]=random.randint(180,540)

	#more game variables
	background1=True #this boolean checks which background is in use
	frame=1

	#the amount of cars that have spawned
	num=0


	invincible=False
	carsAllSpawned=False
	timesHit=0

	delay=45 #spawn delay
	#timer variables and text
	timer=0
	text=""
	temporary=""
	color=(0,0,0)
	while gameOver==False:

		#this updates the timer every fourty frames
		if frame%40==0 or frame==1:
			time-=1
			timer=fixTime(time)
			timer[0]=str(timer[0])
			timer[1]=str(timer[1])
			temporary=(timer[0]+"' "+timer[1]+'"')
		text = font.render(temporary, True, (color))
		
		#this changes the background every 8 frames so it looks like its moving
		if frame%8==0:
			if background1==True:
				background= pygame.image.load("road2.png")
				backgroundRect=background.get_rect()
				background1=False
			else:
				background= pygame.image.load("road1.png")
				backgroundRect=background.get_rect()
				background1=True

		#after 13 cars have passed it makes them move faster
		if num==13 and harder==False:
			speed=25
			delay=30
		elif num==13 and harder==True:
			speed=30
			delay=20

		


		screen.fill(green)

		screen.blit(background,backgroundRect)
		screen.blit(car,carHit)
		screen.blit(text,(0,0))
		pygame.time.Clock().tick(60)

		#main controls
		pygame.event.pump()
		key=pygame.key.get_pressed()
		if key[pygame.K_d]==1:
			carHit=carHit.move(15,0)
		if key[pygame.K_a]==1:
			carHit=carHit.move(-15,0)
		if key[pygame.K_p]==1:
			sys.exit()

		#makes sure the car doesnt hit the end
		if carHit.left<120:
			carHit=carHit.move(15,0)
		if carHit.right>width-120:

			carHit=carHit.move(-15,0)

		#spawns a car after a set time
		if frame%delay==0:
			#print(num)
			enemy.append(pygame.image.load("enemy.png"))
			enemyHit.append(0)
			enemyHit[num]=enemy[0].get_rect()
			enemyHit[num]=enemyHit[num].move(carSpawns[num],-50)
			screen.blit(enemy[num],enemyHit[num])
			num+=1
			pygame.display.flip()

		#ends once all the cars have passed
		if num==25:
			gameOver=True
		

		#moves the enemies
		for j in range(len(enemy)):
			enemyHit[j]=enemyHit[j].move(0,speed)
			screen.blit(enemy[j],enemyHit[j])

		pygame.display.flip()

		#checks for collisions and deducts time from the main timer if theres a hit
		if collide(carHit,enemyHit,invincible)==True:
			start=frame
			invincible=True
			car=pygame.image.load("blank.png")
			pygame.mixer.music.load('hit.wav')
			pygame.mixer.music.play(0)
			timesHit+=1
			time-=5
			color=(255,0,0)

		#the car hit animation where it just flashes on and off twice
		#you get a few I frames too
		if frame==start+10:
			car=pygame.image.load("car.png")

		if frame==start+20:
			car=pygame.image.load("blank.png")

		if frame==start+30:
			car=pygame.image.load("car.png")
			invincible=False
			color=(0,0,0)


		frame+=1

	return time
	#print(timesHit)

	#the timer function
	#converts a bunch of seconds into minutes and seconds
def fixTime(time):
	minutes=time/60
	minutes=int(minutes)
	seconds=time%60
	timer=[minutes,seconds]
	return timer

	#collision function
	#checks every car and sees if they are within a certai distance
def collide(carHit,enemyHit,invincible):
	if invincible==True:
		return False
	for i in range(len(enemyHit)):

		if 8>=enemyHit[i].bottom-carHit.top>=0:
			if 0>=enemyHit[i].left-carHit.right>=-2*carHit[2]:
				return True
		if 0>=enemyHit[i].left-carHit.right>=-1*carHit[2]:
			if 0>=carHit.top-enemyHit[i].bottom>=-2*carHit[3]:
				return True

		if carHit[3]>=enemyHit[i].right-carHit.left>=0:
			if 0>=carHit.top-enemyHit[i].bottom>=-2*carHit[3]:
				return True




if __name__ == "__main__":
	time=startScreen(300)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
			
		