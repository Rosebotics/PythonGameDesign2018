

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((150,0,150))
    pygame.draw.circle(screen,(9,250,218),(100,100),35)
    pygame.draw.circle(screen,(9,250,218),(200,200),35)
    pygame.draw.circle(screen,(9,250,218),(300,300),35)
    pygame.draw.circle(screen,(9,250,218),(400,400),35)
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
