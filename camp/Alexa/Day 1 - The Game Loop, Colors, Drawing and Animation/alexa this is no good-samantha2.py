import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
<<<<<<< Updated upstream:camp/Alexa/Day 2 - Raindrops/alexa this is no good-samantha.py
    def __init__(self, screen, x, y, raindrop_filename):
=======
    def __init__(self, screen, x, y, image):
>>>>>>> Stashed changes:camp/Alexa/Day 2 - Raindrops/00-TODOs.py
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
<<<<<<< Updated upstream:camp/Alexa/Day 2 - Raindrops/alexa this is no good-samantha.py
        self.raindrop_filename = raindrop_filename
        self.image_raindrop = pygame.image.load(self.raindrop_filename).convert()
=======
        self.image = image
        self.image_raindrop = pygame.image.load(self.image).convert()
>>>>>>> Stashed changes:camp/Alexa/Day 2 - Raindrops/00-TODOs.py

-
    def move(self):
        # TODO. Change the  y  position of this Raindrop by its speed.
        pass

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.
        self.screen.blit(self.image_raindrop, (self.x, self.y))


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        ...
        self.screen = screen
        self.x = x
        self.y = y
        self.with_umbrella = with_umbrella
        self.without_umbrella = without_umbrella
        self.last_hit_time = 0
        self.image_umbrella = pygame.image.load(self.with_umbrella).convert()

    def draw(self):
        self.screen.blit(self.image_umbrella, (self.x, self.y))

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        pass

class Cloud:
    def __init__(self, screen, x, y, cloud_png):
        # TODO. Inititalize this Cloud, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of this Cloud to x and y.
        # TODO    - Set the image of this Cloud to the given image.
        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(cloud_png).convert()
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.direction = 1

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
    def rain(self):
        random_x = random.randint(0, 300) + self.x
        raindrop = Raindrop(self.screen, random_x, self.y + 100, "raindrop")
    def move(self, dx, dy):
        self.x = self.x + (dx * self.direction)
        self.y = self.y + dy
        if self.x > 800:
            self.direction = -1
        elif self.x < 0:
            self.direction = 1

def main():
    # TODO: Initialize the game, display a captian, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.set_caption("My moving objects")
    screen = pygame.display.set_mode((1000, 600))

    # TODO: Make a Clock,pygame.init() Hero and Cloud with appropriate images, starting at appropriate positions.
    clock = pygame.time.Clock()
    hero = Hero(screen, 0, 400, "Mike_umbrella.png", "Mike.png")
    cloud1 = Cloud(screen, 0, 100, "cloud.png")
    raindrop = Raindrop(screen, 0, 2, "images.jpeg")


    # TODO: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    # TODO    Make the pygame.QUIT event stop the game.
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            hero.move(5, 0)
        if pressed_keys[pygame.K_LEFT]:
            hero.move(-5, 0)
        if pressed_keys[pygame.K_UP]:
            hero.move(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            hero.move(0, 5)

        cloud1.move(5, 0)
        screen.fill((100, 20, 244))
        hero.draw()
        raindrop.draw()
        cloud1.draw()
        pygame.display.update()

    # TODO: Inside the game loop, get the list of keys that are currently pressed.
    # TODO    Arrange so that the Cloud moves:
    # TODO      1 pixel to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
    # TODO      1 pixel to the left if the Left Arrow key (pygame.K_LEFT) is pressed.
    # TODO      1 pixel up if the Up Arrow key (pygame.K_UP) is pressed.
    # TODO      1 pixel down if the Down Arrow key (pygame.K_DOWN) is pressed.

    # TODO: Inside the game loop, draw the screen, Hero and Cloud.

    # TODO: Inside the game loop, make the Cloud "rain", and then:
    # TODO    For each Raindrop in the Cloud's list of raindrops:
    # TODO      - move the Raindrop.
    # TODO      - draw the Raindrop.
    # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
    # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.
    pass


# TODO: Call main.
main()