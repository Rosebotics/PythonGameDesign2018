
import pygame
import sys

pygame.init()
pygame.display.set_caption('TETROMINO')
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((102, 205, 170))
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25)
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25)
    pygame.draw.circle(screen, (255, 0, 0), (320, 240), 25, 4)
    pygame.draw.rect(screen, (255, 255, 0), (280, 270, 240, 400))
    pygame.draw.rect(screen, (255, 0, 0), (200, 270, 240, 400))
    pygame.display.update()
