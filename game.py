from pygame import *
from constantes import *
from class_player import*
from class_enemy import*
from class_fishing import*
from class_projectile import *


x = 400
y = 400

pygame.init()

window = pygame.display.set_mode((Xmax, Ymax))

pygame.display.set_caption("The cake is a lie")

run = True

perso = player(x,y,width,height)


dog1 = dog(533,272,"backgrounds/foret_road.png",1125-533, 138, 83, 3)

fish1 = fish(1280,360,"backgrounds/fleuve_1.png",1280, 64, 37, 3)

# the bee enemies
bee1 = bee(1000, 600,"backgrounds/fleuve_2.png",600, 32, 32, 3)
bee2 = bee(800, 700,"backgrounds/fleuve_2.png",700, 32, 32, 3)
bee3 = bee(1100, 800,"backgrounds/fleuve_2.png",800, 32, 32, 3)
bee4 = bee(400, 650,"backgrounds/fleuve_2.png",650, 32, 32, 3)

# the octopus enemies
octopus1 = octopus(400, 700,"backgrounds/fleuve_3.png",800, 82, 82, 3)
octopus2 = octopus(0, 800,"backgrounds/fleuve_3.png",900, 82, 82, 3)
octopus3 = octopus(200, 650,"backgrounds/fleuve_3.png",750, 82, 82, 3)

# the goblin enemies
goblin_1 = goblin( 500, 300, 'backgrounds/desert_1.png',  600, 64, 64, 3)
goblin_2 = goblin(500, 300, 'backgrounds/desert_2.png', 600, 64, 64, 3)

fishing_can = fishing(x,y + 100)



# the list for the monsters apparitions

nb_enemy = 0 #number of enemies
enemy_liste= []  #enemies's list

def presence_enemy ():
    print("enemy here")
    """ The fonction wich is in charge of 'calling' the enemies"""
    global nb_enemy, enemy_liste

    print(perso.zone, bee1.zone)

    if perso.zone == dog1.zone :
        dog1.main()

        enemy_liste = []  #on remet la liste à zéro

        nb_enemy = 1
        enemy_liste.append(dog1)

    elif perso.zone == fish1.zone :
        fish1.main()

        enemy_liste= []

        nb_enemy = 1
        enemy_liste.append(fish1)

    elif perso.zone == bee2.zone :
        bee1.main()
        bee2.main()
        bee3.main()
        bee4.main()

        enemy_liste= []

        nb_enemy = 4
        enemy_liste.append(bee1)
        enemy_liste.append(bee2)
        enemy_liste.append(bee3)
        enemy_liste.append(bee4)


    elif perso.zone == octopus1.zone :
        octopus1.main()
        octopus2.main()
        octopus3.main()

        enemy_liste= []

        nb_enemy = 3
        enemy_liste.append(octopus1)
        enemy_liste.append(octopus2)
        enemy_liste.append(octopus3)


    elif goblin_2.life > 0 and perso.zone == goblin_2.zone:
        goblin_2.main()

        enemy_liste= []
        nb_enemy = 1
        enemy_liste.append(goblin_2)


    elif goblin_1.life > 0 and perso.zone == goblin_1.zone:
        goblin_1.main()

        enemy_liste= []
        nb_enemy = 1
        enemy_liste.append(goblin_1)

    if perso.can == 1 :

        fishing_can.main()

        if fish1.hitBox[0] < fishing_can.can[0] and fish1.hitBox[0] + fish1.hitBox[2] > fishing_can.can[0] + fishing_can.can[2] : #collision x

            if fish1.hitBox[1] < fishing_can.can[1] and fish1.hitBox[1] + fish1.hitBox[3] > fishing_can.can[1] + fishing_can.can[3] : #collision y

                fish1.life = 0
                perso.fish = 1




    print(enemy_liste,nb_enemy)


def bullet():

    global facing_x, facing_y

    # variable qui prends la touche du clavier
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and perso.arme == 1 and perso.life > 0:

        if perso.right:
            facing_x = 1


        else :
            facing_x = -1

        if len(bullets) == 0 :
            bullets.append(projectile(perso.x, perso.y,facing_x, perso.right, perso.left, 37, 15,  perso.zone))

    for bullet in bullets:
        if bullet.x > 0 and bullet.x < 1270 and bullet.y > 0 and bullet.y < 720:
            bullet.draw(window)

        else:
            bullets.pop(bullets.index(bullet))


def attack(nb_enemy, enemy_liste):

    for bullet in bullets:

        for i in range (nb_enemy):
            # to avoid the out of range
            if enemy_liste[i].zone == bullet.zone:

                print("in the area")

                if (bullet.hitBox[0] + bullet.hitBox[2]) >= enemy_liste[i].hitBox[0] and bullet.hitBox[0] <= (enemy_liste[i].hitBox[0] + enemy_liste[i].hitBox[2]) :

                    print("check one ")

                    if bullet.hitBox[1] >= enemy_liste[i].hitBox[1] and  ( bullet.hitBox[1] + bullet.hitBox[3]) <= (enemy_liste[i].hitBox[1] + enemy_liste[i].hitBox[3]):

                        print("touché")
                        enemy_liste[i].hit()
                        bullets.pop(bullets.index(bullet))

    print(enemy_liste,nb_enemy)


    for i in range(nb_enemy):

        # to avoid the out of range
        if enemy_liste[i].zone == perso.zone:

            print("in the area")

            if (perso.hitBox[0] + perso.hitBox[2]) >= enemy_liste[i].hitBox[0] and perso.hitBox[0] <= (enemy_liste[i].hitBox[0] + enemy_liste[i].hitBox[2]) :

                print("check one ")

                if (perso.hitBox[1] + perso.hitBox[3]) >= enemy_liste[i].hitBox[1] and  ( perso.hitBox[1]) <= (enemy_liste[i].hitBox[1] + enemy_liste[i].hitBox[3]):
                    # even if the enemy is dead there is still its hitbox
                    if enemy_liste[i].life > 0:
                        print(" Manon touché !!!!!!!")
                        perso.hit()
                        print("-1")


def redraw_Window():
    """ Fonction nous permettant de changer l'image assignée au personnage en fonction des actions demandées"""
    global nb_enemy , enemy_liste

    # the character animation + all of of the others player's fonction
    perso.draw(window)

    #if an enemy is on map
    presence_enemy()

    bullet()



    #concerning the bullet
    attack(nb_enemy, enemy_liste)

    pygame.display.update()


while run:


    pygame.time.delay(5)
    # if the player wants to close the window
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            run = False

    # the fonction which link the different class and display of the game
    redraw_Window()
    print(perso.x , perso.y)


pygame.quit()