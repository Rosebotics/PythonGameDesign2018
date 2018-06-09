import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y, raindrop):
        # TODO. Initialize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_Raindrop = pygame.image.load(raindrop).convert()
        self.image_Raindrop = pygame.transform.scale(self.image_Raindrop, (20, 10))
        self.speed =5

    def move(self):
        self.y = self.y + self.speed

    def off_screen(self): 480

    # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
    pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.
        self.screen.blit(self.image_Raindrop, (self.x, self.y))


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        # TODO. Initialize this Hero, as follows:
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
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()
        self.current_image = self.image_without_umbrella
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def warpspeed(self, dx, dy):
        self.x = self.x + 100

    # TODO      - draw the Raindrop.
    def hit_by(self, raindrop):
        hero_box = pygame.Rect(self.x, self.y,
                                self.current_image.get_width(),
                               self.current_image.get_height())
        raindrop_box = pygame.Rect(raindrop.x, raindrop.y,
                                   raindrop.image_Raindrop.get_width(),
                                   raindrop.image_Raindrop.get_height())
        return hero_box.colliderect(raindrop_box)

    def draw(self):

        if time.time() > self.last_hit_time + 1:
            self.current_image = self.image_without_umbrella
        else:
            self.current_image = self.image_umbrella
        self.screen.blit(self.current_image, (self.x, self.y))


        # def copy(self, screen, x, y, with_umbrella):


class Cloud:
    def __init__(self, screen, x, y, Petpet, hereo_the_magnificent):
        # TODO. Initialize this Cloud, as follows:
        # TODO    - Store the screen.251
        # TODO    - Set the initial position of this Cloud to x and y.
        # TODO    - Set the image of this Clo   ud to the given image.
        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_cloud = pygame.image.load(Petpet).convert()
        self.image_cloud = pygame.transform.scale(self.image_cloud, (200, 200))
        self.direction = 1
        self.raindrops = []
        self.hero = hereo_the_magnificent

    def move(self, x, y):
        self.x = self.x + (x * self.direction)
        self.y = self.y + y
        if self.x > 1000 - 300:
            self.direction = -1
        elif self.x < 0:
            self.direction = 1

    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image_cloud, (self.x, self.y))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of    Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        randomx = self.x + random.randint(0, 100)
        raindrop = Raindrop(self.screen, randomx, self.y + 200, "My raindrop.png")
        self.raindrops.append(raindrop)

        for k in range(len(self.raindrops)):
            raindrop = self.raindrops[k]
            raindrop.move()
            raindrop.draw()
            if self.hero.hit_by(raindrop):
                self.hero.last_hit_time =time.time()


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('My Raindrops are falling on my head')
    clock = pygame.time.Clock()
    hero = Hero(screen, 425, 400, "Mike_umbrella.png", "Mike.png")
    cloud1 = Cloud(screen, 0, 10, 'Petpet.png',hero)

    raindrop = Raindrop(screen, 400, 400, 'My raindrop.png')

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        cloud1.move(1, 0)
        screen.fill((255, 255, 255))
        hero.draw()
        cloud1.draw()
        cloud1.rain()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            hero.move(2, 0)
        if pressed_keys[pygame.K_LEFT]:
            hero.move(-2, 0)
        if pressed_keys[pygame.K_UP]:
            hero.move(0, -2)
        if pressed_keys[pygame.K_DOWN]:
            hero.move(0, 3)
        if pressed_keys[pygame.K_w]:
            hero.warpspeed(100, 0)  # WARNING!!!!!!!!!!!!!!!!! DO NOT USE UNLESS YOU'RE DUMB AND WANT TO DIE!!!!!
        if pressed_keys[pygame.K_s]:  # IT'S A BAD IIIIDDDEEEEAAAAAAAAAAAHJAGOHWHATAWORLDHELP!!!!!!!!!
            hero.move(0, -100)

        pygame.display.update()
    # TODO: Inside the game loop, make the Cloud "rain", and then:
    # TODO    For each Raindrop in the Cloud's list of raindrops:
    # TODO      - move the Raindrop.
    # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
    # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.
    pass


main()
