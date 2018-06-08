# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("GameGame")

xpos = 50
kpos = 200
clock = pygame.time.Clock()
while True:
    clock.tick(0)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        kpos = kpos + 1
    if pressed_keys[pygame.K_LEFT]:
        kpos = kpos - 1
    print(pressed_keys)
   # kpos = kpos + 1
    xpos = xpos + 1
    screen.fill((0, 150, 255))
    pygame.draw. circle(screen, (255, 128, 0), (255, 130), 200)
    pygame.draw.circle(screen, (255, 255, 255), (140, 350), 200)
    pygame.draw.circle(screen, (255, 255, 255), (130, 130), 100)
    pygame.draw.rect(screen, (0, 0, 0), (kpos, 10, 150, 40))
    pygame.draw.rect(screen, (0, 0, 0), (90, 0, 90, 50))
    pygame.draw.circle(screen, (0, 0, 0), (100, 100), 10)
    pygame.draw.circle(screen, (0, 0, 0), (150, 100), 10)
    pygame.draw.circle(screen, (0, 0, 0), (170, 140), 7)
    pygame.draw.circle(screen, (0, 0, 0), (150, 150), 7)
    pygame.draw.circle(screen, (0, 0, 0), (130, 155), 7)
    pygame.draw.circle(screen, (0, 0, 0), (110, 150), 7)
    pygame.draw.circle(screen, (0, 0, 0), (90, 140), 7)
    pygame.draw.circle(screen, (255, 128, 0), (130, 130), 9)
    pygame.draw.rect(screen, (255, 255, 255), (0, 500, 1000, 600))
    pygame.draw.circle(screen, (0, 0, 0), (130, 220), 10)
    pygame.draw.circle(screen, (0, 0, 0), (130, 270), 10)
    pygame.draw.circle(screen, (0, 0, 0), (130, 320), 10)

    pygame.display.update()

