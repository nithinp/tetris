########################################################################
#                                                                      #
#                      Simple-Tetris-Game                              #
#                                                                      #
#                                                                      #
# CREATED BY    :    Nithin.P                                          #
#                    nithup123@gmail.com                               #
#                    http://facebook.com/nithin.nithinp                #
#                                                                      #
# Description   :    This is a Simple Tetris Game  coded by            #
#                    me in python using pygame module.                 #
#                                                                      #
# License       :    This Source Code is free to use                   #
#                    for educational purpose only.                     #
#                                                                      #
# Instructions  :    Use UP key for change the shape.                  #
#                    Use DOWN key to accelarate speed of shape.        #
#                    USE LEFT key for move to left.                    #
#                    USe RIGHT key for move to right.                  #
#                                                                      #
########################################################################


import pygame
import sys
import random




# Initial Conditions.

score=0
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
gray=(128,128,128)
size=[660,600]
game=[ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ]
new_one=True
i_1=0
i_2=0
i_3=1
i_4=1
j_1=9
j_2=10
j_3=9
j_4=10
can_accel_left=False
can_accel_right=False
can_accel_down=False
can_change_shape=False
time1=pygame.time.get_ticks()
time2=pygame.time.get_ticks()
shape=0
game_over=True
clock=500







# Definition of printing press any key function.

def print_press_any_key() :
	global paused_game
	font=pygame.font.Font(None,30)
	if paused_game :
		text = font.render("Press Escape key to continue", True, gray)
	else :
		text = font.render("Press any key to continue", True, gray)
	rect = text.get_rect()
	rect.centerx=size[0]-150
	rect.centery=size[1]-50
	screen.blit(text, rect)







# Definition of wait for any key function

def wait_for_any_key() :
	while True :
		for event in pygame.event.get() :
			if event.type==pygame.QUIT :
				sys.exit()
				pygame.quit()
			if event.type == pygame.KEYDOWN :
				return True






# Function to draw initial screen.

def draw_initial_screen() :
	font=pygame.font.Font(None,220)
	gameText = font.render("Nithin's", True, white)
	overText = font.render('Tetris', True, white)
	over1Text = font.render('Game', True, white)
	gameRect = gameText.get_rect()
	overRect = overText.get_rect()
	over1Rect = over1Text.get_rect()
	gameRect.centerx=(size[0]/2)
	gameRect.centery=(size[1]/2)-150
	overRect.centerx=(size[0]/2)
	overRect.centery=(size[1]/2)
	over1Rect.centerx=(size[0]/2)
	over1Rect.centery=(size[1]/2+150)
	screen.blit(gameText, gameRect)
	screen.blit(overText, overRect)
	screen.blit(over1Text, over1Rect)
	print_press_any_key()
	pygame.display.update()







# Definition of function to print game over.

def print_game_over() :
	font=pygame.font.Font(None,260)
	font1=pygame.font.Font(None,50)
	gameText = font.render('Game', True, white)
	overText = font.render('Over', True, white)
	sc="Your Score : "+str(score)
	scoreText = font1.render(sc, True, white)
	gameRect = gameText.get_rect()
	overRect = overText.get_rect()
	scoreRect = scoreText.get_rect()
	gameRect.centerx=(size[0]/2)
	gameRect.centery=(size[1]/2)-150
	overRect.centerx=(size[0]/2)
	overRect.centery=(size[1]/2)
	scoreRect.centerx=(size[0]/2)
	scoreRect.centery=(size[1]/2)+120
	screen.blit(gameText, gameRect)
	screen.blit(overText, overRect)
	screen.blit(scoreText, scoreRect)
	




# Definition of function to change position of the shapes

def change_position(direction,start_accel) :
	global can_accel_left
	global can_accel_right
	global can_accel_down
	global can_change_shape
	if start_accel :
		if direction=='left' :
			can_accel_left=True
		if direction=='right' :
			can_accel_right=True
		if direction=='down' :
			can_accel_down=True
		if direction=='up' :
			can_change_shape=True
	else :
		if direction=='left' :
			can_accel_left=False
		if direction=='right' :
			can_accel_right=False
		if direction=='down' :
			can_accel_down=False
		if direction=='up' :
			can_change_shape=False






# Function to draw screen.

