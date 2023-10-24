import pygame

class Grenade(pygame.sprite.Sprite):

    def __init__(self, screen, boat):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill('black')
        self.rect = self.image.get_rect()
        self.rect.x = boat.rect.x
        self.rect.y = boat.rect.y + boat.rect.height
        self.velocity = 1
        self.screen = screen

    def boom(self):
        self.image.fill('red')


    def update(self):
        self.rect.y += self.velocity
        if self.rect.y > self.screen.get_height()/2:
            self.boom()

    def draw(self, screen):
        screen.blit(self.image, self.rect)