# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.
# TODO: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  02-TheGameLoop.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.
# My first Pygame program.
# Authors: Many people and <emmett>

import pygame
import sys
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get() :
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((244, 105, 180))  # blue
    pygame.draw.circle(screen, (255, 255, 255,), (255, 255), 110)
    pygame.display.update()
    pygame.display.update()
# TODO: With your instructor's help (live coding):camp/Emmet/Day 2 - Raindrops/00-TODOs.py:148
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
                                                                                                