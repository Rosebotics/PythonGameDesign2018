# My first Pygame program.
# Authors: Many people and <Albus Dumblydore and Villager#64>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

ypos = 450
clock = pygame.time.Clock()
pygame.display.set_caption("My Rising Sun")
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    ypos = ypos - 1
    screen.fill((255, 110, 80))
    pygame.draw.circle(screen, (220, 200, 10), (250, ypos), 220)
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
