# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
clock = pygame.time.Clock()
nose_y_position = 240

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    clock.tick(600000000000000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        nose_y_position = 0
    screen.fill((0,147,180 ))

    #Draw shapes on the screen
    #Big yellow circle
    pygame.draw.circle(screen,(225,225, 0),(320, 240),210)
    #left eye
    pygame.draw.circle(screen,(0, 0, 0),(240,160),25)
    #right eye
    pygame.draw.circle(screen,(0, 0, 0),(400, 160), 25)
    #mouth
    pygame.draw.rect(screen, (100, 0, 0),(200, 320, 240, 30))
    #nose
    nose_y_position = nose_y_position + 1
    if nose_y_position > 400:
        nose_y_position = 200
    pygame.draw.circle(screen, (225, 0, 0),(320,nose_y_position), 20, 5)

    pygame.display.update()
