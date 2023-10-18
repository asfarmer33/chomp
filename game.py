import pygame
from pygame.locals import *
import sys
import random

pygame.init()

HEIGHT = 600
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = pygame.time.Clock()

green_fish = pygame.image.load("images/fishTile_072.png")

def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    water_tile = pygame.image.load("images/fishTile_089.png")
    water_top_tile = pygame.image.load("images/fishTile_088.png")
    sand_bottom_tile = pygame.image.load("images/fishTile_001.png")
    sand_top_tile = pygame.image.load("images/fishTile_021.png")
    sand_shell_tile = pygame.image.load("images/fishTile_018.png")
    plant = pygame.image.load("images/fishTile_028.png")


    # draw water tiles
    tile_width = water_tile.get_width()
    tile_height = water_tile.get_height()
    for x in range(0, WIDTH, tile_width):
        for y in range(0, HEIGHT, tile_height):
            if y == 0:
                screen.blit(water_top_tile, (x, y))
            else:
                screen.blit(water_tile, (x, y))

    # draw sand tiles
    for x in range(0, WIDTH, tile_width):
        for y in range(HEIGHT - tile_height*3, HEIGHT, tile_height):
            if y == HEIGHT - tile_height*3:
                screen.blit(sand_top_tile, (x, y))
            else:
                random_num = random.randint(0,17)
                if random_num < 1:
                    screen.blit(sand_shell_tile, (x, y))
                else:
                    screen.blit(sand_bottom_tile, (x, y))

    # draw plants
    num_plants = 10
    for x in range(num_plants):
        plantx = random.randint(0, WIDTH - tile_width)
        planty = random.randint(HEIGHT - tile_height*4 + 20, HEIGHT - tile_height)
        screen.blit(plant, (plantx, planty))



make_background(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption(f"Chomp {FPS.get_fps():3.2f}")
    pygame.display.flip()
    FPS.tick(60)