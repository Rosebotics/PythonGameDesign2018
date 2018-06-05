
import pygame
import sys

pygame.init()
pygame.display.set_caption("my first program")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

nose_y_position = 240

while True:
     clock.tick(9090909090909)
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
     screen.fill((234, 162, 123.456789))
     # Big yellow circle
     pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)
     # Left eye
     pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 0)
     # Right eye
     pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 0)
     # nose
     nose_y_position = nose_y_position + 1
     if nose_y_position > 400:

     pygame.draw.circle(screen, (255, 0, 0), (320, nose_y_position), 20, 0)
     # mouth
     pygame.draw.rect(screen, (0, 0, 0),     (200, 320, 240, 30))

     pygame.draw.circle(screen, (0, 0, 0),  (250, 320), 25,0)

     pygame.display.update()