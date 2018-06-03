# This continues the previous module.
# Students will copy their previous code into their version of this module.
# Students will then start with something like the following:


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
#     pygame.draw.circle(screen, (0, 0, 0), (100, 150), 20)
#     pygame.draw.circle(screen, (255, 255, 0), (200, 350), 50)
#     pygame.draw.rect(screen, (0, 0, 255), (20, 40, 100, 40), 5)
#     pygame.display.update()


# TODO: 7. Add animation per the code below (with just xpos, not yet xpo2).
# TODO       Run, then discuss.  Then:
# TODO         a. Students: Play with the animation speed.
# TODO         b. Students: Animate MORE of the objects that you drew.
# TODO              Be creative!

# xpos = 50
# xpos2 = 500
# while True:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             sys.exit()
#     xpos = xpos + 1
#     xpos2 = xpos2 = xpos2 - 5
#     screen.fill((255, 105, 180))  # Hot pink
#     pygame.draw.circle(screen, (0, 0, 0), (100, 150), 20)
#     pygame.draw.circle(screen, (255, 255, 0), (xpos, 350), 50)
#     pygame.draw.rect(screen, (0, 0, 255), (xpos2, 40, 100, 40), 5)
#     pygame.display.update()


# TODO: 8. Add a Clock to control the speed of the Game Loop,
# TODO       per the code below.
# TODO     Students:  Experiment with the clock speed.
# TODO        What is the fastest speed your computer allows?
# TODO        What happens as the speed gets slow?

# xpos = 50
# xpos2 = 500
# clock = pygame.time.Clock()
# while True:
#     clock.tick(500)
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             sys.exit()
#     xpos = xpos + 1
#     xpos2 = xpos2 - 5
#     screen.fill((255, 105, 180))  # Hot pink
#     pygame.draw.circle(screen, (0, 0, 0), (100, 150), 20)
#     pygame.draw.circle(screen, (255, 255, 0), (xpos, 350), 50)
#     pygame.draw.rect(screen, (0, 0, 255), (xpos2, 40, 100, 40), 5)
#     pygame.display.update()


# TODO: 9. Add a caption for your program,
# TODO       per the code below.
# TODO     Students:  Choose your own caption.

pygame.display.set_caption("My First Game")
xpos = 50
xpos2 = 500
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    xpos = xpos + 1
    xpos2 = xpos2 - 5
    screen.fill((255, 105, 180))  # Hot pink
    pygame.draw.circle(screen, (0, 0, 0), (100, 150), 20)
    pygame.draw.circle(screen, (255, 255, 0), (xpos, 350), 50)
    pygame.draw.rect(screen, (0, 0, 255), (xpos2, 40, 100, 40), 5)
    pygame.display.update()