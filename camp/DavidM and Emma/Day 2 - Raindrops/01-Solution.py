import pygame, sys, time, random
from pygame.locals import *


class Raindrop:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)
        self.screen = screen

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > 800

    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 5), 1)


class Hero:
    def __init__(self, screen):
        self.x = 300
        self.y = 400
        # self.hero = pygame.images.load("../images/RosieRover_160w.png").convert()
        self.image_umbrella = pygame.image.load("Mike_umbrella.png").convert()
        self.image_no_umbrella = pygame.image.load("Mike.png").convert()
        self.screen = screen
        self.last_hit_time = 0

    def draw(self):
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        # return pygame.Rect(self.x, self.y, 120, 80).collidepoint((raindrop.x, raindrop.y))
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))


class Cloud:
    def __init__(self, screen):
        self.x = 300
        self.y = 50
        self.image = pygame.image.load("cloud.png").convert()
        self.screen = screen
        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        self.raindrops.append(Raindrop(self.screen,
                                       random.randint(self.x, self.x + 300),
                                       self.y + 100))



def main():
    pygame.init()
    pygame.display.set_caption("Raindrops")
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()

    hero = Hero(screen)
    cloud = Cloud(screen)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RIGHT]:
            cloud.x += 1
        if pressed_keys[K_LEFT]:
            cloud.x -= 1
        if pressed_keys[K_UP]:
            cloud.y -= 1
        if pressed_keys[K_DOWN]:
            cloud.y += 1

        cloud.rain()
        # print(len(raindrops))

        # screen.fill((100, 200, 255))
        screen.fill((255, 255, 255))
        hero.draw()
        cloud.draw()
        for k in range(len(cloud.raindrops) - 1, -1, -1):
            raindrop = cloud.raindrops[k]
            raindrop.move()
            raindrop.draw()
            if raindrop.off_screen():
                del cloud.raindrops[k]
            if hero.hit_by(raindrop):
                hero.last_hit_time = time.time()
                del cloud.raindrops[k]

        pygame.display.update()


main()