
import pygame
import sys

clock = pygame.time.Clock()

nose_y_position = 250

pygame.init()
pygame.display.set_caption("       Interactions")
screen = pygame.display.set_mode((640, 480))
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
       nose_y_position = 0


    screen.fill((0, 255, 180))

    # draw shapes on the screen
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 240, )
# ____________________________________________________________________________
    pygame.draw.circle(screen, (255, 255, 255), (180, 160), 70, )
# ____________________________________________________________________________
    pygame.draw.circle(screen, (255, 255, 255), (460, 160), 70, )
# ____________________________________________________________________________
    nose_y_position = nose_y_position + 1
    if nose_y_position > 400:
        nose_y_position = 200
    pygame.draw.circle(screen, (0, 0, 0), (320, nose_y_position), 40, 10)
# ____________________ ________________________________________________________

    pygame.draw.rect(screen, (255, 0, 0), (200, 350, 240, 30), 70, )

    pygame.display.update()