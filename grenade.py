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
        self.collision_radius = 30

    def boom(self):
        if self.boom_time == 0:
            self.boom_time = pygame.time.get_ticks()
            self.kill_fish()
            self.sound.play()


    def update(self):
        self.rect.y += self.velocity
        self.check_fish_hit()
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
        for fish in self.fish_group:

            if self.get_distance(self.rect.center, fish.rect.center) < 100:
                fish.skeleton()


    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return (self.get_distance(coord1, coord2) < self.collision_radius)


    def check_fish_hit(self):
        hit_fish_list = pygame.sprite.spritecollide(self, self.fish_group, False, collided=self.get_sprite_distance)
        if hit_fish_list:
            for fish in hit_fish_list:
                if fish.speed != 0:
                    self.boom()
        for fish in hit_fish_list:
                fish.skeleton()
