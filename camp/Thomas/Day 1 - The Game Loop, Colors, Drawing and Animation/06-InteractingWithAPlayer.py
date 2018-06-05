
import pygame
import sys

nose_y_position=242
pygame.init()
pygame.display.set_caption('Animation')
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

while True:
    clock.tick(9999999999999999999999999999999999999999999999999999999)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((2, 215, 15))
    #draw shapes on the screen
    nose_y_position = nose_y_position + 1
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        nose_y_position = 0
    if nose_y_position > 900:
        nose_y_position=240
    pygame.draw.circle(screen, (23, 29, 10), (321, nose_y_position), 360)
    pygame.draw.circle(screen, (23, 239, 10), (321, nose_y_position), 340, 40)
    pygame.draw.circle(screen, (223, 29, 10), (321, nose_y_position), 300, 40)
    pygame.draw.circle(screen, (23, 239, 110), (321, nose_y_position), 260, 40)
    pygame.draw.circle(screen, (243, 233, 10),(321, nose_y_position), 220, 40)
    pygame.draw.circle(screen, (255, 230, 130), (21, nose_y_position), 200, 40)
    pygame.draw.circle(screen, (23, 29, 255), (321, nose_y_position), 160, 40)
    pygame.draw.circle(screen, (242, 239, 255,), (321, nose_y_position), 140, 40)
    pygame.draw.circle(screen, (83, 239, 170,), (321, nose_y_position), 100, 40)
    pygame.display.update()