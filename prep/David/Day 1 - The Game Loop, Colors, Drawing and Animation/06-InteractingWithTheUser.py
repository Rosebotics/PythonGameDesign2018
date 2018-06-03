# This continues the previous module.
# Students will copy their previous code into their version of this module.
# Students will then start with something like the following:


# My first Pygame program.
# Authors: Many people and <PUT-YOUR-NAME-HERE>

import pygame
import sys

pygame.init()
pygame.display.set_caption("My First Game")
screen = pygame.display.set_mode((640, 480))

xpos = 50
xpos2 = 500
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    xpos = xpos + 1
    xpos2 = xpos2 - 5
    screen.fill((255, 105, 180))  # Hot pink
    pygame.draw.circle(screen, (0, 0, 0), (100, 150), 20)
    pygame.draw.circle(screen, (255, 255, 0), (xpos, 350), 50)
    pygame.draw.rect(screen, (0, 0, 255), (xpos2, 40, 100, 40), 5)
    pygame.display.update()