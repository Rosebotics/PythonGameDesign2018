
import pygame
import sys

pygame.init()
pygame.display.set_caption('Interactions')
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

nose_y_position = 240

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        nose_y_position = 0


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
    nose_y_position = nose_y_position + 1
    if nose_y_position > 600:
        nose_y_position = 240
    pygame.draw.circle(screen, (128, 0, 0), (320, nose_y_position), 40)

    # Mouth
    pygame.draw.rect(screen, (90, 0, 0), (200, 320, 240, 30))

    pygame.display.update()
