
import pygame
import sys

pygame.init()
pygame.display.set_caption("animation")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

nose_y_position = 240

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((234, 162, 223))

    # drawing shapes on the screen
    # big circle
    pygame.draw.circle(screen, (0, 125, 255), (320, 240), 200, 200)
    # left eye
    pygame.draw.circle(screen, (0, 255, 255), (240, 160), 66, 40)
    # rtight eye
    pygame.draw.circle(screen, (0, 255, 0), (400, 160), 66, 40)
    # nose
    nose_y_position = nose_y_position + 122
    if nose_y_position > 400:
        nose_y_position = 200
    pygame.draw.circle(screen, (255, 0, 0), (320, nose_y_position), 40, 20)
    # muoth
    pygame.draw.rect(screen, (0, 255, 255), (200, 320, 240, 30))

    pygame.display.update()
