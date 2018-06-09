# My first Pygame program.
# Authors: Many people and <Albus Dumblydore and Villager#64>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Rising Sun")

kpos = 200
ypos = 450
clock = pygame.time.Clock()

while True:
    clock.tick(25)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        kpos = kpos + 1
    if pressed_keys[pygame.K_LEFT]:
        kpos = kpos - 1
    screen.fill((255, 110, 80))
    pygame.draw.circle(screen, (220, 200, 10), (kpos, ypos), 220)  # Moderate Yellow Sun.
    pygame.draw.circle(screen, (255, 255, 255), (kpos, ypos), 5)  # small shine
    pygame.display.update()
