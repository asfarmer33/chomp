import pygame
import random
import sys

def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    background = pygame.Surface((WIDTH, HEIGHT))
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
                background.blit(water_top_tile, (x, y))
            else:
                background.blit(water_tile, (x, y))

    # draw sand tiles
    for x in range(0, WIDTH, tile_width):
        for y in range(HEIGHT - tile_height*3, HEIGHT, tile_height):
            if y == HEIGHT - tile_height*3:
                background.blit(sand_top_tile, (x, y))
            else:
                random_num = random.randint(0,17)
                if random_num < 1:
                    background.blit(sand_shell_tile, (x, y))
                else:
                    background.blit(sand_bottom_tile, (x, y))

    # draw plants
    num_plants = 10
    for x in range(num_plants):
        plantx = random.randint(0, WIDTH - tile_width)
        planty = random.randint(HEIGHT - tile_height*4 + 20, HEIGHT - tile_height)
        background.blit(plant, (plantx, planty))

    return background


def center_surfaces(fs, bs):
    fg_width = fs.get_width()
    fg_height = fs.get_height()
    bg_width = bs.get_width()
    bg_height = bs.get_height()

    bs.blit(fs, (bg_width / 2 - fg_width / 2, bg_height / 2 - fg_height / 2))