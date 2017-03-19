#!/usr/bin/env python3

# Script Name		: faceEater.py
# Author			: David Bridges
# Email				: david-bridges@hotmail.co.uk
# Created			: 10th November 2016
# Last Modified		: 2th November 2016
# Version			: 1.0
# Description		: A simple pyGame in development

import pygame
import time
import random
from TextDisplays import Text

 # Next step - use food choices to determine reaction and animation e.g., bad > good = bad reaction

class Player(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super(Player, self).__init__(*groups)
		self.image = pygame.image.load('face.png')
		self.rect = pygame.rect.Rect((320, 240), self.image.get_size())
		self.rectmouth = pygame.rect.Rect((360, 270), (30,30))
		self.is_dead = False
		self.points=0
		self.rageCount=0

	def update(self, dt, game):
		last = self.rect.copy()
		last_mouth = self.rectmouth.copy()
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			self.rect.x -= 300 * dt
			self.rectmouth.x-=300 * dt
			self.image = pygame.image.load('face.png')
		if key[pygame.K_RIGHT]:
			self.rect.x += 300 * dt
			self.rectmouth.x+=300 * dt
			self.image = pygame.image.load('face_right.png')
		if key[pygame.K_UP]:
			self.rect.y -= 300 * dt
			self.rectmouth.y-=300 * dt
		if key[pygame.K_DOWN]:
			self.rect.y += 300 * dt
			self.rectmouth.y+=300 * dt
		for cell in pygame.sprite.spritecollide(self, game.walls, False):
			self.rect = last
			self.rectmouth = last_mouth

	def rageFace(self,game,score):
		if self.rageCount==1 and not score:
			game.rage.play()
			game.player.image=pygame.image.load('face_rage.png')
			return 2000 # waitTime
		elif score:
			return 0


class blocks(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super(blocks, self).__init__(*groups)

		# Food lists
		self.goodFood = ['cherry.png','banana.png']
		self.badFood = ['burger.png','fries.png']
		self.foodList = [self.goodFood, self.badFood]
		
		# Food counters
		self.badEaten = 0
		self.goodEaten = 0

		# Image presentation
		self.currentFood = "burger.png"
		self.image=pygame.image.load(self.currentFood)
		self.rect=pygame.rect.Rect((200,-200),self.image.get_size())
		self.rect.y=-200
		self.rect.x=300

	def update(self,dt,game):
		if dt and self.rect.y < 640:
			self.rect.y += 300 * dt

		else:
			self.rect.y = -100
			self.rect.x = random.randint(10,630)
			self.selectFood()
		game.player.points=0

		if self.rect.colliderect(game.player.rect):
			game.player.image = pygame.image.load('face_eat.png')
			if self.rect.colliderect(game.player.rectmouth):
				game.gulp.play()
				game.player.points+=1
				self.rect.y = -100
				self.rect.x = random.randint(10,630)
				self.foodCounter(self.currentFood)
				self.currentFood=self.selectFood()
				return game.player.points 
				#game.player.is_dead = True

	def selectFood(self):
		foodType = random.randrange(0,2,1)
		food = blocks().foodList[foodType]
		random.shuffle(food)
		self.image=pygame.image.load(food[0])
		return food[0]
   
	def foodCounter(self,foodType):
		if foodType in self.badFood:
			self.badEaten+=1
		else:
			self.goodEaten+=1
		


class texts(Text):
	def __init__(self, message="Message here",font="Purisa.ttf",font_size = 24,font_location=(320,240), font_color=(255,0,0),screen=None):
		super(texts,self).__init__(message="Message here",font="Purisa.ttf",font_size = 24,font_location=(320,240), font_color=(255,0,0),screen=None)
		self.message = message
		self.font = font
		self.font_size = font_size
		self.font_location=font_location
		self.font_color=font_color
		self.score = 0

	def setScore(self,screen,counter):
		self.score+=counter
		fontObj=pygame.font.SysFont(self.font,self.font_size)
		textSurfaceObj = fontObj.render(str(self.score),True,self.font_color)
		textRectObj=textSurfaceObj.get_rect()
		textRectObj.center = (610,30)
		screen.blit(textSurfaceObj,textRectObj)
		pygame.display.flip()

class Game():

	def __init__(self):
		self.sprites = pygame.sprite.Group()
		self.player = Player(self.sprites)
		self.block = blocks(self.sprites)
		self.walls = pygame.sprite.Group()
		self.gulp = pygame.mixer.Sound('gulp_x.wav')
		self.rage = pygame.mixer.Sound('rage.wav')

	def main(self, screen):

		clock = pygame.time.Clock()
		gameover = texts(message="CRUSHED!", font_size = 60)
		score = texts(font_size=40)
		background = pygame.image.load('background.png')
		pygame.mixer.music.load("ColdasSteel.mp3")
		pygame.mixer.music.play()
		block = pygame.image.load('block.png')
		
		for x in range(0, 640, 5):
			for y in range(0, 480, 5):
				if x in (0, 640-5) or y in (0, 480-5):
					wall = pygame.sprite.Sprite(self.walls)
					wall.image = block
					wall.rect = pygame.rect.Rect((x, y), block.get_size())
		self.sprites.add(self.walls)

		while 1:
			dt = clock.tick(30)
			intro = texts()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					gameover.drawText(screen)
					pygame.time.wait(1000)
					return       

			if self.player.points == 1:
				score.setScore(screen,1)
				self.player.points=0
			if score.score != 0 and not score.score%10:
				try: 
					waitTime = self.player.rageFace(self,score.score%10)
					self.player.rageCount+=1
					self.sprites.draw(screen)
					pygame.display.flip()
					pygame.time.wait(waitTime)
					print(self.block.badEaten)
				except TypeError as e:
					pass
			else:
				self.player.rageCount=0

			self.sprites.update(dt / 1000., self)
			screen.blit(background, (0, 0))
			self.sprites.draw(screen)
			score.setScore(screen,0)
			pygame.display.flip()

			# if self.player.is_dead:
			# 	self.player.image = pygame.image.load('deadface.png')
			# 	sprites.draw(screen)
			# 	pygame.display.flip()
				
			# 	gameover.drawText(screen)
				
			# 	channela=self.explosion.play()
			# 	while channela.get_busy():
			# 		pygame.time.delay(100)
			# 		time.sleep(2)
			# 		return

if __name__ == '__main__':
	pygame.init()
	pygame.mixer.init()
	pygame.mouse.set_visible(False)
	screen = pygame.display.set_mode((640, 480),pygame.FULLSCREEN)
	Game().main(screen)