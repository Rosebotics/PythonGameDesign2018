import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        # done Inititalize this Raindrop, as follows:
        # done   - Store the screen.
        # done  - Set the initial position of the Raindrop to x and y.
        # done - Set the initial speed to a random integer between 5 and 18.

        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)

    def move(self):
        #done. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
     pass
    def draw(self):
        # done. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # done   from the current position of this Raindrop.
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        # done. Inititalize this Hero, as follows:
        # done    - Store the screen.
        self.screen = screen
        # done   - Set the initial position of this Hero to x and y.
        # TODO    - Set the image of this Hero WITH an umbrella to the given with_umbrella file.
        # TODO    - Set the image of this Hero WITHOUT an umbrella to the given without_umbrella file.
        self.x = x
        self.y = y
        # done    - Set the image of this Cloud to the given image.
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        self.image_without_umbrella=pygame.image.load(without_umbrella).convert()
        # done    - Set the "last hit time" to 0.
        self.last_hit_time = 0
        # done  Use instance variables:
        # done     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.

    def draw(self):
        # done Draw (blit) this Hero, at this Hero's position, as follows:
        # done    If the current time is greater than this Hero's last_hit_time + 1,
        # done      draw this Hero WITHOUT an umbrella,
        # done     otherwise draw this Hero WITH an umbrella.

        if time.time() > self. last_hit_time + 1:
         self.screen.blit(self.image_with_umbrella, (self.x, self.y))
        else:
         self.screen.blit(self.image_without_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        #TODO:
    #Return True if this Hero is currently colliding with the given Raindrop.
        pass

class Cloud:
    def __init__(self, screen, x, y, image):
        # done. Inititalize this Cloud, as follows:
        # done    - Store the screen.
        self.screen = screen
        # done    - Set the initial position of this Cloud to x and y.
        self.x = x
        self.y = y
        # done    - Set the image of this Cloud to the given image.
        self.image = pygame.image.load(image).convert()
        # done    - Set the list of Raindrop objects for this Cloud to the empty list.
        self.raindrops =[]
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.

    def draw(self):
        # done. Draw (blit) this Cloud's image at its current position.
         self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        pass


def main():
    # done: Initialize the game, display a captian, and set   screen   to a 1000x600 Screen.
    print("ready")
    pygame.init()
    pygame.display.set_caption("raindrops")
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    cloud = Cloud(screen,100,100,"cloud.png")
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")

    #Temporary testing!!!!
    single_raindrop = Raindrop(screen, 500, 50)
    # done: Make a Clock)
    # done: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    # done:Make the pygame.QUIT event stop the game.
    while True:
        clock.tick(60)
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                sys.exit()
         #move the cloud
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 2
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 2
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 2
        #
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 2
         #move mike
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d]:
            mike.x = mike.x + 2
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            mike.x = mike.x - 2

        # done: Inside the game loop, get the list of keys that are currently pressed.
        # done   Arrange so that the Cloud moves:
        # done     2 pixel to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # done     2 pixel to the left if the Left Arrow key (pygame.K_LEFT) is pressed.
        # done      2 pixel up if the Up Arrow key (pygame.K_UP) is pressed.
        # done     2 pixel down if the Down Arrow key (pygame.K_DOWN) is pressed.

        # TODO: Inside the game loop, draw the screen, Hero and Cloud.
        screen.fill((255, 255, 255))

        cloud.draw()
        mike.draw()
        single_raindrop.draw()
        single_raindrop.move()
        # TODO: Inside the game loop, make the Cloud "rain", and then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
        # TODO      - move the Raindrop.
        # TODO      - draw the Raindrop.
        # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
        # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.

        pygame.display.update()

# done: Call main
main()