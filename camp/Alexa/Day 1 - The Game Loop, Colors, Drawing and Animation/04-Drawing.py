# My first Pygame program.
# Authors: Many people and Alexa, Aarna, and Madison

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((210, 2, 183))
    pygame.draw.circle(screen, (255, 0, 0), (100, 50), 30)
    pygame.draw.circle(screen, (166, 0, 0), (103, 50), 30)
    pygame.display.update()

# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
