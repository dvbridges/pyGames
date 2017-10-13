#!/usr/bin/env python
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Note, vertices are (A,B,C,D,E,F,G,H) or (0,1,2,3,4,5,6,7). Positive x,y,z point right, up, backwards, respectively.

vertices = (
	(1,-1,1),
	(-1,-1,1),
	(-1,1,1),
	(1,1,1),
	(1,-1,-1),
	(-1,-1,-1),
	(-1,1,-1),
	(1,1,-1),)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,6),
	(5,1),
	(5,4),
	(5,6),
	(7,3),
	(7,4),
	(7,6))

surfaces = (
	(0,1,2,3),
	(1,2,6,5),
	(0,3,7,4),
	(0,1,5,4),
	(2,3,7,6),
	(4,5,6,7),
	)

surface_colors = (
	(.5,1,1),
	(1,.1,0),
	(1,0,1),
	(0,0,.5),
	(0,1,1),
	(1,0.5,1),
	(.5,1,1),
	(1,1,0),
	(1,0,1),
	(0,0,1),
	(0,1,1),
	(1,0.5,1),
	)

def Cube():

	glBegin(GL_QUADS)
	for surface in surfaces:
		# glColor3fv(surface_colors[surfaces.index(surface)]) ## colors based on face
		for vertex in surface:
			glColor3fv(surface_colors[vertex]) # colours based on vertex
			glVertex3fv(vertices[vertex])
	glEnd()


	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

def main():
	pygame.init()
	display = (1000,700)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0.0,0.0, -10)
	glRotate(15,3,3,2)
	x,y,z = .1,.1,.1 # movement increments
	# Start Pygame event loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-x,0,0)
				if event.key == pygame.K_RIGHT:
					glTranslatef(x,0,0)
				if event.key == pygame.K_UP:
					glTranslatef(0,y,0)
				if event.key == pygame.K_DOWN:
					glTranslatef(0,-y,0)
			# Add zoom
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,z)
				if event.button == 5:
					glTranslatef(0,0,-z)
		# glRotate(1,3,3,2)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		pygame.display.flip()
		pygame.time.wait(10)
	


if __name__ == "__main__":
	main()
