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
    def __init__(self, screen, x, y, no_umbrella, with_umbrella):
        # TODO    - Store the screen.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(no_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(no_umbrella).convert()
        self.screen.blit(self.image_with_umbrella, (self.x, self.y))

        # wip w    - Set the "last hit time" to 0.
        # wip Use instance variables:
        # wip     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.


    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        self.screen.blit(self.image_with_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        pass

class Cloud:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert()
        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y ))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.

        pass


def main():
    print('hello world itz ya boi RYLAND ')
    pygame.init()
    pygame.display.set_caption("Make it RAIN!!!!!")
    screen = pygame.display.set_mode((1000, 600))


    Link = Hero(screen, 300, 400, "Mike.png", "Mike_umbrella.png")


    cloud = Cloud(screen, 300, 50, "cloud.png")
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys [pygame.K_RIGHT]:
            cloud.x = cloud.x +4
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 4
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 4
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 4

        # TODO: Inside the game loop, draw the screen, Hero and
        cloud.draw()
        Link.draw()
        # TODO: Inside the game loop, make the Cloud "rain", and then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
        # TODO      - move the Raindrop.
        # TODO      - draw the Raindrop.
        # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
        # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.

        pygame.display.update()

main()

