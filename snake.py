import sys,random,pygame,time
from pygame.locals import*

#color
white	=	(255,255,255)
black	=	(0,0,0)
red		=	(255,0,0)
blue		=	(0,0,255)
green	=	(0,128,0)
darkgreen = 	(0, 155, 0)
gray 	= 	(70,70,70)

#global variable
fps	=	10
windowwidth	=	640
windowheight	=	600
cellsize		= 	20	
cellwidth		=	int(windowwidth/cellsize)
cellheight	=	int(windowheight/cellsize)
finalscore	=	0
f = k	=	0
flg  = 	0
#directions
up    = 'up'
down  = 'down'
left  = 'left'
right = 'right'

def start():
	global clock,display,font,finalscore,fps,f
	
	pygame.init()
	
	clock	=	pygame.time.Clock()
	display	=	pygame.display.set_mode((windowwidth,windowheight))
	font		=	pygame.font.Font('freesansbold.ttf',20)
	pygame.display.set_caption('SnaKe and MouSe')
	
	while True:
		pygame.mixer.music.load('mov.mid')
		pygame.mixer.music.set_volume(0.9)
		pygame.mixer.music.play(-1)
		Show_Screen()
		fps = 10
		f = flg = k = 0
		finalscore = 0
		display.fill(black)
		Pause()
		Run_Game()
		Game_Over()

def Show_Screen():
	
	title  = pygame.font.SysFont('freesansbold.ttf',80)
	title1 = title.render('Snake & Mouse', True, white,darkgreen)
	title2 = title.render('Snake & Mouse', True, blue)
	
	key_surface1 	 = font.render('Press a key to start',True,red)
	key_rect1		 = key_surface1.get_rect()
	key_rect1.center = (100,50)
	
	key_surface2 	 = font.render('Developer',True,red)
	key_rect2		 = key_surface2.get_rect()
	key_rect2.center = (550,50)
	
	d1=d2=0
	
	while True:
		display.fill(black)
		
		surf1 = pygame.transform.rotate(title1,d1)
		rec1  = surf1.get_rect()
		rec1.center = (windowwidth/2, windowheight/2)
		
		surf2 = pygame.transform.rotate(title2,d2)
		rec2   = surf2.get_rect()
		rec2.center = (windowwidth/2, windowheight/2)
		
		
		display.blit(surf1,rec1)
		display.blit(surf2,rec2)
		display.blit(key_surface1,key_rect1)
		display.blit(key_surface2,key_rect2)
		
		pygame.display.update()
		clock.tick(fps)
		
		d1+=3
		d2-=5
		
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				if key_rect2.collidepoint(event.pos):
					Developer()
			elif event.type == QUIT:
				Exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					Exit()
				return

def printLine(string,x,y):
	FOnt = pygame.font.Font('freesansbold.ttf',15)
	surf = FOnt.render(string,True,darkgreen)
	rec  = surf.get_rect()
	rec.topleft = (x,y)
	display.blit(surf,rec)

def Developer():
	img1 = pygame.image.load('jsm.jpg')
	img2 = pygame.image.load('same.jpg')
	display.fill(black)
	display.blit(img1,(10,30))
	display.blit(img2,(10,350))
	
	temp  = pygame.font.Font('freesansbold.ttf',30) 
	surf1 = temp.render('Developer',True,red)
	rec1  = surf1.get_rect()
	rec1.center = (windowwidth/2,50)
	display.blit(surf1,rec1)
	printLine('NAME        :   JITENDRA SINGH',200,100)
	printLine('Email         :   everestacoder@gmail.com',200,125)
	printLine('Linkdin      :   www.linkedin.com/in/jitendra-singh-a41114105',200,150)
	printLine('Facebook  :   www.facebook.com/jitendrasingh.bolagura',200,175)
	
	
	surf2 = temp.render('Snake And Mouse',True,red)
	rec2  = surf2.get_rect()
	rec2.center = (windowwidth/2,300)
	display.blit(surf2,rec2)
	
	printLine('The player starts out controlling a short worm that',200,350)
	printLine('is constantly moving around the screen.Player can.',200,375)
	printLine('control which direction it turns, A mouse appears',200,400)
	printLine('randomly on the screen,  and the player must move ',200,425)
	printLine('the snake so that it eats the mouse . The snake ',200,450)	
	printLine('grows longer by one segment and a new apply randomly',200,475)
	printLine('appears on the screen The game is over if the worm',200,500)
	printLine('crashes into itself or the edges of the screen',200,525)
	
	pygame.display.update()
	
	
	while True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				return 
			elif event.type == QUIT:
				Exit()
			
			
