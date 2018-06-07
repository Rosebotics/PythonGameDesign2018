# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys


pygame.init()
pygame.display.set_mode((640, 480))


nose_y_position = 240

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # big yellow circle
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)

    # left eye
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25)
    pygame.draw.circle(screen, (255, 255, 255), (240, 160), 25)