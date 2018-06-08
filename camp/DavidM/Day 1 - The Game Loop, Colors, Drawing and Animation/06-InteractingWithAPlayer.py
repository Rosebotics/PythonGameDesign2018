# My first Pygame program.
# Authors: Many people and Gandalf.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My moving objects")

xpos = 50
kpos = 200
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        kpos = kpos + 1
    if pressed_keys[pygame.K_LEFT]:
        kpos = kpos - 1

    screen.fill((255, 105, 180))  # Hot pink
    pygame.draw.circle(screen, (255, 0, 0), (xpos, 50), 30)
    pygame.draw.rect(screen, (0, 0, 0), (kpos, 300, 100, 50))
    pygame.display.update()
