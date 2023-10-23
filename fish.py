import random
import pygame

class Fish():

    def __init__(self, screen):
        images = ["images/fishTile_079.png", "images/fishTile_081.png", "images/fishTile_075.png"]
        self.speed = random.random()*5
        self.x = screen.get_width()
        self.img = pygame.image.load(images[random.randint(0,2)])
        #self.img = pygame.image.load("images/fishTile_079.png")
        self.img = pygame.transform.flip(self.img, 1, 0)
        self.y = random.randint(0, screen.get_height() - self.img.get_height())
        self.screen = screen

    def update(self):
        if self.x < 0-self.img.get_width():
            self.x = self.screen.get_width()
            self.y = random.randint(0, self.screen.get_height()-self.img.get_height())
        self.x -= self.speed

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))