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
        pygame.draw.line(self.screen, (0, 0, 255), (self.x, self.y), (self.x, self.y + 5), 2)
        # TODO    from the current position of this Raindrop.


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        self.screen = screen
        self.x = x
        self.y =y
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()
        self.last_hit_time = 0


    def draw(self):
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        pass

    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))

class Cloud:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert()
        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        new_raindrop = Raindrop(self.screen, random.randint(self.x, self.x + 300), self.y + 100)
        self.raindrops.append(new_raindrop)
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.


def main():
    print('ready')
    pygame.init()
    pygame.display.set_caption('Rain Drops')
    screen = pygame.display.set_mode((1000,600))
    clock = pygame.time.Clock()
    cloud = Cloud(screen, 300, 50 ,"cloud.png")
    cloud.rain()
    cloud.rain()
    cloud.rain()
    cloud.rain()
    like = Hero(screen, 300, 400, 'Mike_umbrella.png', 'Mike.png')
    single_raindrop = Raindrop(screen, 500, 50)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        cloud.rain()
        screen.fill((255, 255, 255))


        # TODO: Inside the game loop, get the list of keys that are currently pressed.
        # TODO    Arrange so that the Cloud moves:
        # TODO      1 pixel to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # TODO      1 pixel to the left if the Left Arrow key (pygame.K_LEFT) is pressed.
        # TODO      1 pixel up if the Up Arrow key (pygame.K_UP) is pressed.
        # TODO      1 pixel down if the Down Arrow key (pygame.K_DOWN) is pressed.
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 2
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 2
        if pressed_keys[pygame.K_UP]:
             cloud.y = cloud.y - 2
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 2

        if pressed_keys[pygame.K_d]:
            like.x = like.x + 2
        if pressed_keys[pygame.K_a]:
            like.x = like.x - 2
        if pressed_keys[pygame.K_w]:
            like.y = like.y - 2
        if pressed_keys[pygame.K_s]:
            like.y = like.y + 2
        like.draw()
        cloud.draw()
        #single_raindrop.move()
       #single_raindrop.draw()
        for raindrop in cloud.raindrops:

            raindrop.draw()
            raindrop.move()
            if like.hit_by(raindrop):
                like.last_hit_time = time.time()


        like.draw()

        # TODO: Inside the game loop, make the Cloud "rain", and then:

        # TODO    For each Raindrop in the Cloud's list of raindrops:
        # TODO      - move the Raindrop.
        # TODO      - draw the Raindrop.
        # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
        # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.

        pygame.display.update()

# TODO: Call main.
main()