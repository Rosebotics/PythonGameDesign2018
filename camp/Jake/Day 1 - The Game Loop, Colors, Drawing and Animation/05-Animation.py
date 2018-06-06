# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

import pygame
import sys

pygame.init()
pygame.display.set_caption('Animation')
screen = pygame.display.set_mode((720, 620))

clock = pygame.time.Clock()

nose_y_position = 310


while True:
    clock.tick(100)
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((175, 255, 255))

    # Draw shapes on the screen

    # Big Yellow circle
    pygame.draw.circle(screen, (250, 250, 0), (320, 240), 210)

    # Left Eye
    pygame.draw.circle(screen,(0, 0, 0), (240, 160), 25)

    # Right Eye
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25)

    # Nose
    nose_y_position = nose_y_position - 1
    pygame.draw.circle(screen, (255, 0, 0), (320, nose_y_position), 25, 20)
    if nose_y_position < 20:
        nose_y_position = 200


    # Mouth
    pygame.draw.rect(screen, (0,0,0),(200, 320, 200, 30))


    pygame.display.update()