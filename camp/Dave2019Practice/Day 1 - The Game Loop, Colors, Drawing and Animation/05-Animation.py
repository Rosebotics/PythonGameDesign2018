# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# My first Pygame program.
# Authors: Many people and David Fisher

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((234, 162, 123))
    pygame.display.update()


