import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        # TODO. Inititalize this Raindrop, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)


    def move(self):
        # TODO. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.
        pygame.draw.line(self.screen, (255, 255, 0), (self.x, self.y), (self.x, self.y + 50), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        # TODO. Inititalize this Hero, as follows:
        # TODO    - Store the screen.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()

        self.last_hit_time = 0
        # TODO    - Set the initial position of this Hero to x and y.
        # TODO    - Set the image of this Hero WITH an umbrella to the given with_umbrella file.
        # TODO    - Set the image of this Hero WITHOUT an umbrella to the given without_umbrella file.
        # TODO    - Set the "last hit time" to 0.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.



    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        if time.time() > self. last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint(raindrop.x, raindrop.y)




class Cloud:
    def __init__(self, screen, x, y, image):
        # DONE. Inititalize this Cloud, as follows:
        # DONE    - Store the screen.
        self.screen = screen
        # TODO    - Set the initial position of this Cloud to x and y.
        self.x = x
        self.y = y
        # TODO    - Set the image of this Cloud to the given image
        self.image = pygame.image.load(image).convert()
        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        self.raindrops = []
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.


    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        # DONE. Append a new Raindrop to this Cloud's list of Raindrops,\
        self.screen.blit(self.image, (self.x, self.y))
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        new_raindrop = Raindrop(self.screen, random.randint(self.x, self.x + 300),self.y + 100)
        self.raindrops.append(new_raindrop)



def main():
    # DONE: Initialize the game, display a captian, and set   screen   to a 1000x600 Screen.
    print('hello world')
    pygame.init()
    pygame.display.set_caption('rainy day')
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    #single_raindrop = Raindrop (screen, 500, 20)

    # TODO: Make a Clock, Hero and Cloud with appropriate images, starting at appropriate positions.
    cloud = Cloud(screen, 300, 50, "cloud.png")

    mike = Hero(screen, 300, 400, "Mike_umbrella.png", 'Mike.png')
    # TODO: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    # DONE    Make the pygame.QUIT event stop the game.
    while True:
        clock.tick(6000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        cloud.rain()


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

        if pressed_keys[pygame.K_d]:
            mike.x = mike.x + 5
        if pressed_keys[pygame.K_a]:
            mike.x = mike.x - 5




        # TODO: Inside the game loop, draw the screen, Hero and Cloud.
        cloud.draw()

        #single_raindrop.draw()
        #single_raindrop.move()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()

        mike.draw()
        # TODO: Inside the game loop, make the Cloud "rain", and then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
        # TODO      - move the Raindrop.
        # TODO      - draw the Raindrop.
        # TODO      - if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
        # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.

        pygame.display.update()





# DONE: Call main.
main()