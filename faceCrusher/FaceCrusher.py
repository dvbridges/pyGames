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

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('face.png')
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())
        self.rectmouth = pygame.rect.Rect((360, 270), (30,30))
        self.is_dead = False

    def update(self, dt, game):
        last = self.rect.copy()

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
        if key[pygame.K_DOWN]:
            self.rect.y += 300 * dt

        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last

class blocks(pygame.sprite.Sprite):
    def __init__(self, *groups):
    	super(blocks, self).__init__(*groups)
    	self.image=pygame.image.load("anvil.png")
    	self.rect=pygame.rect.Rect((200,-200),self.image.get_size())
    	self.rect.y=-200
    	self.rect.x=300

    def update(self,dt,game):
    	if dt and self.rect.y < 640:
    		self.rect.y += 300 * dt
    	else:
    		self.rect.y = -100
    		self.rect.x = random.randint(0,640)

    	if self.rect.colliderect(game.player.rect):
    		game.player.is_dead = True

class texts():
	def __init__(self):
		self.gameOver="CRUSHED!"
		self.red=(255,0,0)
		self.green=(0,255,0)
		self.blue=(0,0,255)

	def setFont(self,screen):
		fontObj=pygame.font.Font('freesansbold.ttf',64)
		textSurfaceObj = fontObj.render(self.gameOver,True,self.red)
		textRectObj=textSurfaceObj.get_rect()
		textRectObj.center = (320,150)
		screen.blit(textSurfaceObj,textRectObj)
		pygame.display.flip()


class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()
        gameover=texts()
        background = pygame.image.load('background.png')
        pygame.mixer.music.load("ColdasSteel.mp3")
        pygame.mixer.music.play()
        self.explosion = pygame.mixer.Sound('explosion.wav')
        
        sprites = pygame.sprite.Group()
        self.player = Player(sprites)
        self.block = blocks(sprites)

        self.walls = pygame.sprite.Group()
        block = pygame.image.load('block.png')
        for x in range(0, 640, 5):
            for y in range(0, 480, 5):
                if x in (0, 640-5) or y in (0, 480-5):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x, y), block.get_size())
        sprites.add(self.walls)

        while 1:
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            sprites.update(dt / 1000., self)
            screen.blit(background, (0, 0))
            sprites.draw(screen)
            pygame.display.flip()

            if self.player.is_dead:
            	self.player.image = pygame.image.load('deadface.png')
            	sprites.draw(screen)
            	pygame.display.flip()
            	
            	gameover.setFont(screen)
            	
            	channela=self.explosion.play()
            	while channela.get_busy():
            		pygame.time.delay(100)
            		time.sleep(2)
            		return

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((640, 480),pygame.FULLSCREEN)
    Game().main(screen)