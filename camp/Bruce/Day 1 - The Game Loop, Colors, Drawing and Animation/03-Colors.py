# done: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# done    One way to do so is:

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((2000, 2000))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((102, 205, 170))
    pygame.display.update()