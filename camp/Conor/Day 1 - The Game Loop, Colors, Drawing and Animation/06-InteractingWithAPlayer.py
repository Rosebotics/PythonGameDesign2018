import pygame
import sys

pygame.init()
pygame.display.set_caption("Animation")
screen = pygame.display.set_mode((900, 900))
nose_y_position = 240
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            clock = pygame.time.Clock()
            nose_y_position = 240

    screen.fill((242,148,242))


    nose_y_position = nose_y_position + 1
    # Draw shapes on the screen.
    #Big yellow Circle
    pygame.draw.circle(screen, (255, 255, 225), (255, 255), 210)

    pygame.draw.circle(screen, (100, 100, 100), (240, 160), 55)

    pygame.draw.circle(screen, (100, 100, 100), (400, 160), 55)

    pygame.draw.circle(screen, (0, 0, 255), (220, nose_y_position), 27)
    # Mouth rect
    pygame.draw.rect(screen, (100, 0, 0), (200, 320, 240, 30))



    if nose_y_position > 400:
        nose_y_position = 240
    pygame.display.update()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        nose_y_position = 0