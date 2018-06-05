# My first Pygame program.
# Authors: Many people and Gandalf.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My moving objects")

xpos = 50
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    xpos = xpos + 1
    screen.fill((255, 105, 180))  # Hot pink
    pygame.draw.circle(screen, (255, 0, 0), (xpos, 50), 30)
    pygame.draw.rect(screen, (0, 0, 0), (100, 300, 100, 50))
    pygame.display.update()
