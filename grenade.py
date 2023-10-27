import pygame
import math

class Grenade(pygame.sprite.Sprite):

    def __init__(self, screen, boat, fish_group):
        super().__init__()
        self.image = pygame.image.load("images/grenade.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.midtop = boat.rect.midbottom
        self.velocity = 2
        self.screen = screen
        self.boom_time = 0
        self.sound = pygame.mixer.Sound("sounds/explosion.wav")
        self.fish_group = fish_group

    def boom(self):
        if self.boom_time == 0:
            self.boom_time = pygame.time.get_ticks()
            self.kill_fish()
            self.sound.play()


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

    def kill_fish(self):
        # get location
        x_g, y_g = self.rect.center

        # loop over each fish in fish group
        for fish in self.fish_group:
            # get distance to fish
            x_f, y_f = fish.rect.center
            distance = math.sqrt((x_f-x_g)**2 + (y_f-y_g)**2)
            # if fish is close, kill it
            if distance < 60:
                fish.kill()
