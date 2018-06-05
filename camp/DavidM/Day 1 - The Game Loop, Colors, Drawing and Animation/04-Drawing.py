# My first Pygame program.
# Authors: Many people and Gandalf.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 105, 180))  # Hot pink
    pygame.draw.circle(screen, (255, 0, 0), (100, 50), 30)
    pygame.draw.rect(screen, (0, 0, 0), (100, 300, 100, 50))
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
