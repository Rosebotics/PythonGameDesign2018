# TODO: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  02-TheGameLoop.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.
# My first Pygame program.
# Authors: Many people and <Samhita Shantharam>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

xpos = 50
kpos = 200
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type ==pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        kpos = kpos + 1
    if pressed_keys[pygame.K_LEFT]:
        kpos = kpos - 1
    xpos = xpos + 1
    screen.fill((121,254,255))
    pygame.draw.circle(screen, (243,33,12), (xpos,60),xpos)
    pygame.draw.circle(screen, (22,233,15), (540,480), 100)
    pygame.draw.rect(screen, (243,15,22),(100,52,100,50))
    pygame.draw.rect(screen, (243,15,22),(100,52,100,50))
    pygame.draw.arc(screen,(222,23,210),(100,40,200,50),50,70)
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.


