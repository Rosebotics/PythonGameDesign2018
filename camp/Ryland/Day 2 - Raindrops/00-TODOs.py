import pygame
import sys
import time  # Note this!
import random  # Note this!

class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)


    def move(self):
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 255), (self.x, self.y ) ,(self.x, self.y + 5),2)

class Hero:
    def __init__(self, screen, x, y, no_umbrella, with_umbrella):
        # TODO    - Store the screen.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(no_umbrella).convert()
        self.screen.blit(self.image_with_umbrella, (self.x, self.y))

        # TODO  - Set the "last hit time" to 0.
        self.last_hit_time = 0
        # wip Use instance variables:
        # wip     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.


    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        if time.time() > self.last_hit_time + 0.25:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        return pygame.Rect(self.x, self.y , 170 ,192).collidepoint((raindrop.x, raindrop.y ))

class Cloud:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert()
        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y ))

    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        new_raindrop = Raindrop(self.screen, random.randint(self.x, self.x + 300), self.y + 100)
        self.raindrops.append(new_raindrop)

def main():
    print('hello world itz ya boi RYLAND ')
    pygame.init()
    pygame.display.set_caption("Make it RAIN!!!!!")
    screen = pygame.display.set_mode((1000, 600))

    #single_raindrop  = Raindrop(screen, 500, 20)

    Link = Hero(screen, 300, 400, "Mike.png", "Mike_umbrella.png")
    cloud = Cloud(screen, 300, 50, "cloud.png")



    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        cloud.rain()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys [pygame.K_RIGHT]:
            cloud.x = cloud.x + 4
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 4
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 4
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 4

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d]:
            Link.x = Link.x + 6
        if pressed_keys[pygame.K_a]:
            Link.x = Link.x - 6
        if pressed_keys[pygame.K_w]:
            Link.y = Link.y - 6
        if pressed_keys[pygame.K_s]:
            Link.y = Link.y + 6









        cloud.draw()

        for raindrop in cloud.raindrops:
            raindrop.draw()
            raindrop.move()
            if Link.hit_by(raindrop):
                Link.last_hit_time = time.time()

        Link.draw()
        # TODO: Inside the game loop, make the Cloud "rain", and then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
        # TODO      - move the Raindrop.
        # TODO      - draw the Raindrop.
        # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
        # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.

        pygame.display.update()

main()

