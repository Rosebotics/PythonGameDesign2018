


# My first Pygame program. i like turtles
# Authors: Many people and <Ryland Hayes 62 127 255>

import pygame
import sys


pygame.init()
pygame.display.set_caption(" Detroit Lion Blue  ")
pygame.display.set_mode((640, 480))
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill( ( 75, 140,255) )
    pygame.display.update()
print('Hello World')


