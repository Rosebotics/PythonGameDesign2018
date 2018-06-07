import pygame
import sys
import time  # Note this!
import random  # Note this!

kpos = 200



class Raindrop:
    def __init__(self, screen, x,y,image):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen=screen
        self.x=x
        self.image=image
        self.y=y
        self.image=pygame.image.load(self.image).convert()
        self.image=pygame.transform.scale(self.image,(10,15))



    def move(self):
        # TODO. Change the  y  position of this Raindrop by its speed.
        pass

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.
        self.screen.blit(self.image,(self.x,self.y))


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):

        # TODO  Use instance variables:
        # TODO     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.screen = screen
        self.x = x
        self.y = y
        self.with_umbrella = with_umbrella
        self.without_umbrella = without_umbrella
        self.last_hit_time = 0
        self.image_umbrella = pygame.image.load(self.with_umbrella).convert()
        pass

    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        self.screen.blit(self.image_umbrella,(self.x,self.y))

    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy







    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        pass


class Cloud:
    def __init__(self, screen, x, y, image):
        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.
        self.screen=screen
        self.x=x
        self.y=y
        self.image=image
        self.image_cloud = pygame.image.load(self.image).convert()
        self.direction=1
    def draw(self):
        self.screen.blit(self.image_cloud,(self.x,self.y))

    def move(self,dx,dy):
        self.x=self.x+(dx*self.direction)
        self.y=self.y+dy
        if self.x>700:
            self.direction=-1
        elif self.x<0:
            self.direction=1
    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        # random x= random.randint(0, 300)=+self.x
        # raindrop= Raindrop(self.screen,random_x,self.y+100,"raindrop_png_file")
        pass
def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("raindrops")
    # TODO: Make a Clock, Hero and Cloud with appropriate images, starting at appropriate positions.
    clock = pygame.time.Clock()
    hero = Hero(screen, 0, 500, "Mike_umbrella.png", "Mike.png")
    cloud = Cloud(screen,150,50,"cloud.png")
    raindrop=Raindrop(screen,150,147,"raindrop.png")
    # TODO: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    # TODO    Make the pygame.QUIT event stop the game.

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        hero.draw()
        cloud.draw()
        raindrop.draw()
        pygame.display.update()
        screen.fill((255,255,255))
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            hero.move(2,0)
        if pressed_keys[pygame.K_LEFT]:
            hero.move(-2,0)
        if pressed_keys[pygame.K_UP]:
            hero.move(0,-2)
        if pressed_keys[pygame.K_DOWN]:
            hero.move(0,2)
        if pressed_keys[pygame.K_SPACE]:
            hero.move(0,-5)
        if pressed_keys[pygame.K_a]:
            cloud.move(-1,0)
        if pressed_keys[pygame.K_s]:
            cloud.move(0, 1)
        if pressed_keys[pygame.K_w]:
                cloud.move(0, -1)
        if pressed_keys[pygame.K_d]:
            cloud.move(1, 0)
        cloud.move(1,0)




    # TODO: Inside the game loop, draw the screen, Hero and Cloud.

    # TODO: Inside the game loop, make the Cloud "rain", and then:
    # TODO    For each Raindrop in the Cloud's list of raindrops:
    # TODO      - move the Raindrop.
    # TODO      - draw the Raindrop.
    # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
    # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.
    pass


# TODO: Call main.
main()
