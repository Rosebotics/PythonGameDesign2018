

# My first Pygame program.
# Authors: Many people and Michael Tanoos

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("A journey of 1000 miles begins with a single step.")

xpos = 50
ypos = 30
clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    xpos = xpos + 1
    ypos = ypos + 1
    screen.fill((25, 105, 5)) #Dark Green
    pygame.draw.circle(screen,(255, 200, 0),(167, ypos),50)
    # pygame.draw.ellipse(screen,(34, 89, 246),(12,78),34)
    pygame.draw.circle(screen,(35, 45, 78),(xpos,123),70)
    pygame.draw.rect(screen,(234, 78, 90),(40, 265, 378, 190),48)
    pygame.display.update()