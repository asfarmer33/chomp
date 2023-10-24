import pygame


class Boat(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface((150, 50))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = 0
        self.velocity = -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.velocity


