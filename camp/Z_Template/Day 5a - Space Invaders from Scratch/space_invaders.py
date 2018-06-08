import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x):
        # Store the data.  Initialize:   y to 591   and   exploded to False.

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).

    def draw(self):
        # Draw a horizontal, 1-pixel thick, 8 pixels long, red line on the screen,
        # where the line starts at the current position of this Missile.

class Fighter:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image. and set its colorkey to white.

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.

    def fire(self):
        self.missiles.append(Missile(self.screen, self.x + 50))

    def remove_exploded_missles(self):
        # for k in range(len(self.missiles) - 1, -1, -1):
            # if self.missiles[k].exploded or self.missiles[k].y < 0:
                # del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   dead to False   and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.

    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with a point the given missile's current position.
        # Return False otherwise.


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.

    def move(self):
        # Make each badguy in this EnemyFleet move.

    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].dead:
                del self.badguys[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((640, 650))

    # TODO: Set    enemy_rows    to an initial value of 3.
    # TODO: Create an EnemyFleet object (called enemy) with the screen and enemy_rows
    # TODO: Create a Fighter (called fighter) at location  320, 590
    enemy_rows = 3
    enemy = EnemyFleet(screen, enemy_rows)
    fighter = Fighter(screen, 320, 590)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # TODO: If the event type is KEYDOWN and pressed_keys[K_SPACE} is True, then fire a missile
            if event.type == QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # TODO: If K_LEFT is pressed move the fighter left 3
        # TODO: If K_RIGHT is pressed move the fighter right 3
        # TODO: Draw the fighter

        # TODO: Move the enemy
        # TODO: Draw the enemy
        enemy.draw()

        # TODO: For each missle in the fighter missiles
        # TODO: Move the missle
        # TODO: Draw the missle
        for missile in fighter.missiles:
            missile.draw()

        # TODO: For each badguy in the enemy badguys
        #     TODO: For each missle in the fighter missiles
        #         TODO: If the badguy is hit by the missle
        #             TODO: Mark the badguy as dead = True
        #             TODO: Mark the missile as exploded = True


        # TODO: Use the fighter to remove exploded missiles
        # TODO: Use the enemy to remove dead badguys


        # TODO: If the enemy id_defeated
        #     TODO: Increment the enemy_rows
        #     TODO: Create a new enemy with the screen and enemy_rows

        pygame.display.update()


main()
