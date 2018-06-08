import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.y = 591
        self.exploded = False
        # TODO: Save the screen into a field
        # TODO: Save the x into a field
        # TODO: Set the y to 591 as a field (which is just above the fighter)
        # TODO: Set a field called exploded to False


    def move(self):
        # TODO: Move the missile up 5
        self.y = self.y - 5

    def draw(self):
        # TODO: Draw a red line from x, y that is 8 pixels in height
        pygame.draw.line(self.screen, (255, 0, 0), (self.x, self.y),(self.x, self.y - 8 ), 4)


class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("fighter.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.missiles = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        self.missiles.append(Missile(self.screen, self.x + 50))

    def remove_exploded_missles(self):
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y):
        self.dead = False
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("badguy.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.original_x = x
        self.moving_right = True

    def move(self):
        if self.moving_right:
            self.x = self.x + 2
            if self.x > self.original_x + 100:
                self.moving_right = False
                self.y = self.y + 15
        else:
            self.x = self.x - 2
            if self.x < self.original_x - 100:
                self.moving_right = True
                self.moving_right = True
                self.y = self.y + 15
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(missile.x, missile.y)


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20))

    @property
    def is_defeated(self):
        return len(self.badguys) == 0

    def move(self):
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].dead:
                del self.badguys[k]


def main():
    game_over = False
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((640, 650))

    # DONE: Set    enemy_rows    to an initial value of 3.
    enemy_rows = 3
    # DONE: Create an EnemyFleet object (called enemy) with the screen and enemy_rows
    enemy = EnemyFleet(screen, enemy_rows)
    # DONE: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen, 320, 590)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # DONE: If the event type is KEYDOWN and pressed_keys[K_SPACE} is True, then fire a missile
            # if pressed_keys[pygame.K_SPACE]:
            #     fighter.fire()
            if event.type == QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT] and fighter.x < (640 - 50):
            fighter.x = fighter.x + 10
        if pressed_keys[pygame.K_LEFT] and fighter.x > (0 - 50):
            fighter.x = fighter.x - 10
        if pressed_keys[pygame.K_SPACE]:
         fighter.fire()






        # TODO: Draw the fighter
        fighter.draw()

        # TODO: Move the enemy
        enemy.move()
        # TODO: Draw the enemy
        enemy.draw()

        # TODO: For each missle in the fighter missiles
        # TODO: Move the missle
        # TODO: Draw the missle
        for missile in fighter.missiles:
            missile.move()
            missile.draw()
        # TODO: For each badguy in the enemy badguys
        #     TODO: For each missle in the fighter missiles
        #         TODO: If the badguy is hit by the missle
        #             TODO: Mark the badguy as dead = True
        #             TODO: Mark the missile as exploded = True
        for badguy in enemy.badguys:
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    badguy.dead = True
                    missile.exploded = True

        # TODO: Use the fighter to remove exploded missiles
        fighter.remove_exploded_missles()
        # TODO: Use the enemy to remove dead badguys
        enemy.remove_dead_badguys()

        # TODO: If the enemy id_defeated
        #     TODO: Increment the enemy_rows
        #     TODO: Create a new enemy with the screen and enemy_rows
        if enemy.is_defeated:
            enemy_rows = enemy_rows + 1
            enemy = EnemyFleet(screen, enemy_rows)

        for badguy in enemy.badguys:
            if badguy.y > 590:
                game_over = True
                print("You just lost!")
                game_over = True



        if not game_over:
            pygame.display.update()


main()
