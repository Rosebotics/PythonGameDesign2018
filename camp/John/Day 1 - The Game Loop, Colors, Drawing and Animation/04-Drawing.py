# My first Pygame program.
# Authors: Many people and <John Paul Nolte>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 1200))

xpos = 50
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    xpos = xpos + 1
    screen.fill((0, 167, 255))
    pygame.draw.circle(screen, (0, 10, 250), (720,400), 100)
    pygame.draw.circle(screen, (0, 10, 250), (xpos,500), 57)
    pygame.draw.circle(screen, (0, 10, 250), (xpos, 160), 50)
    pygame.draw.circle(screen, (0, 10, 250), (500, 690), 200)
    pygame.draw.circle(screen, (0, 10, 250), (xpos, 200), 20)
    pygame.draw.circle(screen, (0, 10, 250), (xpos, 560), 10)
    pygame.draw.circle(screen, (0, 10, 250), (xpos, 270), 85)
    pygame.draw.circle(screen, (0, 10, 250), (xpos, 400), 27)
    pygame.draw.circle(screen, (0, 10, 250), (348, 500), 123)
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
