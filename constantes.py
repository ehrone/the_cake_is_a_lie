import pygame

zone=place="village.png"

#variables texte

texte0=pygame.Surface((0,0))
texte1=pygame.Surface((0,0))
texte2=pygame.Surface((0,0))
texte3=pygame.Surface((0,0))

bloc=pygame.Surface((0,0))
talk=pygame.Surface((0,0))

n=100
b=0
n4=4
n0=0
b = 0
#variables texte

Xmax=1270
Ymax = 720

window = pygame.display.set_mode((Xmax, Ymax))

bullets = []

x = 400
y = 400
width = 50
height = 60
vel = 8

#variables animation perso
walkRight = [pygame.image.load('Manon/RIGHT/1.png'), pygame.image.load('Manon/RIGHT/2.png'), pygame.image.load('Manon/RIGHT/3.png'), pygame.image.load('Manon/RIGHT/4.png'), pygame.image.load('Manon/RIGHT/5.png'), pygame.image.load('Manon/RIGHT/6.png'), pygame.image.load('Manon/RIGHT/7.png'), pygame.image.load('Manon/RIGHT/8.png'), pygame.image.load('Manon/RIGHT/9.png')]
walkLeft = [pygame.image.load('Manon/LEFT/1.png'), pygame.image.load('Manon/LEFT/2.png'), pygame.image.load('Manon/LEFT/3.png'), pygame.image.load('Manon/LEFT/4.png'), pygame.image.load('Manon/LEFT/5.png'), pygame.image.load('Manon/LEFT/6.png'), pygame.image.load('Manon/LEFT/7.png'), pygame.image.load('Manon/LEFT/8.png'), pygame.image.load('Manon/LEFT/9.png')]
walkUp = [pygame.image.load('Manon/UP/1.png'), pygame.image.load('Manon/UP/2.png'), pygame.image.load('Manon/UP/3.png'), pygame.image.load('Manon/UP/4.png'), pygame.image.load('Manon/UP/5.png'), pygame.image.load('Manon/UP/6.png'), pygame.image.load('Manon/UP/7.png'), pygame.image.load('Manon/UP/8.png'), pygame.image.load('Manon/UP/9.png')]
walkDown = [pygame.image.load('Manon/DOWN/1.png'), pygame.image.load('Manon/DOWN/2.png'), pygame.image.load('Manon/DOWN/3.png'), pygame.image.load('Manon/DOWN/4.png'), pygame.image.load('Manon/DOWN/5.png'), pygame.image.load('Manon/DOWN/6.png'), pygame.image.load('Manon/DOWN/7.png'), pygame.image.load('Manon/DOWN/8.png'), pygame.image.load('Manon/DOWN/9.png')]
charUP = pygame.image.load('Manon/UP/1.png')
charDOWN = pygame.image.load("Manon/DOWN/1.png")
#variables animation perso

#variables animation ennemy
goblinRight = [pygame.image.load('goblin/R1E.png'), pygame.image.load('goblin/R2E.png'), pygame.image.load('goblin/R3E.png'), pygame.image.load('goblin/R4E.png'), pygame.image.load('goblin/R5E.png'), pygame.image.load('goblin/R6E.png'), pygame.image.load('goblin/R7E.png'), pygame.image.load('goblin/R8E.png'), pygame.image.load('goblin/R9E.png'), pygame.image.load('goblin/R10E.png'), pygame.image.load('goblin/R11E.png')]
goblinLeft = [pygame.image.load('goblin/L1E.png'), pygame.image.load('goblin/L2E.png'), pygame.image.load('goblin/L3E.png'), pygame.image.load('goblin/L4E.png'), pygame.image.load('goblin/L5E.png'), pygame.image.load('goblin/L6E.png'), pygame.image.load('goblin/L7E.png'), pygame.image.load('goblin/L8E.png'), pygame.image.load('goblin/L9E.png'), pygame.image.load('goblin/L10E.png'), pygame.image.load('goblin/L11E.png')]

dogRight = [pygame.image.load('dog/1.png'), pygame.image.load('dog/2.png'), pygame.image.load('dog/3.png'), pygame.image.load('dog/4.png'), pygame.image.load('dog/5.png'), pygame.image.load('dog/6.png'), pygame.image.load('dog/7.png'), pygame.image.load('dog/8.png')]

fishLeft = [pygame.image.load('fish/1.png'), pygame.image.load('fish/2.png')]

beeUp = [pygame.image.load('bee/1.png'), pygame.image.load('bee/2.png')]


keys = pygame.key.get_pressed()

facing_x = 1


