# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys

pygame.init()
pygame.display.set_caption("Animation")
screen = pygame.display.set_mode((640,480))

    clock = pygame.time.Clock()

nose_y_position = 240


while True:
    clock.tick(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((234,123 , 245))
    #Big Yellow Circle
    pygame.draw.circle(screen, (255,255,0), (320,240), 210)

    #Left Eye
    pygame.draw.circle(screen, (0,0,0), (240,160 ),25)

    #Right Eye
    pygame.draw.circle(screen, (0, 0, 0), (400,160),25)

    #Nose
    nose_y_position = nose_y_position+1
    if nose_y_position > 400:
        nose_y_position = 200
    pygame.draw.circle(screen, (0, 0, 0),(320,nose_y_position),20,5 )

    #Mouth
    pygame.draw.rect(screen, (100,0,0),     (200, 320, 240, 30))

    pygame.display.update()
