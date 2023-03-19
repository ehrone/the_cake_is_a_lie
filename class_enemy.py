import pygame
from constantes import *
import random


class enemy :

    def __init__(self, x, y, zone, distance, width, height, life):
        self.x = x
        self.y = y
        self.distance = distance
        self.width = width
        self.height = height
        self.x_init = x
        self.y_init = y
        self.zone = zone
        self.vel = 8
        self.limit_left = x - distance
        self.limit = self.distance + x
        self.limit_y = y - int(distance)
        self.life = life
        self.right = False
        self.left = False
        self.up = False
        self.walkEnemy = 0
        self.hitBox = (self.x + 17 , self.y + 2, 31, 57)


    def hit(self):
        self.life -= 1
        print("hit !")


class goblin(enemy):

    def movement(self):
        """ the deplacement of the goblin"""
        if self.vel > 0:

            if self.x > self.limit:
                self.vel = -13

            else :
                self.x += self.vel
                self.right = True
                self.left = False

        elif self.vel < 0 :
            if self.x < self.x_init :
                self.vel = 13

            else:
                self.x += self.vel
                self.right = False
                self.left = True

    def draw(self):
        """ the animation of the goblin """

        if self.walkEnemy == 8:
            self.walkEnemy = 0

        if self.right :
            window.blit(goblinRight[self.walkEnemy], (self.x, self.y))
            self.walkEnemy +=1

        elif self.left :
            window.blit(goblinLeft[self.walkEnemy], (self.x, self.y))
            self.walkEnemy +=1

        self.hitBox = (self.x + 17 , self.y+2, self.width, self.height)
        #pygame.draw.rect(window, (255, 0, 0),self.hitBox, 2)

    def main(self):
        """ the fonction wuch gather the movement and the animation of the goblin """
        if self.life != 0 :
            self.movement()
            self.draw()



class dog (enemy):

    def movement(self):
        if self.vel > 0:

            if self.x > self.limit:
                self.vel = -13

            else :
                self.x += self.vel
                self.right = True
                self.left = False

        elif self.vel < 0 :

            if self.x < self.x_init :
                self.vel = 13

            else:
                self.x += self.vel
                self.right = False
                self.left = True

    def draw(self):
        if self.walkEnemy == 8:
            self.walkEnemy = 0

        elif self.right or self.left :
            window.blit(dogRight[self.walkEnemy], (self.x, self.y))
            self.walkEnemy +=1

        self.hitBox = (self.x - 5 ,self.y, self.width, self.height)
        #pygame.draw.rect(window,(255, 0, 0),self.hitBox, 2)

    def main(self):
        if self.life != 0 :
            self.movement()
            self.draw()





class fish(enemy):


    def movement(self):
        if self.x < self.limit_left:

            self.x = self.x_init
            self.y = self.y_init

        else :

            self.y = self.y_init
            self.x -= 30


    def draw(self):

        if self.walkEnemy == 2:
            self.walkEnemy = 0

        if self.x > 648 or self.x < 450 :  #fish must not be showed on the bridge

            window.blit(fishLeft[self.walkEnemy], (self.x, self.y))
            self.walkEnemy +=1

        self.hitBox = (self.x - 5,self.y, self.width, self.height)
        #pygame.draw.rect(window,(255, 0, 0),self.hitBox, 2)


    def main(self):
        if self.life != 0 :
            self.movement()
            self.draw()




class bee (enemy):

    def movement(self):
        #print(self.limit_y,self.y,self.y_init)

        if self.y < self.limit_y:
            self.y = self.y_init
            self.x = self.x_init


        else :
            self.y -= 20
            self.x = self.x_init



    def draw(self):
        if self.walkEnemy == 2:
            self.walkEnemy = 0

        #print(self.x,self.y)

        window.blit(beeUp[self.walkEnemy], (self.x, self.y))
        self.walkEnemy +=1

        self.hitBox = (self.x - 5 ,self.y - 5, self.width, self.height)
        #pygame.draw.rect(window,(255, 0, 0),self.hitBox, 2)



    def main(self):
        if self.life !=0:

            self.movement()
            self.draw()


class octopus(enemy):


    def movement(self):
        if self.y < self.limit_y or self.x < 0 or self.x > 1270:  #staying in the sxreen
            self.y = self.y_init
            self.x = self.x_init

        else :
            self.y -= random.randint(10, 150)  #making complete random movements
            self.y += random.randint(3, 50)

            self.x += random.randint(5, 100)
            self.x -= random.randint(3, 30)




    def draw(self):
        window.blit(pygame.image.load('octo.png'), (self.x, self.y))

        self.hitBox = (self.x - 5 ,self.y - 5, self.width, self.height)
        #pygame.draw.rect(window,(255, 0, 0),self.hitBox, 2)



    def main(self):
        if self.life != 0 :
            self.movement()
            self.draw()
