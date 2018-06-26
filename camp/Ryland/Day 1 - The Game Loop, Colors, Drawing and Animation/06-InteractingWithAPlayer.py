
import pygame
import sys


pygame.init()
pygame.display.set_caption(" Interactions ")
pygame.display.set_mode((640, 480))
screen = pygame.display.set_mode((640, 480))


clock = pygame.time.Clock()
mouth_y_position = 300
eye_y_position = 20


while True:
    clock.tick(55)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill( ( 75, 140,255) )
    pygame.draw.circle(screen, (255, 255, 255),(200,200), 70, )
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 250, )


    pygame.draw.circle(screen, (0, 0, 0), (220, 120), 30)
    pygame.draw.circle(screen, (0, 0, 0), (420, 120), 30)



    eye_y_position = eye_y_position + 1
    if eye_y_position > 121:
        eye_y_position = 50
    pygame.draw.circle(screen, (255, 255, 0), (220, eye_y_position), 31 )
    pygame.draw.circle(screen, (255, 255, 0), (420, eye_y_position), 31)







    pygame.draw.circle(screen, (175, 0, 0), (320, 220), 38, 18)
    pygame.draw.circle(screen, (225, 0, 0), (320, 220), 22, )
    #pygame.draw.circle(screen, (150, 150, 150), (220, 120), 7, )
    #pygame.draw.circle(screen, (150, 150, 150), (420, 120), 7, )

    mouth_y_position = mouth_y_position + 1
    if  mouth_y_position > 307:
        mouth_y_position = 293

    #pygame.draw.circle(screen, (150, 150, 150), (220, 120), 7, )
    #pygame.draw.circle(screen, (150, 150, 150), (420, 120), 7, )
    pygame.draw.rect(screen, (0, 0, 0),       (200, 300 , 270, 60))
    pygame.draw.rect(screen, (170, 0, 0),     (200,mouth_y_position , 270, 54), 20)

    pygame.display.update()
