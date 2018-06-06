# My first Pygame program.
# Authors: Many people and <John Paul Nolte>

import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("Shapes")

kpos = 10
zpos = 10
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        kpos = kpos + 10
    if pressed_keys[pygame.K_LEFT]:
        kpos = kpos - 10
    if pressed_keys[pygame.K_UP]:
        zpos = zpos - 10
    if pressed_keys[pygame.K_DOWN]:
        zpos = zpos + 10

    screen.fill((0, 167, 255))

    pygame.draw.circle(screen, (0, 10, 250, 50), (kpos, zpos), 50)

    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
