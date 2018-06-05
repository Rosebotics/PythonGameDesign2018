# TODO: Copy all of your   03-Colors.py   program and put it below this comment. done!!!!!
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

# My first Pygame program.
# Authors: Many people and <Ryland Hayes >

import pygame
import sys


pygame.init()
pygame.display.set_caption(" Anamation ")
pygame.display.set_mode((640, 480))
screen = pygame.display.set_mode((640, 480))


mouth_x_position = 265



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill( ( 75, 140,255) )
    # DRAW SHAPES ON THE SCREEN
    #print('Hello Worl')


    pygame.draw.circle(screen, (255, 255, 255),(200,200), 70, )
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 250, )
    pygame.draw.circle(screen, (0, 0, 0), (220, 120), 30, )
    pygame.draw.circle(screen, (0, 0, 0), (420, 120), 30, )
    pygame.draw.circle(screen, (175, 0, 0), (320, 220), 38, 18)
    pygame.draw.circle(screen, (225, 0, 0), (320, 220), 22, )
    pygame.draw.circle(screen, (250, 250, 250), (220, 120), 7, )
    pygame.draw.circle(screen, (250, 250, 250), (420, 120), 7, )
    #pygame.draw.circle(screen, (175, 0, 0), (320, 380), 90, 8)
    #pygame.draw.circle(screen, (0, 0, 0), (320, 380), 84, 0)


    pygame.draw.rect(screen, (0,0,0),       (200, 300, 270, 55))
    pygame.draw.rect(screen, (170, 0, 0), (200, 300, 270, 55), 8)

    pygame.display.update()


