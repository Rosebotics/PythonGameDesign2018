# This continues the previous module.  I have put it into its own module only to help my sequencing.
# Students start with the following:

# My first Pygame program.
# Authors: Many people and <PUT-YOUR-NAME-HERE>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

# while True:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             sys.exit()
#     screen.fill((255, 105, 180))  # Hot pink
#     pygame.display.update()


# TODO: 6. Add the   pygame.draw.circle(screen, ...), per the code below.  Run, then discuss.  Then:
# TODO     a. Students: Make a bunch of circles appear.  (Learn that Y-axis goes DOWN.)
# TODO     b. Students: Make other kinds of objects appear.  The DOT trick may help (show them it).
# TODO           rect:  ulX, ulY, width, height
# TODO           line
# TODO           lines
# TODO           ellipse:
# TODO           arc:
# TODO           line:
# TODO           polygon:
# TODO           aaline, aalines:

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 105, 180))  # Hot pink
    pygame.draw.circle(screen, (0, 0, 0), (100, 150), 20)
    pygame.draw.circle(screen, (255, 255, 0), (200, 350), 50)
    pygame.draw.rect(screen, (0, 0, 255), (20, 40, 100, 40), 5)
    pygame.display.update()

