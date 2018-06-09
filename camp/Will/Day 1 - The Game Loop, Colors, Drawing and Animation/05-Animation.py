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
# Authors: Many people and William Dorsey

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption()
xpos = 50
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            sys.exit()
        xpos = xpos + 1
    screen.fill((190, 50, 120))  #Hot Pink
    pygame.draw.rect(screen, (0, 0, 255), (xpos, 90, 200, 50))
    pygame.draw.circle(screen, (0, 255, 0), (xpos, 80), 25)
    pygame.display.update()

# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
