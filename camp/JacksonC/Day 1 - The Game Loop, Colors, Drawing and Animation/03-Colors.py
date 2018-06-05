# done: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# done:    One way to do so is:
# done     1. Inside  02-TheGameLoop.py,  do:
# done           -- Control-A (to SELECT the entire contents of the file, then
# done           -- Control-C (to COPY that entire selection)
# done     2. Inside this file:
# done          -- Click below this comment, then
# done          -- Control-V (to PASTE the copied code into this file.
import pygame
import sys

pygame.init()
pygame.display.set_caption("my first program")
screen = pygame.display.set_mode((640, 480))
while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
     screen.fill((234, 162, 123.456789))
     pygame.display.update()