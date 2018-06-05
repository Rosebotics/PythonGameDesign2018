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
pygame.display.set_caption("My first program")
screen = pygame.display.set_mode((1080, 720))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((234,123 , 245))

    pygame.draw.circle(screen, (255,255,0), (320,240), 210)
    pygame.draw.circle(screen, (0,0,0), (240,160 ),25)
    pygame.draw.circle(screen, (0, 0, 0), (400,160),25)
    pygame.draw.circle(screen, (0, 0, 0),(320,240),20,5 )

    pygame.draw.rect(screen, (100,0,0),     (200, 320, 240, 30))

    pygame.display.update()