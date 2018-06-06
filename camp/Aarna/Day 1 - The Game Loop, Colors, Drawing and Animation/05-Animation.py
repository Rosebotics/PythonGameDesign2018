# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
# My first Pygame program.
# Authors: Many people and Aarna

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My moving objects")

xpos = 50
kpos = 200
clock = pygame.Clock()
while True:
    clock.tick(1)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
         sys.exit()
         pressed_keys = pygame.get pressed()
                if pressed_keys[pygame.K_RIGHT]:
                    kpos = kpos + 1
        if pressed_keys[pygame.K_LEFT]
                    kpos = kpos - 1

    screen.fill((233, 99, 125))
    pygame.draw.circle(screen, (123,12,22), (xpos,xpos),37)
    pygame.draw.circle(screen, (233,66,35), (255,22),22)
    pygame.display.update()

# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.

