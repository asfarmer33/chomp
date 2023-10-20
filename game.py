import pygame
from pygame.locals import *
import sys
import helpers

pygame.init()

HEIGHT = 600
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = pygame.time.Clock()

green_fish = pygame.image.load("images/fishTile_072.png")

my_font = pygame.font.SysFont('Comic Sans MS', 50, True)
text = my_font.render('Seaworld', True, (0, 0, 0))

background = helpers.make_background(screen)





running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    helpers.center_surfaces(text, screen)

    pygame.display.set_caption(f"Chomp {FPS.get_fps():3.2f}")
    pygame.display.flip()
    FPS.tick(60)