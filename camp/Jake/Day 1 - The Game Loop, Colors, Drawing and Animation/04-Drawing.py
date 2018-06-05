# Done: Copy all of your   03-Colors.py   program and put it below this comment.
# DOne    One way to do so is:
# Done      1. Inside  03-Colors.py,  do:
# Done           -- Control-A (to SELECT the entire contents of the file, then
# Done           -- Control-C (to COPY that entire selection)
# Done      2. Inside this file:
# Done           -- Click below this comment, then
# Done           -- Control-V (to PASTE the copied code into this file.
import pygame
import sys

pygame.init()
pygame.display.set_caption('My first program')
screen = pygame.display.set_mode((720, 620))
while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((175, 255, 255))

    # Draw shapes on the screen

    # Big Yellow circle
    pygame.draw.circle(screen, (250, 250, 0), (320, 240), 210)

    # Left Eye
    pygame.draw.circle(screen,(0, 0, 0), (240, 160), 25)

    # Right Eye
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25)

    # Nose
    pygame.draw.circle(screen, (255, 0, 0), (320, 240), 20)

    # Mouth
    pygame.draw.rect(screen, (0,0,0),(200, 320, 250, 30))

    # For the Smiles
    pygame.draw.rect(screen, (0, 0, 0), (200, 320, 300, 30))







    pygame.display.update()