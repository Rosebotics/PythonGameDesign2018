import pygame, sys, random, time
from pygame.locals import *

# Global setup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640, 650))

class Missile:
    def __init__(self, x):
        self.x = x
        self.y = 591

    def move(self):
        self.y -= 5

    def is_off_screen(self):
        return self.y < -8

    def draw(self):
        pygame.draw.line(screen, (255, 0, 0), (self.x, self.y), (self.x, self.y + 8), 1)

class Fighter:
    def __init__(self):

        self.image = pygame.image.load("../images/fighter.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.x = 320
        self.y = 591

        self.missiles = []

    def check_for_actions(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= 3
        if pressed_keys[K_RIGHT] and self.x < 540:
            self.x += 3
        # if pressed_keys[K_SPACE]:
        #     self.fire()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def fire(self):
        self.missiles.append(Missile(self.x + 50))


class Badguy:
    def __init__(self):
        self.image = pygame.image.load("../images/badguy.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.reset()

    def reset(self):
        self.x = random.randint(0, 520)
        self.y = -100
        self.dy = random.randint(2, 6)
        self.dx = random.choice((-1, 1)) * self.dy

    def move(self):
        self.dy += 0.01
        self.y += self.dy
        # self.dx += 0.2
        self.x += self.dx
        # if self.y > 150 and self.y < 250:
        #     self.x += 5
        # if self.y > 250:
        #     self.x -= 5
        self.bounce()

    def bounce(self):
        if self.x < 0 or self.x > 570:
            self.dx *= -1

    def is_off_screen(self):
        return self.y > 640

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


def main():
    last_badguy_spawn_time = 0
    badguys = []

    fighter = Fighter()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_SPACE] and event.type == KEYDOWN:
                fighter.fire()

        screen.fill((0, 0, 0))

        if time.time() - last_badguy_spawn_time > 0.5:
            badguys.append(Badguy())
            last_badguy_spawn_time = time.time()

        for badguy in badguys:
            badguy.move()
            if badguy.is_off_screen():
                badguy.reset()
            badguy.draw()


        for missile in fighter.missiles:
            missile.move()
            if missile.is_off_screen():
                del missile  # TODO: Fix the list mutation issue
                continue
            missile.draw()

        fighter.check_for_actions()
        fighter.draw()

        pygame.display.update()


main()