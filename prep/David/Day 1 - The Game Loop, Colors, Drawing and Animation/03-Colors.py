# This continues the previous module.
# Students will copy their previous code into their version of this module.
# Students will then start with the following:

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
#     pygame.display.update()


# TODO: 5. Add the   screen.fill   as shown below.  Run.
# TODO       Talk about RGB and TUPLEs.
# TODO       Talk (again) about applying METHODS (who dot what with-what) to objects (screen).
# TODO     Students: experiment with other background colors.

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 105, 180))  # Hot pink
    pygame.display.update()
