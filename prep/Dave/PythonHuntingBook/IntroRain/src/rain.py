import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Rain")
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

rain_y = 0
rain_x = random.randint(0, 800)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 255, 100))
    rain_y += 4
    pygame.draw.line(screen, (0, 0, 0), (rain_x, rain_y), (rain_x, rain_y + 5), 1)

    pygame.display.update()