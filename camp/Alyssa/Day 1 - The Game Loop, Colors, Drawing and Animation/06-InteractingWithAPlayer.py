# TODO: Copy all of your   05-Animation.py   program and put it below this comment.


import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
xpos = 50
kpos=200
clock=pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys=pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
                kpos=kpos+1
    if pressed_keys[pygame.K_LEFT]:
                kpos=kpos-1



    screen.fill((150,0,150))
    pygame.draw.circle(screen,(9,250,218),(xpos,100),35)
    pygame.draw.circle(screen,(9,250,218),(200,200),35)
    pygame.draw.circle(screen,(9,250,218),(300,kpos),35)
    pygame.draw.circle(screen,(9,250,218),(400,400),35)
    pygame.display.update()
