import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.image).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.speed = 3
        self.raindrops = []

    def move(self):
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass


    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.
        self.screen.blit(self.image, (self.x, self.y))


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):

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
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_umbrella, (self.x, self.y))

        else:
            self.current_image = self.image_umbrella
            self.screen.blit(self.current_image, (self.x, self.y))

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def hit_by(self, raindrop):
        hero_box = pygame.Rect(self.x, self.y,
                                self.current_image.get_width(),
                                self.current_image.get_height())
        raindrop_box = pygame.Rect(raindrop.x, raindrop.y,
                                   raindrop.image.get_width(),
                                   raindrop.image.get_height())
        return hero_box.collidedict(raindrop_box)
        pass

class Cloud:

    def __init__(self, screen, x, y, file, ships):
        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.cloud_image = pygame.image.load(file).convert()
        self.direction = 1
        self.raindrops = []
        self.ships = ships

    def draw(self):
        self.screen.blit(self.cloud_image, (self.x, self.y))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        randomx = self.x + random.ranint(0, 100)
        raindrop = Raindrop(self.screen, randomx, self.y, "cat.jpg")
        self.raindrops.append(raindrop)

        for k in range(len(self)):
            raindrop = self.raindrops[k]
            raindrop.move()
            raindrop.draw()


    def move(self, dx, dy):
        self.x = self.x + (dx * self.direction)
        self.y = self.y + dy
        if self.x > 1000 - 300:
            self.direction = -1
        elif self.x < 0:
            self.direction = 1


pass


def main():
    pygame.init()
    pygame.display.set_caption("make the screen white")
    screen = pygame.display.set_mode((1000, 600))
    screen.fill((255, 255, 255))
    ships = Hero(screen, 230, 300, "Mike_umbrella.png", "Mike.png")
    me = Cloud(screen, 300, 50, "cloud.png", ships)
    clock = pygame.time.Clock()
    while True:
        clock.tick(68)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            ships.move(3, 0)
        if pressed_keys[pygame.K_LEFT]:
            ships.move(-3, -0)
        if pressed_keys[pygame.K_UP]:
            ships.move(-0, -3)
        if pressed_keys[pygame.K_DOWN]:
            ships.move(0, 3)

        me.move(1, 0)
        ships.draw()
        me.draw()
        me.rain
        pygame.display.update()

    # TODO: Inside the game loop, make the Cloud "rain", and then:
    # TODO    For each Raindrop in the Cloud's list of raindrops:
    # TODO      - move the Raindrop.
    # TODO      - draw the Raindrop.
    # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
    # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.
    pass


main()
