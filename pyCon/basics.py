import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('man.png')
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())
        self.resting=False
        self.dy=0

    def update(self, dt, game):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt

        if self.resting and key[pygame.K_SPACE]:
        	self.dy = -500
        self.dy=min(400, self.dy+40)

        self.rect.y += self.dy * dt

        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect

            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
            	self.resting=True
            	new.bottom = cell.top
            	self.dy=0
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy=0

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        background = pygame.image.load('background.png')
        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        self.walls = pygame.sprite.Group()
        block = pygame.image.load('block.png')
        for x in range(0, 640, 10):
            for y in range(0, 480, 10):
                if x in (0, 640-10) or y in (0, 480-10):

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

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().main(screen)