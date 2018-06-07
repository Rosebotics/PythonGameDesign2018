import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        # TODO. Inititalize this Raindrop, as follows:
        # DONE   - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 18.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)
    def move(self):
        # DONE. Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        # TODO. Return  True  if the y  position of this Raindrop is greater than 800.
        pass

    def draw(self):
        # DONE. Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # DONE    from the current position of this Raindrop.
        pygame.draw.line(self.screen, (4, 6, 255), (self.x, self.y), (self.x, self.y + 5), )



class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        # DONE. Inititalize this Hero, as follows:
        # DONE    - Store the screen.
        self.screen = screen
        # DONE    - Set the initial position of this Hero to x and y.
        self.x = x
        self.y = y
        # TODO    - Set the image of this Hero WITH an umbrella to the given with_umbrella file.
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        # TODO    - Set the image of this Hero WITHOUT an umbrella to the given without_umbrella file.
        self.image_without_umbrella= pygame.image.load(without_umbrella).convert()
        # TODO    - Set the "last hit time" to 0.
        self.last_hit_time = 0
        # TODO  Use instance variables:

        # TODO     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.



    def draw(self):
        # TODO. Draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.

        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
        # TODO: Return True if this Hero is currently colliding with the given Raindrop.
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))

class Cloud:
    def __init__(self, screen, x, y, image):
        # DONE. Inititalize this Cloud, as follows:
        # DONE - Store the screen.
        self.screen = screen
        # DONE    - Set the initial position of this Cloud to x and y.
        self.x = x
        self.y = y
        # DONE    - Set the image of this Cloud to the given image.
        self.image = pygame.image.load(image).convert()
        # DONE    - Set the list of Raindrop objects for this Cloud to the empty list.
        self.raindrops = []

    def draw(self):
        # TODO. Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def rain(self):

        new_raindrop = Raindrop(self.screen, random.randint(self.x, self.x + 300), self.y + 100)
        self.raindrops.append(new_raindrop)


def main():

    print('Ready!')
    pygame.init()
    pygame.display.set_caption('Rain.')
    screen=pygame.display.set_mode((1000, 600))

    clock=pygame.time.Clock()


    Jeff = Hero(screen, 300, 400, 'Mike_umbrella.png', 'Mike.png')

    cloud = Cloud(screen, 300, 50, "cloud.png")
    cloud.rain()
    cloud.rain()
    cloud.rain()
    cloud.rain()


    # single_raindrop = Raindrop(screen, 500, 20)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        cloud.rain()
        cloud.rain()
        cloud.rain()
        cloud.rain()




        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 10
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 10
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 10
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 10

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d]:
            Jeff.x = Jeff.x + 10
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            Jeff.x = Jeff.x - 10
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            Jeff.y = Jeff.y - 10
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_s]:
            Jeff.y = Jeff.y + 10

        cloud.draw()
        Jeff.draw()
        # single_raindrop.move()
        # single_raindrop.draw()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if Jeff.hit_by(raindrop):

                Jeff.last_hit_time = time.time()


            Jeff.draw()


        pygame.display.update()


# DONE: Call main.
main()