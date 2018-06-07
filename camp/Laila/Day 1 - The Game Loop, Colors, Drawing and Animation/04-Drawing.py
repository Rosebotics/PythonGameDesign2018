
# My first Pygame program.
# Authors: Many people and <laila holman>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((100,140,130))
    pygame.draw.circle(screen, (0,100,120),(100,100), 45)
    pygame.draw.line(screen, (0,0,250), (50,100), (200,80))


    pygame.display.update()


