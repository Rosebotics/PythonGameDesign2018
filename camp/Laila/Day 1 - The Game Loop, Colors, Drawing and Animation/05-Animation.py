# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

xpos = 50
clock = pygame.time.Clock()
while True:
    clock.tick(1000000900000000000000000000000000000000000000000000000000000000000000000000)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    xpos = xpos + 1
    screen.fill((100, 140, 130))
    pygame.draw.circle(screen, (0, 100, 120), (xpos, 100), 45)

    pygame.draw.line(screen, (0, 0, 250), (50, 100), (200, 80))

    pygame.display.update()
