import pygame


class Boat(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.imageL = pygame.image.load("images/ship.png")
        self.imageL = pygame.transform.scale(self.imageL, (150, 90))
        self.imageR = pygame.transform.flip(self.imageL, 1, 0)
        self.image = self.imageL
        self.rect = self.imageL.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = 0
        self.velocity = -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.velocity
        if self.velocity <= 0:
            self.image = self.imageL
        else:
            self.image = self.imageR


