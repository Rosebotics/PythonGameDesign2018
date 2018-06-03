# This continues the previous module.
# Students will copy their previous code into their version of this module.
# Students will then start with something like the following:


# My first Pygame program.
# Authors: Many people and <PUT-YOUR-NAME-HERE>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 105, 180))  # Hot pink
    pygame.draw.circle(screen, (0, 0, 0), (100, 150), 20)
    pygame.draw.circle(screen, (255, 255, 0), (200, 350), 50)
    pygame.draw.rect(screen, (0, 0, 255), (20, 40, 100, 40), 5)
    pygame.display.update()