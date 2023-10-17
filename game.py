import pygame
from pygame.locals import *
import sys

pygame.init()

HEIGHT = 800
WIDTH = 600

screen = pygame.display.set_mode((HEIGHT,WIDTH))
FPS = pygame.time.Clock()

water = pygame.Surface((HEIGHT,WIDTH))

running = True

while running:
    pygame.Surface.fill(water,'blue')

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.flip()
    pygame.display.update()
    FPS.tick(60)