# done: Copy all of your   03-Colors.py   program and put it below this comment.
import pygame
import sys

pygame.init()
pygame.display.set_caption("       Drawings")
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 255, 180))

    # draw shapes on the screen
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 240, )
    pygame.draw.circle(screen, (255, 255, 255), (180, 160), 70, )
    pygame.draw.circle(screen, (255, 255, 255), (460, 160), 70, )
    pygame.draw.circle(screen, (255, 255, 255), (320, 250), 40, )
    pygame.draw.rect(screen, (255, 0, 0), (200, 350, 240, 30), 70, )

    pygame.display.update()
