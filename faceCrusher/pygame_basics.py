#!/usr/bin/env python3
# Pygame basics to set up window

import pygame

# First thing to do, is initialise pygame
pygame.init()

# Set window
gameDisplay=pygame.display.set_mode((800,600))

# Set title
pygame.display.set_caption("The Race")

# Set clock
clock=pygame.time.Clock()

crashed=False

while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed=True
		print (event)

	# Update screen
	pygame.display.update()

	# Set frames per second
	clock.tick(60)

pygame.quit()
quit()