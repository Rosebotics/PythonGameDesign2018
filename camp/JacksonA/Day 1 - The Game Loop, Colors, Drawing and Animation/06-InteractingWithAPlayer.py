# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
pygame.init()
pygame.display.set_caption("interactions")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

nose_y_position =240

while True:
    clock.tick(95)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:

        nose_y_position=0

    screen.fill((110,11,112))



    pygame.draw.circle(screen, (255,255,0),(320,240),210, )
    pygame.draw.circle (screen,(0,0,0 ),(240,160),25,  )
    pygame.draw.circle( screen,(0,0,0),(400,160),25,  )
    if nose_y_position ==400:
        nose_y_position =199
    nose_y_position=nose_y_position+1
    pygame.draw.circle(screen, (255,0,0),(320,nose_y_position),20, 4)
    pygame.draw.rect(screen,(100,0,0), (200,320,240,30))
    pygame.display.update()