import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        # DONE. Inititalize this Raindrop, as follows:
        # DONE    - Store the screen.
        # DONE    - Set the initial position of the Raindrop to x and y.
        # DONE    - Set the initial speed to a random integer between 5 and 18.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)

    def move(self):
        # DONE. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # DONE. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # DONE    from the current position of this Raindrop.
        pygame.draw.line(self.screen, (0, 0, 150), (self.x, self.y), (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        # DONE. Inititalize this Hero, as follows:
        # DONE    - Store the screen.
        self.screen = screen
        # DONE    - Set the initial position of this Hero to x and y.
        self.x = x
        self.y = y
        # DONE    - Set the image of this Hero WITH an umbrella to the given with_umbrella file.
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        # DONE    - Set the image of this Hero WITHOUT an umbrella to the given without_umbrella file.
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()

        # DONE    - Set the "last hit time" to 0.
        self.last_hit_time = 0

    def draw(self):
        # DONE. Draw (blit) this Hero, at this Hero's position, as follows:
        # DONE    If the current time is greater than this Hero's last_hit_time + 1,
        # DONE      draw this Hero WITHOUT an umbrella,
        # DONE      otherwise draw this Hero WITH an umbrella.

        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        pass


class Cloud:
    def __init__(self, screen, x, y, image):
        # DONE. Inititalize this Cloud, as follows:
        # DONE    - Store the screen.
        self.screen = screen
        # DONE    - Set the initial position of this Cloud to x and y.
        self.x = x
        self.y = y
        # DONE    - Set the image of this Cloud to the given image.
        self.image = pygame.image.load(image).convert()
        # DONE    - Set the list of Raindrop objects for this Cloud to the empty list.
        self.raindrops = []

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
    print("Ready!")
    pygame.init()
    pygame.display.set_caption("Raindrops")
    screen = pygame.display.set_mode((1000, 600))

    # DONE: Make a Clock
    clock = pygame.time.Clock()

    # DONE: Make a Cloud with appropriate images, starting at appropriate positions.
    cloud = Cloud(screen, 300, 50, "cloud.png")

    # DONE: Make a Hero with appropriate images, starting at appropriate positions.
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")

    # Temporary testing!!!!!!!  TODO: Delete this later
    single_raindrop = Raindrop(screen, 500, 20)

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
        # DONE      2 pixel to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # DONE      2 pixel to the left if the Left Arrow key (pygame.K_LEFT) is pressed.
        # DONE      2 pixel up if the Up Arrow key (pygame.K_UP) is pressed.
        # DONE      2 pixel down if the Down Arrow key (pygame.K_DOWN) is pressed.
        pressed_keys = pygame.key.get_pressed()

        # Move the cloud
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 5
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 5
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 5
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 5

        # Move Mike
        if pressed_keys[pygame.K_d]:
            mike.x = mike.x + 5
        if pressed_keys[pygame.K_a]:
            mike.x = mike.x - 5


        # DONE: Inside the game loop, draw the screen, Hero and Cloud.
        cloud.draw()
        mike.draw()
        single_raindrop.move()
        single_raindrop.draw()

        # TODO: Inside the game loop, make the Cloud "rain", and then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
        # TODO      - move the Raindrop.
        # TODO      - draw the Raindrop.
        # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
        # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.

        pygame.display.update()


# DONE: Call main.
main()