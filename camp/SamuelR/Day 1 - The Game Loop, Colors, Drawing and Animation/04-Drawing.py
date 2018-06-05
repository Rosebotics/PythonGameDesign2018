
import pygame
import sys

pygame.init()
pygame.display.set_caption('drawing')
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((128, 0, 128))

    # Big yellow Circle
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)

    # Left Eye
    pygame.draw.circle(screen, (255, 255, 255), (240, 160), 60)
    pygame.draw.circle(screen, (0, 0, 255), (240, 160), 40)

    # Right Eye
    pygame.draw.circle(screen, (255, 255, 255), (400, 160), 60)
    pygame.draw.circle(screen, (0, 0, 255), (400, 160), 40)

    # nose
    pygame.draw.circle(screen, (128, 0, 0), (320, 240), 40)

    #Mouth
    pygame.draw.rect(screen, (90, 0, 0), (200, 320, 240, 30))

    pygame.display.update()

