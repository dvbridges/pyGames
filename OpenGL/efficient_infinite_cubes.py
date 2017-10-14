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

def Cube_color():
	"""
	Sets cube color
	"""
	surface_colors=[(random.random(),random.random(),random.random()) for x in range(12)]
	return surface_colors

def Cube_list(n, max_distance, min_distance):
	"""
	Cretes dictionary of n cubes
	"""
	cube_dict = {}
	for cubes in range(n):
		cube_dict[cubes]=set_vertices(max_distance, min_distance)
	return cube_dict

def set_vertices(max_distance, min_distance):
	"""
	Set vertices for each cube
	"""
	Cube_loc = glGetDoublev(GL_MODELVIEW_MATRIX) # get cube spatial locations
	camera_x = -1*int(Cube_loc[3][0])
	camera_y = -1*int(Cube_loc[3][1])
	distance = 20

	x_value_change = random.randrange(int(camera_x-distance),int(camera_x+distance))
	y_value_change = random.randrange(int(camera_y-distance),int(camera_y+distance))
	z_value_change = random.randrange(-1*max_distance,min_distance)
	new_vertices=[]
	for vert in vertices:
		new_x=vert[0]+x_value_change
		new_y=vert[1]+y_value_change
		new_z=vert[2]+z_value_change
		new_vertices.append((new_x,new_y,new_z))
	return new_vertices


def Cube(colors=Cube_color(),vertices=vertices):
	"""
	Create cubes
	"""
	glBegin(GL_QUADS)
	for surface in surfaces:
		# glColor3fv(surface_colors[surfaces.index(surface)]) ## colors based on face
		for vertex in surface:
			glColor3fv(colors[vertex]) # colours based on vertex
			glVertex3fv(vertices[vertex])
	glEnd()

	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

def move_cube(x_move,y_move, speed):
	"""
	Move cube based on user input
	"""
	Cube_loc = glGetDoublev(GL_MODELVIEW_MATRIX) # get cube spatial locations
	camera_x = Cube_loc[3][0]
	camera_y = Cube_loc[3][1]
	camera_z = Cube_loc[3][2]
	glTranslatef(x_move,y_move, speed)
	return camera_x,camera_y,camera_z

def main():#
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	display = (1000,700)
	max_distance=100
	min_distance=-10
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	pygame.display.toggle_fullscreen()
	gluPerspective(45, (display[0]/display[1]), 0.1, max_distance)
	glTranslatef(0,0, -50) # translate cube location
	glRotate(0,0,0,0) # Rotate cube
	x_move,y_move,z_move = 0,0,0
	move_inc = .3
	
	number_of_cubes=20
	cube_dict=Cube_list(number_of_cubes,max_distance,min_distance)

	# Start Pygame event loop
	while True:
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
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
			if event.type == pygame.KEYUP:
				x_move,y_move,z_move = 0,0,0

		camera_z=move_cube(x_move,y_move,2)[2]

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		# delete_list=[]
		for each_cube in cube_dict: #create cubes from dict
			Cube(vertices=cube_dict[each_cube])

		for each_cube in cube_dict: #reset distance of cube
			if camera_z <= cube_dict[each_cube][0][2]:
				cube_dict[each_cube]=set_vertices(int(-1*(camera_z-(max_distance*2))),int(camera_z-max_distance/2))

		pygame.display.flip()

		if camera_z <=0:
			object_passed = True
	

if __name__ == "__main__":
	for runs in range(10):
		main()
		glLoadIdentity()

