import pygame

class Grenade(pygame.sprite.Sprite):

    def __init__(self, screen, boat):
        super().__init__()
        self.image = pygame.image.load("images/grenade.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.midtop = boat.rect.midbottom
        self.velocity = 2
        self.screen = screen
        self.boom_time = 0

    def boom(self):
        self.boom_time = pygame.time.get_ticks()


    def update(self):
        self.rect.y += self.velocity
        if self.boom_time:
            if pygame.time.get_ticks() - self.boom_time > 0:
                self.image = self.draw_image("images/explosion1.png")
            if pygame.time.get_ticks() - self.boom_time > 50:
                self.image = self.draw_image("images/explosion2.png")
            if pygame.time.get_ticks() - self.boom_time > 100:
                self.image = self.draw_image("images/explosion3.png")
            if pygame.time.get_ticks() - self.boom_time > 150:
                self.image = self.draw_image("images/explosion4.png")
            if pygame.time.get_ticks() - self.boom_time > 200:
                self.image = self.draw_image("images/explosion4.png")
            if pygame.time.get_ticks() - self.boom_time > 250:
                self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def hit_bottom(self):
        if self.rect.y > self.screen.get_height():
            self.kill()

    def draw_image(self, img):
        image = pygame.image.load(img)
        image = pygame.transform.scale(image, (40, 40))
        return image