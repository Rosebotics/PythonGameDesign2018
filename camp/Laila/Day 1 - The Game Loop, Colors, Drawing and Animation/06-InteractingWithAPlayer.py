
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

xpos = 50
kpos = 200
clock = pygame.time.Clock()
while True:
    clock.tick(10000000000000000)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        kpos = kpos + 1
    if pressed_keys[pygame.K_LEFT]:
        kpos = kpos - 1

    xpos = xpos + 1
    screen.fill((100, 140, 130))
    pygame.draw.circle(screen, (0, 100, 120), (xpos, 100), 45)

    pygame.draw.line(screen, (0, 0, 250), (kpos, 100), (200, 80))

    pygame.display.update()
