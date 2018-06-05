
import pygame
import sys

pygame.init()
pygame.display.set_caption('My first Walter Melone')
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill ((2, 215, 15))
    pygame.display.update()
