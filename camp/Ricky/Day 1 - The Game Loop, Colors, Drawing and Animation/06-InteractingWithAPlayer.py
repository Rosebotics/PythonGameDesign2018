# TODO: Copy all of your   05-Animation.py   program and put it below this comment.


import pygame
import sys

pygame.init()
pygame.display.set_caption('doodle')
screen = pygame.display.set_mode((640, 480))
nose_y_position = 240
clock = pygame.time.Clock()

while True:
    clock.tick(600)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
            nose_y_position = 0
    screen.fill((174, 214, 241))
    if nose_y_position > 400:
        nose_y_position = 200

    # draw
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)
    pygame.draw.circle(screen, (0, 0, 0), (430, 150), 50)
    pygame.draw.circle(screen, (0, 0, 0), (210, 150), 50)
    nose_y_position = nose_y_position + 1
    pygame.draw.circle(screen, (255, 0, 0), (320, nose_y_position), 20, 5)

    pygame.draw.rect(screen,(100, 0, 0),(200, 320, 240, 30))
    pygame.display.update()