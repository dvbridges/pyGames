#!/usr/bin/env python3

# Script Name		: faceCrusher.py
# Author			: David Bridges
# Email				: david-bridges@hotmail.co.uk
# Created			: 10th November 2016
# Last Modified		: 10th October 2016
# Version			: 1.0
# Description		: A simple pyGame in development

import pygame
import time
import random


# First thing to do, is initialise pygame
pygame.init()

# Set window parameters
display_width = 800
display_height = 600

# Set colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


# Set window
gameDisplay=pygame.display.set_mode((display_width,display_height))

# Set title
pygame.display.set_caption("FaceCrusher")

# Set clock
clock=pygame.time.Clock()

# Load images

faceImg = pygame.image.load('face.png')#.convert()
pygame.mixer.music.load('ColdasSteel.mp3')
pygame.mixer.music.play()	

def Crushers(CrusherX, CrusherY,CrusherW,CrusherH,color):
	pygame.draw.rect(gameDisplay, color, [CrusherX,CrusherY, CrusherW, CrusherH])

def face(x,y):
	# Draw onto surface the face at x,y
	gameDisplay.blit(faceImg,(x,y))

def introTitle(switch, Text='FaceCrusher'):
	if switch == True:
		message_display(Text)
	return

def message_display(text):

	largeText=pygame.font.Font('freesansbold.ttf',60)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	


def text_objects(text,font):
	textSurface=font.render(text,True,red)
	return textSurface,textSurface.get_rect()






def game_loop():

	# Start location for face
	x=(display_width * .35)
	y=(display_height * .75)

	face_width=103
	face_height=70

	x_change=0
	y_change=0

	Crusher_startx=random.randrange(0,display_width)
	Crusher_starty=-600
	Crusher_speed=7
	Crusher_width = 100
	Crusher_height = 100

	gameExit=False
	IntroSwitch=True

	while not gameExit:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameExit=True

			# Set movement	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
					IntroSwitch=False
				elif event.key == pygame.K_RIGHT:
					x_change = 5	
					IntroSwitch=False
			# Stop movement 
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change=0

		x += x_change
			#print (event)

		# Create background
		gameDisplay.fill(white)

		Crushers(Crusher_startx,Crusher_starty,Crusher_width,Crusher_height,black)
		Crusher_starty+=Crusher_speed
		# Draw face
		face(x,y)

		# Set boundaries
		if x > display_width-face_width:
			x=display_width-face_width
		elif x < 0:
			x=0

		# Set falling blocks 
		if Crusher_starty > display_height:
			Crusher_starty=-600
			Crusher_startx=380#random.randrange(0,display_width)
		
		if y < (Crusher_starty+Crusher_height) and y+face_height > Crusher_starty:
			if x > Crusher_startx and x < Crusher_startx+Crusher_width or x+face_width > Crusher_startx and x+face_width < Crusher_startx+Crusher_width:
				introTitle(True, 'CRUSHED')

		# Set intro text
		introTitle(IntroSwitch)	
		
		# Update screen
		pygame.display.update()

		# Set frames per second
		clock.tick(60)

game_loop()
pygame.quit()
quit()