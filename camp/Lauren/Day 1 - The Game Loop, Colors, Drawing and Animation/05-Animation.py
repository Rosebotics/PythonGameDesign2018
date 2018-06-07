# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
# My first Pygame program.
# Authors: Many people and <PUT-YOUR-NAME-HERE>


import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("GameGame")

xpos = 50
clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    xpos = xpos + 1
    screen.fill((0, 150, 150))
    pygame.draw. circle(screen, (200, 100, 250), (255, 130), 200)
    pygame.draw.rect(screen,(255, 128, 0), (255, 40, 1000, 500))
    pygame.draw.circle(screen, (150, 255, 130), (xpos, 350), 100)
    pygame.draw.circle(screen, (0,255, 0), (50, xpos), 100)
    pygame.display.update()


# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
