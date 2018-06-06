# My first Pygame program.
# Authors: Many people and Ginny Weasley

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
xpos = 50
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
      print  ( event )
    if event . type == pygame.QUIT:
        sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_Right]
            kpos = kpos + 1
            if pressed_keys [pygame.K_LEFT]:
                kpos = kpos - 1



    screen.fill ((255,128,0,))  # Hot pink
    pygame.draw.circle(screen, (255,0 ,0) ,(xpos, 50),30)
    pygame.display.update ()
    pygame.draw.circle(screen, (255, 0, 0),(100, 50), 30)
    pygame.display.update ()
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully
    #  TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
