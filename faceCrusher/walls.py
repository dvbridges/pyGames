import pygame
import time
import random

class Walls():
    def __init__(self, screen,wall_image='block.png',x_dimension=640, y_dimension=480, wall_size=5):
        clock = pygame.time.Clock()
        self.x_dimension=x_dimension
        self.y_dimension=y_dimension
        self.wall_size=wall_size
        self.walls = pygame.sprite.Group()
        self.wall_image=wall_image
        self.block = pygame.image.load(self.wall_image)
        self.sprites = pygame.sprite.Group()

    def drawWalls(self,screen):
        
        for x in range(0, self.x_dimension, self.wall_size):
            for y in range(0, self.y_dimension, self.wall_size):
                if x in (0, self.x_dimension-self.wall_size) or y in (0, self.y_dimension-self.wall_size):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = self.block
                    wall.rect = pygame.rect.Rect((x, y), self.block.get_size())
        return wall



