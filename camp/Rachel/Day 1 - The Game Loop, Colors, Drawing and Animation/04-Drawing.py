# TODO: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  02-TheGameLoop.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

# My first Pygame program.
# Authors: Many people and Rachel

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
      print  ( event )
    if event . type == pygame.QUIT:
            sys.exit()
    pygame.display.update()

    screen.fill ((255,128,0,)   # Hot pink
    pygame.draw.circle(screen, (255,0 ,0 ) ,(100, 50),30)
    pygame.display.update ()
    pygame.draw.circle(screen, (255, 0, 0),(100, 50), 30)
    pygame.display.update ()
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
