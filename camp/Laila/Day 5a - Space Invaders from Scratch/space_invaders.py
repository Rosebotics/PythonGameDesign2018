import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x):
      self.exploded = False
      self.y = 591
      self.screen = screen
      self.x = x

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        self.y =self.y - 5

    def draw(self):
        # Draw a horizontal, 1-pixel thick, 8 pixels long, red line on the screen,
        # where the line starts at the current position of this Missile.
        pygame.draw.line(self.screen, (255,0,0),
                         (self.x, self.y),
                         (self.x,self.y + 8),
                         1)



class Fighter:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image. and set its colorkey to white.

        self.screen = screen
        self.x = x
        self.y = y
        self.miss = []
        self.image = pygame.image.load("fighter.png").convert()
        self.image.set_colorkey((255,255,255))



    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x,self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        m = Missile (self.screen,self.x + 60)
        self.miss.append(m)

    def remove_exploded_missles(self):
        for k in range(len(self.miss) - 1, -1, -1):
            if self.miss[k].exploded or self.miss[k].y < 0:
                del self.miss[k]



class Badguy:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   dead to False   and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("badguy.png").convert()
        self.image.set_colorkey((0,0,0))
        self.moving_right = True
        self.original_x = x
        self.dead = False

    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        if self.moving_right:
            self.x = self.x + 2
            if self.x > self.original_x + 100:
                self.moving_right = False
        else:
            self.x = self.x - 2
            if self.x < self.original_x - 100:
                self.moving_right = True

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with a point the given missile's current position.
        # Return False otherwise.
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(missile.x, missile.y)



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
        return  len(self.badguys) == 0

    def move(self):
        # Make each badguy in this EnemyFleet move.
        for badguy in self.badguys:
            badguy.move()


    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.
        for badguy in self.badguys:
            badguy.draw()

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
            if pressed_keys[pygame.K_SPACE] and event.type == KEYDOWN:
                fighter.fire()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # TODO: If K_LEFT is pressed move the fighter left 3
        # TODO: If K_RIGHT is pressed move the fighter right 3
        # TODO: Draw the fighter
        if pressed_keys[pygame.K_LEFT]:
            fighter.x = fighter.x - 3
        if pressed_keys[pygame.K_RIGHT]:
            fighter.x = fighter.x + 3
        fighter.draw()

        # TODO: Move the enemy
        # TODO: Draw the enemy
        # TODO: Draw the missle
        enemy.move( )
        enemy.draw()
        # TODO: For each missle in the fighter missiles
        # TODO: Move the missle
        for m in fighter.miss:
            m.move()
            m.draw()

        # TODO: For each badguy in the enemy badguys
        #     TODO: For each missle in the fighter missiles
        #         TODO: If the badguy is hit by the missle
        #             TODO: Mark the badguy as dead = True
        #             TODO: Mark the missile as exploded = True
        for badguy in enemy.badguys:
            for m in fighter.miss :
                if badguy.hit_by(m):
                    badguy.dead = True
                    m.exploaded = True


        # TODO: Use the fighter to remove exploded missiles
        # TODO: Use the enemy to remove dead badguys
        fighter.remove_exploded_missles()
        enemy.remove_dead_badguys()

        # TODO: If the enemy id_defeated
        #     TODO: Increment the enemy_rows
        #     TODO: Create a new enemy with the screen and enemy_rows
        if enemy.is_defeated:
            enemy_rows = enemy_rows + 1
            enemy = EnemyFleet(screen, enemy_rows)
        pygame.display.update()


main()
