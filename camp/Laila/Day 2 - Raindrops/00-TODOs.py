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

        self.screen = screen
        self.x = x
        self.y = y
        self.with_umbrella = without_umbrella
        self.last_hit_time = 0
        self.image_umbrella = pygame.image.load(self.with_umbrella).convert()

    def draw(self):

        self.screen.blit(self.image_umbrella, (self.x, self.y))

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def hit_by(self, raindrop):
        pass





class Cloud:
    def __init__(self, screen, x, y, file):

        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.cloud_image = pygame.image.load(file).convert()
        self.direction = 1

    def draw(self):
        self.screen.blit(self.cloud_image,(self.x, self.y))
        pass

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        raindrop = raindrop(self,screen, random_x,self)

    def move(self, dx,dy):
        self.x = self.x + (dx * self.direction)
        self.y = self.y + dy
        if self.x > 1000 - 300:
            self.direction = -1
        elif self.x < 0:
            self.direction = 1


def main():

    pygame.init()
    pygame.display.set_caption("make the screen white")
    screen = pygame.display.set_mode((1000,600))
    screen.fill((255,255,255))


    ships= Hero(screen,230,300,"Mike_umbrella.png","Mike.png")
    me = Cloud(screen,300,50,"cloud.png")


    clock = pygame.time.Clock()
    while True:
        clock.tick(68)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            ships.move(3,0)
        if pressed_keys[pygame.K_LEFT]:
            ships.move(-3,-0)
        if pressed_keys[pygame.K_UP]:
                ships.move(-0, -3)
        if pressed_keys[pygame.K_DOWN]:
                ships.move(0, 3)

        me.move(1,0)

        ships.draw()
        me.draw()
        pygame.display.update()




    # TODO: Inside the game loop, make the Cloud "rain", and then:
    # TODO    For each Raindrop in the Cloud's list of raindrops:
    # TODO      - move the Raindrop.
    # TODO      - draw the Raindrop.
    # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
    # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.
    pass



main()