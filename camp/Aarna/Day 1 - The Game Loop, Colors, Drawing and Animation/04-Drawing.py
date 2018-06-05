# My first Pygame program.
# Authors: Many people and <Aarna-Koduru>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((233, 99, 125))
    pygame.draw.circle(screen, (123,12,22), (24,56),37)
    pygame.draw.circle(screen, (233,66,35), (255,22),22)
    pygame.display.update()

# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
