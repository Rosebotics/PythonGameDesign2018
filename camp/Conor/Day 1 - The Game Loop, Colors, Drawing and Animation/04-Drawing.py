import pygame
import sys

pygame.init()
pygame.display.set_caption("Drawing")
screen = pygame.display.set_mode((900, 900))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((242,148,242))


    # Draw shapes on the screen.
    #Big yellow Circle
    pygame.draw.circle(screen, (255, 255, 225), (320, 240), 210)

    pygame.draw.circle(screen, (100, 100, 100), (240, 160), 55)

    pygame.draw.circle(screen, (100, 100, 100), (400, 160), 55)

    pygame.draw.circle(screen, (100, 100, 100), (320, 250), 50)
    # Mouth rect
    pygame.draw.rect(screen, (100, 0, 0), (200, 320, 240, 30))


    pygame.display.update()

