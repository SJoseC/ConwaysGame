import pygame
from random import randint
from copy import deepcopy

#Technical specifications of the program, display resolution, tile size and framerate

RES = WIDTH, HEIGHT = 1280, 720
TILE = 50
FPS = 15

#Initial pygame function and main loop

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          exit()

    #Grid implementation

    [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range (0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range (0, HEIGHT, TILE)]

    pygame.display.flip()
    clock.tick(FPS)