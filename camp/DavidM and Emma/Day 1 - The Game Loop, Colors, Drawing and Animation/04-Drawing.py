# My first Pygame program.
# Authors: Many people and Gandalf.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((200, 155, 255))  # Hot pink
    #pygame.draw.circle(screen, (200, 155, 255), (300, 150), 100)
    #pygame.draw.rect(screen, (200, 155, 255), (0, 0, 400, 200))
    pygame.draw.polygon(screen, (111, 222, 212), [(7,6),(50,100),(100,50)], 6)
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