def Pause():
	surf = font.render("Score : %s" % finalscore , True ,red);
	rec  = surf.get_rect()
	rec.center = (windowwidth/2,windowheight/2)
	display.blit(surf,rec);
	
	surf1 = font.render("Press Space To Resume" ,True, red);
	rec1  = surf1.get_rect()
	rec1.center = (windowwidth/2,windowheight/2+100)
	display.blit(surf1,rec1);
	
	pygame.display.update()
	
	while True:
		if Press_Space():
			return 

def Press_Space():
	if(len(pygame.event.get(QUIT))>0):
		Exit()
	
	keyevent=pygame.event.get(KEYDOWN)
	
	if(len(keyevent)==0):
		return None
	if(keyevent[0].key==K_ESCAPE):
		Exit()
	elif keyevent[0].key in (K_RETURN,K_SPACE):
		return 1 
	
def Exit():
	pygame.quit()
	sys.exit()
	
def getrandomlocation():
	return { 'x': random.randint(0,cellwidth-1) , 'y': random.randint(0,cellheight-1) }

def Run_Game():
	global finalscore
	
	display.fill(black)
	
	startX = random.randint(5,cellwidth-8)
	startY = random.randint(5,cellheight-8)
	
	snake_crd = [{'x': startX, 'y': startY},
                  {'x': startX - 1, 'y': startY},
                  {'x': startX - 2, 'y': startY}];
	
	direction = right
	mouse = getrandomlocation()
	
	global f,flg,k
	while True:
		flag=0
		global fps
		for event in pygame.event.get():
			if event.type == QUIT:
				Exit()
			elif event.type == KEYDOWN:
				if (event.key == K_LEFT) and direction != right:
					direction = left
				elif (event.key == K_RIGHT) and direction != left:
					direction = right
				elif (event.key == K_UP) and direction != down:
					direction = up
				elif (event.key == K_DOWN ) and direction != up:
					direction = down
				elif event.key == K_ESCAPE:
					flag = 1		
				elif event.key == K_SPACE:
					Pause()	
		
		if snake_crd[0]['x']==-1 or snake_crd[0]['y']==-1 or snake_crd[0]['x']==cellwidth or snake_crd[0]['y']==cellheight:
			flag = 1
		
		for crd in snake_crd[1:]:
			if (crd['x']==snake_crd[0]['x']) and (crd['y']==snake_crd[0]['y']):
				flag=1
				break 
		
		if flag == 1:
			pygame.mixer.music.load('death.mid')
			pygame.mixer.music.play()
			return
			
			
		if snake_crd[0]['x']==mouse['x'] and snake_crd[0]['y']==mouse['y']:
			obj = pygame.mixer.Sound('hit.wav')
			obj.play()
			time.sleep(.05)
			f = f+1
			mouse = getrandomlocation()
			
		else :
			del snake_crd[-1]
			
		
		if direction == up:	
			new={'x':snake_crd[0]['x'],'y':snake_crd[0]['y']-1}
		elif direction == down:
			new={'x':snake_crd[0]['x'],'y':snake_crd[0]['y']+1}
		elif direction == left:
			new={'x':snake_crd[0]['x']-1,'y':snake_crd[0]['y']}
		elif direction == right:	
			new={'x':snake_crd[0]['x']+1,'y':snake_crd[0]['y']}	
			
		snake_crd.insert(0,new)
		display.fill(black)
		DrawGrid()
		DrawSnake(snake_crd)
		
		if(f%5==4):
			DrawMouse2(mouse)
		else:
			DrawMouse1(mouse)
		
		if f%5==0 and f!=0:
			k = 1
			
		score = len(snake_crd)-3
		DrawScore(score,k)
		if finalscore != score:
			finalscore = score
			if (finalscore%100) == 0:
				fps += 5
				Pause()
				
		pygame.display.update()
		clock.tick(fps)
		
