import pygame
from random import randint
from copy import deepcopy

#Technical specifications of the program, display resolution, tile size and framerate, window title and icon

pygame.display.set_caption("Conway's Game of Life by SJoseC")
ICON = pygame.image.load('conway_icon.jpg')
pygame.display.set_icon(ICON)
RES = WIDTH, HEIGHT = 1280, 720
TILE = 5
W, H= WIDTH // TILE, HEIGHT // TILE
FPS = 15

#Initial pygame function and main loop

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

NEXT_FIELD = [[0 for i in range(W)] for j in range(H)]
CURRENT_FIELD = [[randint(0,1) for i in range (W)] for i in range (H)]

while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          exit()

    #Grid implementation

    [pygame.draw.line(surface, pygame.Color(10,10,10), (x, 0), (x, HEIGHT)) for x in range (0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color(10,10,10), (0, y), (WIDTH, y)) for y in range (0, HEIGHT, TILE)]

    pygame.display.flip()
    clock.tick(FPS)