import pygame
import sys

pygame.init()
pygame.display.set_caption("interactions")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
mouth_y_position = 340
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        mouth_y_position = 0

    screen.fill((200, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25)
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25)
    pygame.draw.circle(screen, (0, 0, 255), (320, 240), 25)
    mouth_y_position = mouth_y_position + 1
    if mouth_y_position > 400:
        mouth_y_position = 200
    pygame.draw.circle(screen, (0, 0, 0), (320, mouth_y_position), 50)
    pygame.display.update()