def DrawSnake(snake):
	for crd in snake:
		x=crd['x']*cellsize
		y=crd['y']*cellsize
		
		src1 = pygame.Rect(x,y,cellsize,cellsize)
		pygame.draw.rect(display,darkgreen,src1)
		
		src2 = pygame.Rect(x+4,y+4,cellsize-8,cellsize-8)
		pygame.draw.rect(display,green,src2)
		
def DrawMouse1(mouse):
	x = mouse['x']*cellsize
	y = mouse['y']*cellsize
	pygame.draw.circle(display,red,(x+10,y+10),cellsize/2,0)
			

def DrawMouse2(mouse):
	
	x = mouse['x']*cellsize
	y = mouse['y']*cellsize
	pygame.draw.circle(display,(random.randint(1, 255),random.randint(1,255),random.randint(1, 255)),(x+10,y+10),cellsize/2,0)

			
def DrawGrid():
	for i in range(0,windowwidth,cellsize):
		pygame.draw.line(display,gray,(i,0),(i,windowheight))
	
	for i in range(0,windowheight,cellsize):
		pygame.draw.line(display,gray,(0,i),(windowwidth,i))
		

def DrawFinalScore(score,k):
	score = (score)*10
	temp = pygame.font.Font('freesansbold.ttf',60)
	surf = temp.render("Final Score : %s " % score,True,red)
	rec  = surf.get_rect()
	rec.center =  (windowwidth/2,windowheight-150)
	display.blit(surf,rec)
			
def DrawScore(score,k):
	score = (score)*10
	temp = pygame.font.Font('freesansbold.ttf',20)
	surf = temp.render("Score : %s " % score,True,white)
	rec  = surf.get_rect()
	rec.center =  (windowwidth-100,20)
	display.blit(surf,rec)	
	
	
		
def Press_Enter():
	if(len(pygame.event.get(QUIT))>0):
		Exit()
	
	keyevent=pygame.event.get(KEYDOWN)
	
	if(len(keyevent)==0):
		return None
	if keyevent[0].key == K_ESCAPE:
		Exit()
	elif keyevent[0].key == K_RETURN:
		return 1 
		
def Game_Over():	
	display.fill(black)
	DrawFinalScore(finalscore , k)
	while True:
		temp  = pygame.font.Font('freesansbold.ttf',100)
		surf1 = temp.render("GAME",True,(random.randint(1,255),random.randint(1,255),random.randint(1,255)))
		rec1  = surf1.get_rect()
		rec1.center =  (windowwidth/2,windowheight/2-100)
		surf2 = temp.render("OVER",True,(random.randint(1,255),random.randint(1,255),random.randint(1,255)))
		rec2  = surf2.get_rect()
		rec2.center =  (windowwidth/2,windowheight/2)
		display.blit(surf1,rec1)
		display.blit(surf2,rec2)
		
		surf3 = font.render("Press Enter To Play Again !!",True,red)
		rec3  = surf3.get_rect()
		rec3.center =  (windowwidth/2,windowheight-80)	
		display.blit(surf3,rec3)
		pygame.display.update()
		
		if Press_Enter():
			return
		
		
if __name__ == '__main__':
	start()
