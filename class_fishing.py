import pygame
from constantes import*


class fishing :

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 15
        self.can = (0,0,0,0)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:   #left

            self.x -= self.vel

        if keys[pygame.K_h]:   #right

            self.x += self.vel

        if keys[pygame.K_t]:  #up

            self.y -= self.vel

        if keys[pygame.K_g]:  #down

            self.y += self.vel


    def draw(self) :
        global window

        self.can = (self.x ,self.y , 10, 10)
        pygame.draw.rect(window,(0, 0, 0), self.can, 0)


    def main(self) :
        self.move()
        self.draw()





