import pygame
import sys

pygame.init()
pygame.display.set_caption("drawling")
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((200, 0, 0))


    # pygame.draw.circle(screen, (50, 50, 255), (320, 240), 50, 5)
    # pygame.draw.circle(screen, (0, 255, 255), (320, 240), 20)

    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25)
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25)
    pygame.draw.circle(screen, (0, 0, 255), (320, 240), 25)
    pygame.draw.circle(screen, (0, 0, 0), (320, 340), 50)


    pygame.display.update()