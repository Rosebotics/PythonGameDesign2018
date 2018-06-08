import pygame
import sys
import time  # Note this!
import random  # Note this!



class Raindrop:
    def __init__(self, screen, x, y, raindrop_image):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.raindrop_image = raindrop_image
        self.image = pygame.image.load(self.raindrop_image).convert()
        self.image = pygame.transform.scale(self.image, (25, 50))
        self.speed = 10

    def move(self):
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
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        self.screen = screen
        self.x = x
        self.y = y
        self.last_hit_time = 0
        self.image_umbrella = pygame.image.load(with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()
        self.current_image = self.image_without_umbrella

    def draw(self):
        if time.time() > self.last_hit_time + 1:
            self.current_image = self.image_without_umbrella
        else:
            self.current_image = self.image_umbrella
        self.screen.blit(self.current_image, (self.x, self.y))

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
    def __init__(self, screen, x, y, cloud, hero):
        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        self.screen = screen
        self.x = x
        self.y = y
        self.cloud = cloud
        self.image_cloud = pygame.image.load(self.cloud).convert()
        self.direction = 1
        self.raindrops = []
        self.hero = hero

    def draw(self):
        self.screen.blit(self.image_cloud, (self.x, self.y))

    def rain(self):
        randomj = random.randint(0, 1)
        if randomj == 0:
            randomx = self.x + random.randint(0, 175)
            raindrop = Raindrop(self.screen, randomx, self.y + 175, "Mike.png")
            self.raindrops.append(raindrop)

        for k in range(len(self.raindrops)):
            raindrop = self.raindrops[k]
            raindrop.move()
            if self.hero.hit_by(raindrop):
                self.hero.last_hit_time = time.time()
            else:
                raindrop.draw()

    def move(self, dx, dy):
        self.x = self.x + (dx * self.direction)
        self.y = self.y + dy
        if self.x > 1800 - 150:
            self.direction = -1
        elif self.x < -20:
            self.direction = 1

def main():
    pygame.init()
    pygame.display.set_caption("Raindrops of Death")
    screen = pygame.display.set_mode((1900, 1000))
    clock = pygame.time.Clock()
    hero = Hero(screen, 900, 810, "Mike_umbrella.png", "Mike.png")
    cloud = Cloud(screen, 850, 0, "images.jpeg", hero)

    while True:
        screen.fill((255, 255, 255))
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

        cloud.move(2, 0)

        hero.draw()
        cloud.draw()
        cloud.rain()

        pygame.display.update()

    # TODO: Make a Clock, Hero and Cloud with appropriate images, starting at appropriate positions.
    clock = pygame.time.Clock()
    hero =  Hero(screen, 900, 810, "Mike_umbrella.png", "Mike.png")
    cloud = Cloud(screen, 900, 10, "images.jpeg")
    raindrop = Raindrop(screen, 500, 500, "Mike.png")

    # TODO: Inside the game loop, make the Cloud "rain", and then:
    # TODO    For each Raindrop in the Cloud's list of raindrops:
    # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
    # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.
    pass

# TODO3: Call main.
main()