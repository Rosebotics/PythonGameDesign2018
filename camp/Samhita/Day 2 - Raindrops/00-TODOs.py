import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y, raindrop_filename):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.raindrop_filename = raindrop_filename
        self.image_raindrop = pygame.image.load(self.raindrop_filename).convert()
        self.image_raindrop = pygame.transform.scale(self.image_raindrop,(20,20))
        self.speed = 2

    def move(self):
        # TODO. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.
        self.screen.blit(self.image_raindrop, (self.x, self.y))


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
        self.without_umbrella = without_umbrella
        self.last_hit_time = 0
        self.image_umbrella = pygame.image.load(self.with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(self.without_umbrella).convert()
        self.current_image = self.image_without_umbrella

    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        if time.time() > self.last_hit_time + 1:
            self.current_image = self.image_without_umbrella
        else:
            self.current_image = self.image_umbrella
        self.screen.blit(self.current_image, (self.x,self.y))

    def move(self, dx, dy,):
        self.x = self.x + dx
        self.y = self.y + dy


    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        hero_box = pygame.Rect(self.x, self.y,
                               self.current_image.get_width(),
                               self.current_image.get_height())
        raindrop_box = pygame.Rect(raindrop.x, raindrop.y,
                                   raindrop.image_raindrop.get_width(),
                                   raindrop.image_raindrop.get_height())
        return hero_box.colliderect(raindrop_box)



class Cloud:
    def __init__(self, screen, x, y, cloud_png, hero):
        # TODO. Inititalize this Cloud, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of this Cloud to x and y.
        # TODO    - Set the image of this Cloud to the given image.
        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.;
        self.screen = screen
        self.x = x
        self.y = y
        self.cloud = cloud_png
        self.image_cloud = pygame.image.load(self.cloud).convert()
        self.direction = 1
        self.raindrops = []
        self.hero = hero


    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image_cloud, (self.x, self.y))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        randomx = self.x + random.randint(0,100)
        raindrop = Raindrop(self.screen, randomx, self.y + 100, "Raindrop.png")

        self.raindrops.append(raindrop)

        for k in range(len(self.raindrops)):
            raindrop = self.raindrops[k]
            raindrop.move()
            raindrop.draw()
            if self.hero.hit_by(raindrop):
                self.hero.last_hit_time = time.time()

    def move(self, dx, dy):
        self.x = self.x + (dx * self.direction)
        self.y = self.y + dy
        if self.x > 1000 - 300:
            self.direction = -1
        elif self.x < 0:
            self.direction = 1



def main():
    # TODO 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.get_caption()
    screen = pygame.display.set_mode((1000,600))




    # TODO: Make a Clock, Hero and Cloud with appropriate images, starting at appropriate positions.
    clock = pygame.time.Clock()
    hero = Hero(screen,0,300,"Mike_umbrella.png", "Mike.png" )
    cloud1 = Cloud(screen, 0, 100, "cloud.png",hero)
    # TODO: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            hero.move(5,0)
        if pressed_keys[pygame.K_LEFT]:
            hero.move(-5,0)
        if pressed_keys[pygame.K_UP]:
            hero.move(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            hero.move(0,5)
        if pressed_keys[pygame.K_SPACE]:
            hero.move(0,-40)
        if pressed_keys[pygame.K_BACKSPACE]:
            hero.move(0, 40)

        screen.fill((0, 150, 200))
        cloud1.rain()
        cloud1.move(5,0)

        hero.draw()
        cloud1.draw()
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


# TODO 3: Call main.
main()