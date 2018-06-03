# My first Pygame program.
# Authors: Many people and <PUT-YOUR-NAME-HERE>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    pygame.display.update()


# TODO: 1. Put your name in the preceding line at the place indicated.  Explain why.
# TODO: 2. Run the above.  Show them how to STOP a running program using the red square.
# TODO       Run again, this time using the Green right-facing triangle (arrow).
# TODO: 3. Walk through the code, explaining it.

# TODO: 4. Add the   screen.fill   as shown below.  Run.  Talk about RGB.
# TODO     Talk about applying METHODS (who dot what with-what) to objects (screen).
# TODO     Students: experiment with other background colors, briefly.

# while True:
#     screen.fill((255, 255, 255))
#     pygame.display.update()


# TODO: 5. Make the program able to quit, per the code below:
# TODO      a. Add the FOR loop, with a   print(event)   inside.
# TODO           Run.  Move the mouse, then click near X (to minimize motion),
# TODO           then click-drag, then press X, then press a key.
# TODO           Show them what got printed (on the Console):
# TODO              MouseMotion, MouseButtonUp, MouseButtonDown, Quit, KeyDown, KeyUp event.
# TODO           Talk about FOR loops and events.
# TODO      b. Then add the IF and sys.exit.  Talk about IF, ==, sys.exit.
# TODO           Run.
# TODO           Make a typo and show how it appears (also Run).
# TODO           Then fix the typo and help students fix theirs.
# TODO             Students can experiment with other colors for background
# TODO             and/or IFs for other events (with PRINT as the body).

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 255, 255))
    # pygame.display.update()


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


    pygame.draw.circle(screen, (0, 255, 0), (100, 150), 20)
    pygame.draw.circle(screen, (100, 0, 100), (200, 350), 50)
    pygame.draw.rect(screen, (0, 0, 255), (20, 40, 100, 40), 5)
    pygame.display.update()