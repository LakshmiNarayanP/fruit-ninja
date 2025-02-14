import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('fruit-ninja')
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

Images = [pygame.image.load('Assets/apple.png'), pygame.image.load('Assets/banana.png'), pygame.image.load('Assets/orange.png'), pygame.image.load('Assets/pineapple.png'), pygame.image.load('Assets/watermelon.png')]

class Fruit:
    def __init__(self, img):
        self.img = img
        self.x = 400
        self.y = 750
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.vel = random.randint(-20, 20)
        self.gravity = random.randint(-22, -20)
        self.angle = random.randint(0, 355)

    def draw(self):
        screen.blit(pygame.transform.rotate(self.img, self.angle), (self.x, self.y))

    def movement(self):
        self.x += self.vel
        self.y += self.gravity
        self.gravity += 0.35
        if self.vel > 0:
            self.vel -= 0.25
        if self.vel < 0:
            self.vel += 0.25
        if self.x + self.width >= 800 or self.x <= 0:
            self.vel *= -1
        self.angle = (self.angle + 1) % 360

    def update(self):
        self.draw()
        self.movement()

Fruits=[]
for i in range(random.randint(2, 3)): #no. of fruits spawned at a time
    choice = random.randint(0, 4)#choosing the type of fruit
    Fruits.append(Fruit(Images[choice]))

background = pygame.image.load('Assets/background.png')
while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for fruit in Fruits:
        fruit.update()
    #this loop is for spawning fruits after the first time
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            for i in range(random.randint(2, 3)):  # no. of fruits spawned at a time
                choice = random.randint(0, 4)  # choosing the type of fruit
                Fruits.append(Fruit(Images[choice]))
    

    pygame.display.update()
    clock.tick(50)#speed


