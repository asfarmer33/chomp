import pygame
from pygame.locals import *
import sys

pygame.init()

HEIGHT = 600
WIDTH = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = pygame.time.Clock()

fish1 = pygame.image.load("images/fishTile_072.png").convert()
fish1x = 100
fish1y = 100

sand_height = 100


running = True

def moveFish()
    

while running:
    screen.fill((212, 241, 249))
    pygame.draw.rect(screen, (194, 178, 128), (0, HEIGHT-sand_height, WIDTH, sand_height))
    screen.blit(fish1,(100,100))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.flip()
    FPS.tick(60)