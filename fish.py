import random
import pygame

class Fish(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        images = ["images/fishTile_079.png", "images/fishTile_081.png", "images/fishTile_075.png", "images/fishTile_077.png"]
        self.speed = random.random()*5
        self.image = pygame.image.load(images[random.randint(0,3)])
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = self.image.get_rect()
        self.x = screen.get_width()
        self.rect.x = self.x
        self.y = random.randint(100, screen.get_height() - self.image.get_height())
        self.rect.y = self.y
        self.screen = screen

    def update(self):
        if self.x < 0-self.image.get_width():
            self.x = self.screen.get_width()
            self.y = random.randint(200, self.screen.get_height()-self.image.get_height())
        self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y