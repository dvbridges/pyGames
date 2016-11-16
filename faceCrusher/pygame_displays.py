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

crashed=False

while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed=True
		print (event)

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