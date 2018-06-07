import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y, file_name):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_raindrop = pygame.image.load(file_name).convert()
        self.image_raindrop = pygame.transform.scale(self.image_raindrop, (10, 23))
        self.speed = 6

    def move(self):
        # TODO. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the       y  position of this Raindrop is greater than 800.
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
        self.without_umbrella = without_umbrella
        self.with_umbrella = with_umbrella
        self.last_hit_time = 0
        self.image_umbrella = pygame.image.load(self.with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(without_umbrella)
        self.current_image = self.image_without_umbrella
 
    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        if time.time() > self.last_hit_time + 1:
            self.current_image = self.image_without_umbrella
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.current_image = self.image_umbrella
            self.screen.blit(self.image_umbrella, (self.x, self.y))
    def move(self, dx, dy):
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
    def __init__(self, screen, x, y, file_name, hero):

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
        self.image_cloud = pygame.image.load(file_name).convert()
        self.direction = 1
        self.raindrops = []
        self.hero = hero

    def move(self, dx, dy):
        self.x = self.x + (dx * self.direction)
        self.y = self.y + dy
        if self.x > 1000 - 300:
            self.direction = -2
        elif self.x < 0:
            self.direction = 2

    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image_cloud, (self.x, self.y))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.

        randomx = self.x + random.randint(75, 250)
        #randomy = random.randint(0, 200)
        raindrop = Raindrop(self.screen, randomx, self.y + 100, "raindrop.png")
        self.raindrops.append(raindrop)

        for k in range(len(self.raindrops)):
            raindrop = self.raindrops[k]
            raindrop.move()
            if self.hero.hit_by(raindrop):
                self.hero.last_hit_time = time.time()
            else:
                raindrop.draw()
                #self.screen.blit(self.screen., (x, y), pygame.Rect(x, y, 62, 62))

def main():
    # TODO: Initialize the game, display a captian, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.set_caption("Forecasts Reveal Falsities...")
    screen = pygame.display.set_mode((1000, 600))
    # TODO: Make a Clock, Hero and Cloud with appropriate images, starting at appropriate positions.
    clock = pygame.time.Clock()
    hero = Hero(screen, 500, 400, "Mike_umbrella.png", "Mike.png")
    cloud = Cloud(screen, 300, 60, "cloud.png", hero)
    raindrop = Raindrop (screen, 100, 100, "raindrop.png")
    #raindrop = Raindrop(screen, 300, 60, "raindrop.png")
    # TODO: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    # TODO    Make the pygame.QUIT event stop the game.
    #bg = pygame.image.load("images\space.png")
    while True:
        screen.fill((255, 255, 255))
        clock.tick(60)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            hero.move(1, 0)
        if pressed_keys[pygame.K_LEFT]:
            hero.move(-2, 0)
        if pressed_keys[pygame.K_UP]:
            hero.move(0, -2)
        if pressed_keys[pygame.K_DOWN]:
            hero.move(0, 1)
        if pressed_keys[pygame.K_w]:
            cloud.move(0, -2)
        if pressed_keys[pygame.K_s]:
            cloud.move(0, 2)
        if pressed_keys[pygame.K_a]:
            cloud.move(-2, 0)
        if pressed_keys[pygame.K_d]:
            cloud.move(2, 0)
        cloud.move(1, 0)


        hero.draw()
        cloud.draw()
        raindrop.draw()
        raindrop.move()
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