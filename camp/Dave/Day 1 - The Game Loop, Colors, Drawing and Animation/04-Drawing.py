import pygame
import sys

pygame.init()
pygame.display.set_caption("Drawing")
screen = pygame.display.set_mode((600, 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((153, 51, 102))

    # Draw shapes on the screen
    pygame.draw.circle(screen, (225, 255, 0), (300,300), 300, 10)
    pygame.draw.circle(screen, (0, 0, 0), (150,150), 10, 10)
    pygame.draw.circle(screen, (0, 0, 0), (450,150), 10, 10)
    pygame.draw.circle(screen, (255, 0, 0), (300, 250), 25, 5)
    pygame.draw.circle(screen, (255, 0, 0), (300, 250), 25, 5)
    pygame.draw.rect(screen, (204, 0, 0), (200, 400, 200, 100))

    pygame.display.update()

