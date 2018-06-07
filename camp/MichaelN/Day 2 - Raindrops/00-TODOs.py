import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y, filename):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        self.screen = screen
        # TODO    - Set the initial position of the Raindrop to x and y.
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename).convert()
        self.speed = 2
        self.image = pygame.transform.scale(self.image,(5,10))
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        pass

    def move(self):
        self.y = self.y + 1
        self.y = self.y + self.speed
        pass

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        self.screen.blit(self.image, (self.x, self.y))
        # TODO    from the current position of this Raindrop.
        pass


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
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
        self.with_umbrella = with_umbrella
        self.withhout_umbrella = without_umbrella
        self.last_hit_tiem = 0
        self.image_umbrella = pygame.image.load(self.with_umbrella).convert()
        self.image_no = pygame.image.load(self.withhout_umbrella).convert()
        self.crrent_imag = self.withhout_umbrella

        pass


    def moov(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        if self.x > 1000 - 300:
            self.dirextion = -1
        elif self.x < 0:
            self.dirextion = 1



    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        if time.time() > self.last_hit_tiem + 1:
            self.crrent_imag = self.image_no
        else:
            self.crrent_imag = self.image_umbrella

        self.screen.blit(self.crrent_imag,(self.x, self.y))

    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        hero_box = pygame.Rect(self.x, self.y,
                               self.crrent_imag.get_width(),
                               self.crrent_imag.get_height())
        raindrop_box = pygame.Rect(raindrop.x, raindrop.y,
                                   raindrop.image.get_width(),
                                   raindrop.image.get_height())
        return  hero_box.colliderect(raindrop_box)


class Cloud:
    def __init__(self, screen, x, y, image,  hero):
        # TODO. Inititalize this Cloud, as follows:
        # TODO    - Store the screen.
        self.screen = screen
        # TODO    - Set the initial position of this Cloud to x and y.
        self.x = x
        self.y = y
        # TODO    - Set the image of this Cloud to the given image.
        self.image = image
        self.image = pygame.image.load(self.image).convert()
        self.dirextion = 1
        self.raindrops = []
        self.hero = hero

        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.t
        pass

    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image,(self.x, self.y))
        pass
    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        random_x = self.x + random.randint(0, 300)
        randrop = Raindrop(self.screen, random_x, self.y + 100, "Fire.png")
        self.raindrops.append(randrop)

        for k in  range(len(self.raindrops)):
            randrop = self.raindrops[k]
            randrop.move()
            randrop.draw()
            if self.hero.hit_by(randrop):
                self.hero.last_hit_tiem = time.time()

        pass

    def moov(self,xspeed, yspeed):
        self.x = self.x + xspeed + (xspeed * self.dirextion)
        self.y = self.y + yspeed
        if self.x > 1000 - 300:
           self.dirextion = self.dirextion  - 1
        elif self.x < 0:
            self.dirextion = self.dirextion + 1


def main():
    # TODO: Initialize the game, display a captian, and set   screen   to a 1000x600 Screen.

    pygame.init()
    pygame.display.set_caption("fred")
    screen = pygame.display.set_mode((1000, 600))
    # TODO: Make a Clock, Hero and Cloud with appropriate images, starting at appropriate positions.
    hero = Hero(screen, 500,300, "Mike_umbrella.png", "Mike.png")
    cloud = Cloud(screen, 600, 0, "cloud.png", hero)
    # TODO: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
    # TODO    Make the pygame.QUIT event stop the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            hero.moov(-1, 0)
        if pressed_keys[pygame.K_RIGHT]:
            hero.moov(1, 0)

        cloud.moov(1,0)
        screen.fill((255, 255, 255))
        hero.draw()
        cloud.draw()
        cloud.rain()

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