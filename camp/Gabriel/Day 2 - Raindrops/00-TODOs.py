import pygame
import random
import sys
import time



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
        self.speed = random.randint(5,18)

    def move(self):
        # TODO. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed


    def off_screen(self):
        # TODO. Return  True  if the  y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # TODO. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO    from the current position of this Raindrop.
        pygame.draw.line(self.screen, (0, 0, 50, ), (self.x, self.y), (self.x, self.y + 5), 2)





class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        # TODO. Inititalize this Hero, as follows:
        # TODO    - Store the screen.
        self.screen = screen
        # ODNE    - Set the initial position of this Hero to x and y.
        self.x = x
        self.y = y
        # TODO    - Set the image of this Hero WITH an umbrella to the given with_umbrella file.
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        # TODO    - Set the image of this Hero WITHOUT an umbrella to the given without_umbrella file.
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()
        # TODO    - Set the "last hit time" to 0.
        self.last_hit_time = 0
        # TODO  Use instance variables:
        # TODO     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.



    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))


        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.



    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))


class Cloud:
    def __init__(self, screen, x, y, image):
        # DONE. Inititalize this Cloud, as follows:
        # DONE    - Store the screen.
        self.screen = screen
        # TODO    - Set the initial position of this Cloud to x and y.
        self.x = x
        self.y = y
        # TODO    - Set the image of this Cloud to the given image.
        self.image = pygame.image.load(image).convert()
        # TODO    - Set the list of Raindrop objects for this Cloud to the empty list.
        self.raindrops = []


    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))


    def rain(self):
        # TODO. Append a new Raindrop to this Cloud's list of Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        new_raindrop = Raindrop(self.screen, random.randint(self.x, self.x + 300), self.y + 100)
        self.raindrops.append(new_raindrop)






def main():
    # DONE: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    print("READY!")
    pygame.init()
    pygame.display.set_caption("RAINDROPS")



    screen = pygame.display.set_mode( (1000, 650) )

    #DONE: Make a Clock
    clock = pygame.time.Clock()
    # TODO: Make a Cloud with appropriate images, starting at appropriate positions.
    cloud = Cloud(screen, 300, 50, "cloud.png")





    #TODO Make a Hero
    Luigi = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png" )
    single_raindrop = Raindrop(screen, 500, 50)

    # DONE: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    # DONE    Make the pygame.QUIT event stop the game.
    while True:
        cloud.draw()
        cloud.rain()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # TODO: Inside the game loop, get the list of keys that are currently pressed.
        # TODO    Arrange so that the Cloud moves:
        # TODO      1 pixel to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.


        # TODO      1 pixel to the left if the Left Arrow key (pygame.K_LEFT) is pressed.
        # TODO      1 pixel up if the Up Arrow key (pygame.K_UP) is pressed.
        # TODO      1 pixel down if the Down Arrow key (pygame.K_DOWN) is pressed.
       #Move the cloud
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 10
        if pressed_keys[pygame.K_DOWN]:
          cloud.y = cloud.y + 10
        if pressed_keys[pygame.K_UP]:
            cloud.y =   cloud.y - 10

    #Move Hero
        if pressed_keys[pygame.K_d]:
            Luigi.x = Luigi.x + 10
        if pressed_keys[pygame.K_a]:
            Luigi.x = Luigi.x - 10
        if pressed_keys[pygame.K_s]:
            Luigi.y = Luigi.y + 10
        if pressed_keys[pygame.K_w]:
            Luigi.y = Luigi.y - 10
        # TODO: Inside the game loop, draw the screen, Hero and Cloud.
        screen.fill((255, 255, 255))
        cloud.draw()
        Luigi.draw()
        # single_raindrop.move()
        # single_raindrop.draw()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if Luigi.hit_by(raindrop):
                Luigi.last_hit_time = time.time()



        # TODO: Inside the game loop, make the Cloud "rain", and then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
        # TODO      - move the Raindrop.
        # TODO      - draw the Raindrop.
        # TODO      - if the Hero  hit by a Raindrop, set the Hero's last_time_hit to the current time.
        # TODO      - if the Raindrop is off the screen, delete it from the Cloud's list of Raindrops.

        pygame.display.update()


#DONE TODO: Call main.
main()