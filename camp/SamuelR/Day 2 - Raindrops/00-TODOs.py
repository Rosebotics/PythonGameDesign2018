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


    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 150), (self.x, self.y), (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()
        self.last_hit_time = 0




    def draw(self):

        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
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


def main():
    print('Ready')
    pygame.init()
    pygame.display.set_caption('Raindrops')
    screen = pygame.display.set_mode((1000, 600))

    clock = pygame.time.Clock()

    cloud = Cloud(screen, 300, 50, 'cloud.png')

    hero = Hero(screen, 300, 400, 'Mike_umbrella.png', 'Mike.png')

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255, 255, 255))
        cloud.rain()

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] :
            cloud.x = cloud.x + 5

        if pressed_key[pygame.K_LEFT] :
            cloud.x = cloud.x - 5

        if pressed_key[pygame.K_UP] :
            cloud.y = cloud.y - 5

        if pressed_key[pygame.K_DOWN] :
            cloud.y = cloud.y + 5

        if pressed_key[pygame.K_d]:
            hero.x = hero.x + 5

        if pressed_key[pygame.K_a]:
            hero.x = hero.x - 5

        if pressed_key[pygame.K_w]:
            hero.y = hero.y - 5

        if pressed_key[pygame.K_s]:
            hero.y = hero.y + 5

        cloud.draw()
        hero.draw()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if hero.hit_by(raindrop):
                hero.last_hit_time = time.time()

        pygame.display.update()

main()