import pygame
from pygame.locals import *
import sys
import random
from helpers import *
from fish import *
from boat import Boat
from grenade import Grenade

pygame.init()

HEIGHT = 600
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = pygame.time.Clock()

score = [0]

my_font = pygame.font.SysFont('Comic Sans MS', 50, True)
text = my_font.render('Seaworld', True, (0, 0, 0))

score_font = pygame.font.SysFont('Comic Sans MS', 20, True)

background = make_background(screen)

# fish group
fish_group = pygame.sprite.Group()
# add fish to group
num_fish = 30
[fish_group.add(Fish(screen, score)) for n in range(num_fish)]

# make boat
my_boat = Boat(screen)
boat_group = pygame.sprite.Group()
boat_group.add(my_boat)

# make grenade
grenade_group = pygame.sprite.Group()



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                my_boat.velocity += 1
            if event.key == pygame.K_LEFT:
                my_boat.velocity -= 1
            if event.key == pygame.K_DOWN:
                if len(grenade_group) < 4:
                    grenade_group.add(Grenade(screen, my_boat, fish_group))
            if event.key == pygame.K_SPACE:
                [grenade.boom() for grenade in grenade_group]


    if len(fish_group) < num_fish:
        for n in range(num_fish - len(fish_group)):
            fish_group.add(Fish(screen, score))


            # updates
    fish_group.update()
    boat_group.update()
    grenade_group.update()

    [grenade.hit_bottom() for grenade in grenade_group]

    # draw background
    screen.blit(background, (0, 0))
    if pygame.time.get_ticks() < 3000:
        center_surfaces(text, screen)

    score_text = my_font.render(f"{score[0]}", True, (255, 255, 255))
    screen.blit(score_text, (0, 0))


    # draw
    fish_group.draw(screen)
    boat_group.draw(screen)
    grenade_group.draw(screen)


    pygame.display.set_caption(f"Chomp {FPS.get_fps():3.2f} --------- Score: {score[0]}")
    pygame.display.flip()
    FPS.tick(60)