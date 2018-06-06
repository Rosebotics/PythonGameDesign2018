# TODO: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  02-TheGameLoop.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.
# My first Pygame program.
# Authors: Many people and <John Paul Nolte>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 1200))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 167, 255))
    pygame.draw.circle(screen, (0, 10, 250), (600,400), 100)
    pygame.draw.circle(screen, (0, 10, 250), (500,500), 57)
    pygame.draw.circle(screen, (0, 10, 250), (400, 160), 50)
    pygame.draw.circle(screen, (0, 10, 250), (600, 690), 200)
    pygame.draw.circle(screen, (0, 10, 250), (370, 200), 20)
    pygame.draw.circle(screen, (0, 10, 250), (482, 560), 10)
    pygame.draw.circle(screen, (0, 10, 250), (538, 270), 85)
    pygame.draw.circle(screen, (0, 10, 250), (580, 200), 27)
    pygame.draw.circle(screen, (0, 10, 250), (890, 500), 123)
    pygame.draw.circle(screen, (0, 10, 250), (810, 568), 60)
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
