import pygame
from random import randint
from copy import deepcopy

#Technical specifications of the program, display resolution, tile size and framerate, window title and icon

pygame.display.set_caption("Conway's Game of Life by SJoseC")
ICON = pygame.image.load('conway_icon.jpg')
pygame.display.set_icon(ICON)
RES = WIDTH, HEIGHT = 1280, 720
TILE = 10
W, H= WIDTH // TILE, HEIGHT // TILE
FPS = 5

#Initial pygame function and main loop

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

NEXT_FIELD = [[0 for i in range(W)] for j in range(H)]
CURRENT_FIELD = [[randint(0,1) for i in range (W)] for i in range (H)]

#Cell-Checking function

def CHECK_CELL(CURRENT_FIELD, x, y):
    COUNT = 0
    for j in range(y - 1, y + 2):
      for i in range(x - 1, x + 2):
         if CURRENT_FIELD[j][i]:
            COUNT += 1

    if CURRENT_FIELD[y][x]:
      COUNT -= 1
      if COUNT == 2 or COUNT == 3:
          return 1
      return 0

    else:
       if COUNT == 3:
          return 1
       return 0


while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          exit()

    #Grid implementation
    [pygame.draw.line(surface, pygame.Color(10,10,10), (x, 0), (x, HEIGHT)) for x in range (0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color(10,10,10), (0, y), (WIDTH, y)) for y in range (0, HEIGHT, TILE)]

    #Draw of alive cells
    for x in range(1, W - 1):
       for y in range(1, H - 1):
         if CURRENT_FIELD[y][x]:
             pygame.draw.rect(surface, pygame.Color('gray'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
         NEXT_FIELD[y][x] = CHECK_CELL(CURRENT_FIELD, x, y)
       
    CURRENT_FIELD = deepcopy(NEXT_FIELD)

    pygame.display.flip()
    clock.tick(FPS)