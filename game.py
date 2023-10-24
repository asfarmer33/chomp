import pygame
from pygame.locals import *
import sys
import random
from helpers import *
from fish import *

pygame.init()

HEIGHT = 600
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = pygame.time.Clock()

player_fish = pygame.image.load("images/fishTile_077.png")

my_font = pygame.font.SysFont('Comic Sans MS', 50, True)
text = my_font.render('Seaworld', True, (0, 0, 0))

background = make_background(screen)

# fish group
fish_group = pygame.sprite.Group()
# add fish to group
num_fish = 100
[fish_group.add(Fish(screen)) for n in range(num_fish)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # update fish
    fish_group.update()

    # draw background
    screen.blit(background, (0, 0))
    center_surfaces(text, background)
    # draw fish
    fish_group.draw(screen)


    pygame.display.set_caption(f"Chomp {FPS.get_fps():3.2f}")
    pygame.display.flip()
    FPS.tick(60)