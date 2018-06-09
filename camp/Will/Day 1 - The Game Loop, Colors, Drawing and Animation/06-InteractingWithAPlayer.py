# My first Pygame program.
# Authors: Many people and William Dorsey

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Will's moving objects")
xpos = 50
kpos = 200
clock = pygame.time.Clock()
while True:
    clock.tick(100)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        kpos = kpos + 1
    if pressed_keys[pygame.K_LEFT]:
        kpos = kpos - 1
    screen.fill((190, 50, 120))
    pygame.draw.rect(screen, (0, 0, 255), (kpos, 34, 200, 50))
    pygame.draw.circle(screen, (0, 255, 0), (kpos, 80), 90)
    pygame.display.update()