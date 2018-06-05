
# My first Pygame program.
# Authors: Many people and Michael Tanoos

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((25, 105, 5)) #Dark Green
    pygame.draw.circle(screen,(255, 200, 0),(167, 412),50)
    # pygame.draw.ellipse(screen,(34, 89, 246),(12,78),34)
    pygame.draw.circle(screen,(35, 45, 78),(478,123),70)
    pygame.draw.rect(screen,(234, 78, 90),(40, 265, 378, 190),48)
    pygame.display.update()

