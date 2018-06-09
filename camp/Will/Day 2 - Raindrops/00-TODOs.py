import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y, water_png_file):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.y = y
        self.x = x
        self.water = water_png_file
        self.image = pygame.image.load(water_png_file).convert()
        self.image = pygame.transform.scale(self.image, (5, 10))
        self.speed = 20

    def move(self):
        # TODO. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position o      f this Raindrop.
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
        self.image_without_umbrella = pygame.image.load(without_umbrella)
        self.current_image = self.image_without_umbrella

    def draw(self):
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
            self.current_image = self.image_without_umbrella
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))
            self.current_image = self.image_umbrella


    def move(self, dx, dy):
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

class Cloud:
    def __init__(self, screen, x, y, image_file, hero):
        self.x = x
        self.y = y
        self.screen = screen
        self.image_file = image_file
        self.image = pygame.image.load(self.image_file).convert()
        self.direction = 1
        self.raindrops = []
        self.hero = hero

    def move(self, dx, dy=0):
        self.y = self.y + dy
        self.x = self.x + (dx * self.direction)
        self.y = self.y + dy
        if self.x > 1000 - 300:
            self.direction = -1
        elif self.x < 0:
            self.direction = 1

    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x aRunnd this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        randomx = self.x + random.randint(0, 300)
        raindrop = Raindrop(self.screen, randomx, self.y + 100, "water.png")
        self.raindrops.append(raindrop)

        for k in range(len(self.raindrops)):
            raindrop = self.raindrops[k]
            raindrop.move()
            raindrop.draw()
            if self.hero.hit_by(raindrop):
                self.hero.last_hit_time = time.time()


def main():
    # TODO: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.set_caption("essence of seattle")
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    hero = Hero(screen, 400, 410, "Mike_umbrella.png", "Mike.png")
    cloud1 = Cloud(screen, 390, 50, "cloud.png", hero)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((100, 100, 100))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            hero.move(-9, 0)
        if pressed_keys[pygame.K_d]:
            hero.move(9, 0)
        if pressed_keys[pygame.K_w]:
            hero.move(0, -9)
        if pressed_keys[pygame.K_s]:
            hero.move(0, 9)
        if pressed_keys[pygame.K_DOWN]:
            hero.move(0, 20)
        if pressed_keys[pygame.K_u]:
            cloud1.move(-1)
        if pressed_keys[pygame.K_i]:
            cloud1.move(1)
        cloud1.move(1)


        cloud1.draw()
        cloud1.rain()
        hero.draw()
        pygame.display.update()


# TODO: Call main.
main()
