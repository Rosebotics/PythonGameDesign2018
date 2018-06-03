# My first Pygame program.
# Authors: Many people and <PUT-YOUR-NAME-HERE>

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
# while True:
#     pygame.display.update()


# Students will start with the above.
# TODO: 1. Put your name in the preceding line at the place indicated.  Explain why.
# TODO: 2. Run the above.  Show them how to STOP a running program using the red square.
# TODO       Run again, this time using the Green right-facing triangle (arrow).
# TODO: 3. Walk through the code, explaining it.


# TODO: 4. Make the program able to quit, per the code below:
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
# TODO             Students can experiment with adding PRINT inside the IF, FOR, WHILE, etc.
# TODO           Talk about applying METHODS (who dot what with-what) to objects (screen).

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
