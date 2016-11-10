#!/usr/bin/env python3
# Pygame basics to set up window

import pygame

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
pygame.display.set_caption("The Race")

# Set clock
clock=pygame.time.Clock()

# Load images

faceImg = pygame.image.load('face.png')

def face(x,y):
	# Draw onto surface the face at x,y
	gameDisplay.blit(faceImg,(x,y))

# Start location for face
x=(display_width * .35)
y=(display_height * .75)

x_change=0
y_change=0

crashed=False

while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed=True

		# Set movement	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5	

		# Stop movement 
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change=0

	x += x_change
		#print (event)

	# Create background
	gameDisplay.fill(white)

	# Draw face
	face(x,y)

	# Update screen
	pygame.display.update()

	# Set frames per second
	clock.tick(60)

pygame.quit()
quit()