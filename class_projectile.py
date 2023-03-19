import pygame

window_width = 1270
window_height = 720
window = pygame.display.set_mode((window_width, window_height))


class projectile():

    def __init__(self, x, y, facing_x, rigth, left, width, height, zone):
        self.x = x
        self.y = y
        self.facing_x = facing_x
        self.vel_x = 20*self.facing_x # the direction of the bullet
        self.image = pygame.image.load('bullet_left.png')
        self.right = rigth
        self.left = left
        self.zone = zone
        self.height = height
        self.width = width
        self.hitBox = (self.x, self.y, self.width, self.height)



    def drawing (self):
        global image

        if self.right:
            self.image = pygame.image.load('projectile/bullet_right.png')

        else:
           self.image = pygame.image.load('projectile/bullet_left.png')



    def draw(self,window):
        global image

        self.drawing()

        self.x += self.vel_x

        window.blit(self.image, (self.x, self.y))
        self.hitBox = (self.x + 17 , self.y+2, self.width, self.height)
        #pygame.draw.rect(window, (255, 0, 0),self.hitBox, 2)

