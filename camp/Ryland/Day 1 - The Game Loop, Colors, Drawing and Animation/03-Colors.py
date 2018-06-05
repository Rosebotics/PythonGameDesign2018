


# My first Pygame program.
# Authors: Many people and <Ryland Hayes 62 127 255>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill( ( 0, 0,0) )
    pygame.display.update()