def draw_screen() :
	global game_over
	screen.fill(black)
	i=0
	while i<(size[0]) :
		pygame.draw.line(screen,gray,(i,0),(i,size[1]))
		i+=30
	i=0
	while i<(size[1]) :
		pygame.draw.line(screen,gray,(0,i),(size[0],i))
		i+=30
	if game_over==False :
		font=pygame.font.Font(None,100)
		scoreText = font.render(str(score), True, white)
		scoreRect = scoreText.get_rect()
		scoreRect.centerx=size[0]-100
		scoreRect.centery=100
		screen.blit(scoreText,scoreRect)








# Main play() function.

def play() :
	global clock
	global game_over
	global can_accel_left
	global can_accel_right
	global can_accel_down
	global new_one
	global i_1
	global i_2
	global i_3
	global i_4
	global j_1
	global j_2
	global j_3
	global j_4
	global time1
	global time2
	global score
	global shape
	if new_one :
		new_one=False
		if game[i_1][j_1]==1 :
			game_over=True
			for i in range(20) :
				for j in range(22) :
					if game[i][j]==1 :
						left=(j*30)+1
						up=(i*30)+1
						pygame.draw.rect(screen,red,(left,up,29,29))
			print_game_over()
			print_press_any_key()
		else :
			if shape==0 :
				i_1=0
				i_2=0
				i_3=1
				i_4=1
				j_1=9
				j_2=10
				j_3=9
				j_4=10
			elif shape==1 :
				i_1=0
				i_2=0
				i_3=0
				i_4=0
				j_1=8
				j_2=9
				j_3=10
				j_4=11
			elif shape==2 :
				i_1=0
				i_2=1
				i_3=2
				i_4=3
				j_1=9
				j_2=9
				j_3=9
				j_4=9
			elif shape==3 :
				i_1=0
				i_2=1
				i_3=1
				i_4=2
				j_1=9
				j_2=9
				j_3=10
				j_4=10
			elif shape==4 :
				i_1=1
				i_2=2
				i_3=0
				i_4=1
				j_1=9
				j_2=9
				j_3=10
				j_4=10
			game[i_1][j_1]=1
			game[i_2][j_2]=1
			game[i_3][j_3]=1
			game[i_4][j_4]=1
	else :
		if pygame.time.get_ticks() > (time2+100) :
			game[i_1][j_1]=0
			game[i_2][j_2]=0
			game[i_3][j_3]=0
			game[i_4][j_4]=0
			if can_change_shape :
				if shape==0 :
					if j_1-1 >= 0 and j_2+1 <=21 :
						if game[i_1][j_1-1]==0 and game[i_1][j_2+1]==0 :
							i_3=i_1
							i_4=i_1
							j_3=j_1-1
							j_4=j_2+1
							x=i_3
							i_3=i_2
							i_2=x
							x=j_3
							j_3=j_2
							j_2=x
							x=i_2
							i_2=i_1
							i_1=x
							x=j_2
							j_2=j_1
							j_1=x
							shape=1
				elif shape==1 :
					if i_1+3 <= 19 :
						if game[i_1+1][j_1]==0 and game[i_1+2][j_1]==0 and game[i_1+3][j_1]==0 :
							i_2=i_1+1
							i_3=i_1+2
							i_4=i_1+3
							j_2=j_1
							j_3=j_1
							j_4=j_1
							shape=2
				elif shape==2 :
					if j_1<=20 :
						if game[i_2][j_2+1]==0 and game[i_2+1][j_2+1]==0 :
							i_3=i_2
							j_3=j_2+1
							i_4=i_2+1
							j_4=j_2+1
							shape=3
				elif shape==3 :
					if (i_4+1)<=19 :
						if game[i_4+1][j_2]==0 :
							i_1=i_4
							i_2=i_4+1
							shape=4
				elif shape==4 :
					if game[i_2][j_4]==0 :
						i_3=i_1
						i_4=i_2
						shape=0
						x=i_2
						i_2=i_3
						i_3=x
						x=j_2
						j_2=j_3
						j_3=x
			if shape == 0 :
				if can_accel_left :
					if (j_1)>=1 :
						if game[i_1+1][j_1-1]==0 and game[i_1][j_1-1]==0   :
							j_1-=1
							j_3-=1
							j_2-=1
							j_4-=1
				if can_accel_right :
					if (j_2+1) <=21 : 	
						if game[i_2+1][j_2+1]==0 and game[i_2][j_2+1]==0  :
							j_1+=1
							j_3+=1
							j_2+=1
							j_4+=1
				if can_accel_down :
					if (i_1+1) < 19 and (i_2+1) < 19 :
						if game[i_1+2][j_1]==0 and game[i_2+2][j_2]==0  :
							i_1+=1
							i_3+=1
							i_2+=1
							i_4+=1
						else :
							new_one=True
					else :
						new_one=True

			elif shape ==1 :
				if can_accel_left :
					if (j_1)>=1 :
						if game[i_1][j_1-1]==0 :
							j_1-=1
							j_3-=1
							j_2-=1
							j_4-=1
				if can_accel_right :
					if (j_4+1) <=21 : 	
						if game[i_2][j_4+1]==0 :
							j_1+=1
							j_3+=1
							j_2+=1
							j_4+=1
				if can_accel_down :
					if (i_1+1) < 20 and (i_2+1) < 20 :
						if game[i_1+1][j_1]==0 and game[i_2+1][j_2]==0 and game[i_3+1][j_3]==0 and game[i_4+1][j_4]==0  :
							i_1+=1
							i_3+=1
							i_2+=1
							i_4+=1
						else :
							new_one=True
					else :
						new_one=True

			elif shape ==2 :
				if can_accel_left :
					if (j_1)>=1 :
						if game[i_1][j_1-1]==0 and game[i_2][j_1-1]==0 and game[i_3][j_1-1]==0 and game[i_4][j_1-1]==0 :
							j_1-=1
							j_3-=1
							j_2-=1
							j_4-=1
				if can_accel_right :
					if (j_4+1) <=21 : 	
						if game[i_2][j_4+1]==0 and game[i_1][j_4+1]==0 and game[i_3][j_4+1]==0 and game[i_4][j_4+1]==0 :
							j_1+=1
							j_3+=1
							j_2+=1
							j_4+=1
				if can_accel_down :
					if (i_1+4) < 20  :
						if game[i_1+4][j_1]==0   :
							i_1+=1
							i_3+=1
							i_2+=1
							i_4+=1
						else :
							new_one=True
					else :
						new_one=True
			elif shape ==3 :
				if can_accel_left :
					if (j_1)>=1 :
						if game[i_1][j_1-1]==0 and game[i_2][j_1-1]==0 and game[i_4][j_4-1]==0 :
							j_1-=1
							j_3-=1
							j_2-=1
							j_4-=1
				if can_accel_right :
					if (j_4+1) <=21 : 	
						if  game[i_1][j_4+1]==0 and game[i_3][j_4+1]==0 and game[i_4][j_4+1]==0 :
							j_1+=1
							j_3+=1
							j_2+=1
							j_4+=1
				if can_accel_down :
					if (i_4+1) < 20  :
						if game[i_4+1][j_4]==0 and game[i_2+1][j_2]==0   :
							i_1+=1
							i_3+=1
							i_2+=1
							i_4+=1
						else :
							new_one=True
					else :
						new_one=True
			elif shape ==4 :
				if can_accel_left :
					if (j_1)>=1 :
						if game[i_1][j_1-1]==0 and game[i_2][j_1-1]==0 and game[i_3][j_3-1]==0 :
							j_1-=1
							j_3-=1
							j_2-=1
							j_4-=1
				if can_accel_right :
					if (j_4+1) <=21 : 	
						if  game[i_3][j_3+1]==0 and game[i_4][j_4+1]==0 and game[i_2][j_2+1]==0 :
							j_1+=1
							j_3+=1
							j_2+=1
							j_4+=1
				if can_accel_down :
					if (i_2+1) < 20  :
						if game[i_2+1][j_2]==0 and game[i_4+1][j_4]==0   :
							i_1+=1
							i_3+=1
							i_2+=1
							i_4+=1
						else :
							new_one=True
					else :
						new_one=True
			game[i_1][j_1]=1
			game[i_2][j_2]=1
			game[i_3][j_3]=1
			game[i_4][j_4]=1
			time2=pygame.time.get_ticks()

		if pygame.time.get_ticks() > (time1+clock) :
			game[i_1][j_1]=0
			game[i_2][j_2]=0
			game[i_3][j_3]=0
			game[i_4][j_4]=0
			if shape==0 :
				if (i_1+1) < 19 and (i_2+1) < 19 :
					if game[i_1+2][j_1]==0 and game[i_2+2][j_2]==0  :
						i_1+=1
						i_3+=1
						i_2+=1
						i_4+=1
					else :
						new_one=True
				else :
					new_one=True
			elif shape==1 :
				if (i_1+1) < 20 :
					if game[i_1+1][j_1]==0 and game[i_2+1][j_2]==0 and game[i_3+1][j_3]==0 and game[i_4+1][j_4]==0 :
						i_1+=1
						i_3+=1
						i_2+=1
						i_4+=1
					else :
						new_one=True
				else :
					new_one=True
			elif shape==2 :
				if (i_1+4) < 20  :
					if game[i_1+4][j_1]==0   :
						i_1+=1
						i_3+=1
						i_2+=1
						i_4+=1
					else :
						new_one=True
				else :
					new_one=True
			elif shape==3 :
				if (i_4+1) < 20  :
					if game[i_4+1][j_4]==0 and game[i_2+1][j_2]==0   :
						i_1+=1
						i_3+=1
						i_2+=1
						i_4+=1
					else :
						new_one=True
				else :
					new_one=True
			elif shape==4 :
				if (i_2+1) < 20  :
					if game[i_2+1][j_2]==0 and game[i_4+1][j_4]==0   :
						i_1+=1
						i_3+=1
						i_2+=1
						i_4+=1
					else :
						new_one=True
				else :
					new_one=True

			game[i_1][j_1]=1
			game[i_2][j_2]=1
			game[i_3][j_3]=1
			game[i_4][j_4]=1
			time1=pygame.time.get_ticks()
		for i in range(20) :
			for j in range(22) :
				if game[i][j]==1 :
					left=(j*30)+1
					up=(i*30)+1
					pygame.draw.rect(screen,red,(left,up,29,29))
	if new_one :
		i_1=0
		i_2=0
		i_3=1
		i_4=1
		j_1=9
		j_2=10
		j_3=9
		j_4=10

		for i in range(20) :
			fills=True
			for j in range(22) :
				if game[i][j]==0 :
					fills=False
			if fills==True :
				score+=5
				clock-=25
				for j in range(22) :
					game[i][j]=0
					left=(j*30)+1
					up=(i*30)+1
					pygame.draw.rect(screen,black,(left,up,29,29))
				for k in range(i-1) :
					for j in range(22) :
						if game[i-k][j]==1 :
							game[i-k][j]=0
							game[i-k+1][j]=1

		for i in range(20) :
			for j in range(22) :
				if game[i][j]==1 :
					left=(j*30)+1
					up=(i*30)+1
					pygame.draw.rect(screen,red,(left,up,29,29))
		shape=(int(random.random()*100))%4









