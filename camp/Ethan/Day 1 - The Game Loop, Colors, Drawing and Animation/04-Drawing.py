# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,147,180 ))

    #Draw shapes on the screen

    #Big yellow circle
    pygame.draw.circle(screen,(225,225, 0),(320, 240),210)
    pygame.draw.circle(screen,(0, 0, 0),(240,160),)
    pygame.draw.circle(screen,(0, 0, 0),)
    pygame.draw.circle(screen, (225, 225, 0),(320,240), 50, 5)
    pygame.draw.circle(screen, (0, 225, 225), (320, 240),20)
    pygame.display.update()
