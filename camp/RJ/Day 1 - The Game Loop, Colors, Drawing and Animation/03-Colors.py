# My first Pygame program.
# Authors: Many people and <Albus Dumblydore and Villager#64>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
             sys.exit()
    screen.fill((255, 25, 200))
    pygame.display.update()

#TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
