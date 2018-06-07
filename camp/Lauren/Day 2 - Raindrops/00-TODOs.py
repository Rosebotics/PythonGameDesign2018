import pygame
import sys
import time  # Note this!
import random  # Note this!

class Raindrop:
    def __init__(self, screen, x, y, raindrop_pngfile):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(raindrop_pngfile).convert()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.speed = 100000000000

    def move(self, dx, dy):
        # TODO. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.

        self.screen.blit(self.image, (self.x, self.y))


class Hero:
    def __init__(self, screen: object, x: object, y: object, with_umbrella: object, without_umbrella: object) -> object:
        # TODO. Inititalize this Hero, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of this Hero to x and y.
        # TODO    - Set the image of this Hero WITH an umbrella to the given with_umbrella file.
        # TODO    - Set the image of this Hero WITHOUT an umbrella to the given without_umbrella file.
        # TODO    - Set the "last hit time" to 0.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.

        self.screen = screen
        self.x = x
        self.y = y
        self.last_hit_time = 0
        self.image_umbrella = pygame.image.load(with_umbrella).convert()
        self.without_umbrella = pygame.image.load(without_umbrella).convert()
        self.image_umbrella = pygame.transform.scale(self.image_umbrella, (300, 300))
        self.without_umbrella = pygame.transform.scale(self.without_umbrella, (300, 600))
        self.current_image = self.without_umbrella

    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        if time.time() > self.last_hit_time +1:
            self.current_image = self.without_umbrella
        else:
            self.current_image = self.image_umbrella
        self.screen.blit(self.current_image, (self.x, self.y))

    def move(self, dx, dy):
        # TODO. Change the  y  position of this Raindrop by its speed.

        self.x = self.x + dx
        self.y = self.y + dy

    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        hero_box = pygame.Rect(self.x, self.y,
                               self.current_image.get_width(),
                               self.current_image.get_height())
        raindrop_box = pygame.Rect(raindrop.x, raindrop.y,
                                   raindrop.image.get_width(),
                                   raindrop.image.get_height())
        return hero_box.colliderect(raindrop_box)

    def warpspeed(self, dx, dy):

        self.x = self.x +150

    def warp_speed(self, dx, dy):

        self.x = self.x -1500000000000

class Cloud:
    def __init__(self, screen, x, y, filename, hero):
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
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (350, 260))
        self.direction = 1
        self.raindrops = []
        self.hero = hero

    def move(self, dx, dy):
        self.x = self.x + (dx * self.direction)
        self.y = self.y + dy
        if self.x > 1000 - 300:
            self.direction = -10
        elif self.x < 0:
            self.direction =10

    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.

        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        randoms = random.randint(0, 1)
        if randoms == 0:
            randomx = self.x +random.randint(0, 1)
            raindrop = Raindrop(self.screen, randomx, self.y + 100, "depositphotos_21550737-stock-illustration-cartoon-raindrop-with-cat-face.jpg")
            self.raindrops.append(raindrop)

        for k in range(len(self.raindrops)):
            raindrop = self.raindrops[k]
            raindrop.move(0, 1)
            raindrop.draw()
            if self.hero.hit_by(raindrop):
                self.hero.last_hit_time = time.time()

def main():
    # TODO: Initialize the game, display a captian, and set   screen   to a 1000x600 Screen.

    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Mike vs. Cats")


    # TODO: Make a Clock, Hero and Cloud with appropriate images, starting at appropriate positions.

    clock = pygame.time.Clock()
    hero = Hero(screen, 400, 400, "new_mike.jpg", "new_mike2.0")
    raindrop = Raindrop(screen, 200, 300, "depositphotos_21550737-stock-illustration-cartoon-raindrop-with-cat-face.jpg")
    cloud1 = Cloud(screen, 0, 10, "cat.jpg", hero)

    # TODO: Enter the game loop, with a clock tick of 60 (or so) at each iteration.

    while True:
        clock.tick(60)
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            hero.move(10, 0)
        if pressed_keys[pygame.K_LEFT]:
            hero.move(-10, 0)
        if pressed_keys[pygame.K_UP]:
            hero.move(0, -10)
        if pressed_keys[pygame.K_DOWN]:
            hero.move(0, 10)
        if pressed_keys[pygame.K_w]:
            hero.warpspeed(1000, 0) #WARNING!!!!!!!!!!!!!!!!!!!! DO NOT USE UNLESS IN MOST DIRE SITUATIONS!!!!!!!!!!!!!
        if pressed_keys[pygame.K_s]:
            hero.warp_speed(-1000, 0)

        cloud1.move(1, 0)
        screen.fill((255, 255, 255))
        raindrop.move(0, 2)
        hero.draw()
        cloud1.draw()
        raindrop.draw()
        cloud1.rain()

        pygame.display.update()

    # TODO    Make the pygame.QUIT event stop the game.

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