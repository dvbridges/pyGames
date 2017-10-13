#!/usr/bin/env python
import pygame, os, random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Note, vertices are (0,1,2,3,4,5,6,7). Positive x,y,z point right, up, backwards, respectively.

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
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	display = (1000,700)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(random.randrange(-5,5),random.randrange(-5,5), -50) # translate cube location
	glRotate(0,0,0,0) # Rotate cube
	x_move,y_move,z_move = 0,0,0
	move_inc = .3

	object_passed = False

	# Start Pygame event loop
	while not object_passed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_move=move_inc
				if event.key == pygame.K_RIGHT:
					x_move=-move_inc
				if event.key == pygame.K_UP:
					y_move=-move_inc
				if event.key == pygame.K_DOWN:
					y_move=move_inc
			if event.type == pygame.KEYUP:
				x_move,y_move,z_move = 0,0,0

		Cube_loc = glGetDoublev(GL_MODELVIEW_MATRIX) # get cube spatial locations
		camera_x = Cube_loc[3][0]
		camera_y = Cube_loc[3][1]
		camera_z = Cube_loc[3][2]
		glTranslatef(x_move,y_move, .6)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		pygame.display.flip()

		if camera_z <=0:
			object_passed = True

if __name__ == "__main__":
	for runs in range(10):
		main()
		glLoadIdentity()

