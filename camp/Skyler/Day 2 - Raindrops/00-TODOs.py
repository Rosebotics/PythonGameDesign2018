import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        pass

    def move(self):
        # TODO. Change the  y  position of this Raindrop by its speed.
        pass

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.
        pass


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        # DONE. Inititalize this Hero, as follows:
        # DONE    - Store the screen.
        self.screen = screen
        pass
        # TODO    - Set the image of this Hero WITH an umHero's position, as follows:
        #         # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        #         # TODO      draw this Hero WITHOUT an umbrella,
        #         # TODO      otherwise draw this Hero WITH an umbrella.
        #         passbrella to the given with_umbrella file.
        # TODO    - Set the image of this Hero WITHOUT an umbrella to the given without_umbrella file.
        # DONE    - Set the initial position of this Hero to x and y.
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()

    def hit_by(self, raindrop):
        pass

    def draw(self):
        # TODO. Draw (blit) this Hero, at this
        self.screen.blit(self.image_without_umbrella, (self.x, self.y))




class Cloud:
    def __init__(self, screen, x, y, image):
        # DONE. Inititalize this Cloud, as follows:
        # DONE    - Store the screen.
        # DONE    - Set the initial position of this Cloud to x and y.
        self.x = x
        self.y = y
        # DONE    - Set the image of this Cloud to the given image.
        self.image = pygame.image.load(image).convert()
        # DONE    - Set the list of Raindrop objects for this Cloud to the empty list.
        self.raindrops = []
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.
        self.screen = screen

    def draw(self):
        # DONE. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        pass


def main():
    # DONE: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    print("Ready")
    pygame.init()
    pygame.display.set_caption("Raindrops")
    screen = pygame.display.set_mode((1000, 600))


    # DONE: Make a Clock
    clock = pygame.time.Clock()


    cloud = Cloud(screen, 300, 50, "cloud.png")
    mike = Hero(screen, 300, 400, "Mike_umbrella.png" ,  "Mike.png")
    # DONE: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    # DONE    Make the pygame.QUIT event stop the game.
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255, 255, 255))

        # DONE: Inside the game loop, get the list of keys that are currently pressed.
        # DONE    Arrange so that the Cloud moves:
        # DONE      1 pixel to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # DONE      1 pixel to the left if the Left Arrow key (pygame.K_LEFT) is pressed.
        # TODO      1 pixel up if the Up Arrow key (pygame.K_UP) is pressed.
        # TODO      1 pixel down if the Down Arrow key (pygame.K_DOWN) is pressed.
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 2

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 2

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 2

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 2

        # TODO: Inside the game loop, draw the screen, Hero and Cloud.
        cloud.draw()
        mike.draw()
        # TODO: Inside the game loop, make the Cloud "rain", and then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
        # TODO      - move the Raindrop.
        # TODO      - draw the Raindrop.
        # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
        # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.
        pygame.display.update()

# DONE: Call main.
main()