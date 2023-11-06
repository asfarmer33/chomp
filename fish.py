import random
import pygame

class Fish(pygame.sprite.Sprite):

    def __init__(self, screen, score):
        super().__init__()
        images = ["images/fishTile_079.png", "images/fishTile_081.png", "images/fishTile_075.png", "images/fishTile_077.png"]
        self.speed = random.random()*5
        self.randimg = random.randint(0,3)
        self.image = pygame.image.load(images[self.randimg])
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = self.image.get_rect()
        self.x = screen.get_width()
        self.rect.x = self.x
        self.y = random.randint(100, screen.get_height() - self.image.get_height())
        self.rect.y = self.y
        self.screen = screen
        self.dead_timer = 0
        self.deadspeed = 0
        self.score = score # list with one item

    def update(self):
        if self.x < 0-self.image.get_width():
            self.x = self.screen.get_width()
            self.y = random.randint(200, self.screen.get_height()-self.image.get_height())
        self.x -= self.speed
        self.y -= self.deadspeed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.dead_timer:
            opacity = (pygame.time.get_ticks() - self.dead_timer)/100
            self.image.set_alpha((1/opacity)*100)
        if self.dead_timer and pygame.time.get_ticks() - self.dead_timer > 800:
            self.kill()

    def skeleton(self):
        if self.speed != 0:
            dead_imgs = ["images/fishTile_097.png", "images/fishTile_099.png", "images/fishTile_093.png", "images/fishTile_095.png"]
            self.image = pygame.image.load(dead_imgs[self.randimg])
            self.image = pygame.transform.flip(self.image, 1, 1)
            self.dead_timer = pygame.time.get_ticks()
            self.speed = 0
            self.deadspeed = 1

            self.score[0] += 1

