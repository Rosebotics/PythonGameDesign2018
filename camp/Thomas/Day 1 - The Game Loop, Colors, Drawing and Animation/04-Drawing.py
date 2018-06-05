import pygame
import sys

pygame.init()
pygame.display.set_caption('My first Walter Melone')
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((2, 215, 15))
    #draw shapes on the screen

    pygame.draw.circle(screen, (23, 29, 10), (321, 242), 360)
    pygame.draw.circle(screen, (23, 239, 10), (321, 242), 340, 40)
    pygame.draw.circle(screen, (223, 29, 10), (321, 242), 300, 40)
    pygame.draw.circle(screen, (23, 239, 110), (321, 242), 260, 40)
    pygame.draw.circle(screen, (243, 233, 10),(321, 242), 220, 40)
    pygame.draw.circle(screen, (255, 230, 130), (21, 242), 200, 40)
    pygame.draw.circle(screen, (23, 29, 255), (321, 242), 160, 40)
    pygame.draw.circle(screen, (242, 239, 255,), (321, 242), 140, 40)
    pygame.draw.circle(screen, (83, 239, 170,), (321, 242), 100, 40)
    pygame.display.update()