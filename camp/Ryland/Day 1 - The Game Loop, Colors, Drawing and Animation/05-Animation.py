# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys


pygame.init()
pygame.display.set_caption(" Anamation ")
pygame.display.set_mode((640, 480))
screen = pygame.display.set_mode((640, 480))


clock = pygame.time.Clock()
mouth_y_position = 300



while True:
    clock.tick(55)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill( ( 75, 140,255) )
    pygame.draw.circle(screen, (255, 255, 255),(200,200), 70, )
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 250, )
    pygame.draw.circle(screen, (0, 0, 0), (220, 120), 30, )
    pygame.draw.circle(screen, (0, 0, 0), (420, 120), 30, )
    pygame.draw.circle(screen, (175, 0, 0), (320, 220), 38, 18)
    pygame.draw.circle(screen, (225, 0, 0), (320, 220), 22, )
    pygame.draw.circle(screen, (250, 250, 250), (220, 120), 7, )
    pygame.draw.circle(screen, (250, 250, 250), (420, 120), 7, )

    mouth_y_position = mouth_y_position + 1
    if  mouth_y_position > 307:
        mouth_y_position = 293


    pygame.draw.rect(screen, (0, 0, 0),       (200, 300 , 270, 60))
    pygame.draw.rect(screen, (170, 0, 0),     (200,mouth_y_position , 270, 54), 20)

    pygame.display.update()
