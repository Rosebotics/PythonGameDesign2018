# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied coimport pygame

import pygame
import sys
pygame.init()
pygame.display.set_caption("drawing")
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((234, 162, 223))

    #drawing shapes on the screen
    #big circle
    pygame.draw.circle(screen, (0, 125, 255), (320, 240), 200, 200)
    #left eye
    pygame.draw.circle(screen, (0, 255, 255), (240, 160), 66, 40)
    #rtight eye
    pygame.draw.circle(screen, (0, 255, 0), (400, 160), 66, 40)
    #nose
    pygame.draw.circle(screen, (255, 0, 0), (320, 240), 40, 20)
    #muoth
    pygame.draw.rect(screen, (0, 255, 255), (200,320,240,30))

    pygame.display.update()