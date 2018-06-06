# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
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
xpos = 14
screen = pygame.display.set_mode((690, 480))
clock=pygame.time.Clock()
while True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    xpos = xpos + 100
    screen.fill((244, 105, 180))  # Hot pink
    pygame.draw.circle(screen, (255, 255, 255,), (xpos, 255), 23)
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.