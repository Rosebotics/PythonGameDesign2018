

# My first Pygame program.
# Authors: Many people and MichaelN

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

xpos = 50
ypos = 50
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
      #  print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 225, 0))
    pygame.draw.circle(screen,(0, 225, 225), (xpos, ypos), 30)
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
       xpos = xpos  -1
    if pressed_keys[pygame.K_RIGHT]:
       xpos = xpos  + 1
    pygame.draw.circle(screen, (0, 225, 225), (xpos, ypos), 30)
    pygame.display.update()
