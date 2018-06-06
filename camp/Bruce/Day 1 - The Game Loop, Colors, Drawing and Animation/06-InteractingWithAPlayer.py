
import pygame
import sys


pygame.init()
pygame.display.set_caption('Interactions')
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
he_nose_yyy = 240
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        he_nose_yyy = 0
    screen.fill((102, 205, 170))
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25)
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25)
    he_nose_yyy = he_nose_yyy + 1
    if he_nose_yyy > 400:
        he_nose_yyy = 200
    pygame.draw.circle(screen, (255, 0, 0), (320, he_nose_yyy), 25, 4)
    pygame.draw.rect(screen, (0, 0, 0), (200, 320, 240, 30))

    pygame.display.update()
