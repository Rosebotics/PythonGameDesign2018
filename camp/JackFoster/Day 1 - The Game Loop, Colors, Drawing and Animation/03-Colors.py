# DONE: Copy all of your   02-TheGameLoop.py   program and put it below this comment.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((234, 162, 123.456789))
    pygame.display.update()