# Function to print paused game.

def print_paused_game() :
	font=pygame.font.Font(None,230)
	overText = font.render('Paused', True, white)
	overRect = overText.get_rect()
	overRect.centerx=(size[0]/2)
	overRect.centery=(size[1]/2)
	screen.blit(overText, overRect)
	print_press_any_key()

paused_game=False






# Initial screen.

pygame.init()
screen=pygame.display.set_mode(size,0,32)
pygame.display.set_caption("Nithin's Tetris Game")
draw_screen()
draw_initial_screen()
while True :
	if wait_for_any_key() :
		break
game_over=False






# Main game loop

while True :
	for event in pygame.event.get() :
		if event.type==pygame.QUIT :
			if paused_game :
				sys.exit()
				pygame.quit()
			game_over=True
			print_game_over()
			pygame.display.update()
			time3=pygame.time.get_ticks()
			while pygame.time.get_ticks() < (time3+1000) :
				pygame.time.get_ticks()
			sys.exit()
			pygame.quit()
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_ESCAPE :
				if paused_game==False :
					paused_game=True
					print_paused_game()
				else :
					paused_game=False
			if event.key == pygame.K_LEFT :
				 change_position('left',True)
			if event.key == pygame.K_RIGHT :
				 change_position('right',True)
			if event.key == pygame.K_DOWN :
				 change_position('down',True)
			if event.key == pygame.K_UP :
				 change_position('up',True)
		if event.type == pygame.KEYUP :
			if event.key == pygame.K_LEFT :
				 change_position('left',False)
			if event.key == pygame.K_RIGHT :
				 change_position('right',False)
			if event.key == pygame.K_DOWN :
				 change_position('down',False)
			if event.key == pygame.K_UP :
				 change_position('up',False)
	if game_over==False :
		if paused_game==False :
			draw_screen()
			play()
	else :
		if wait_for_any_key() :
			new_one=True
			i_1=0
			i_2=0
			i_3=1
			i_4=1
			j_1=9
			j_2=10
			j_3=9
			j_4=10
			can_accel_left=False
			can_accel_right=False
			can_accel_down=False
			can_change_shape=False
			time1=pygame.time.get_ticks()
			time2=pygame.time.get_ticks()
			shape=0
			score=0
			game_over=False
			clock=500
			for i in range(20) :
				for j in range(22) :
					game[i][j]=0
	pygame.display.update()
