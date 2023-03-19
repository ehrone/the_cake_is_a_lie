﻿import pygame
from constantes import*
from math import*
import time


class player :

    def __init__(self,x, y, height, width):
        self.x = x
        self.y = y
        self.vel = 8
        self.height = height
        self.width = width
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.zone="backgrounds/foret_village.png"
        self.back = pygame.image.load(self.zone)
        self.hitBox = (self.x -5 , self.y -2, self.width , self.height +35)
        self.life = 1

        #variables texte

        self.t=0  #when text must be printed
        self.dia=0  #when dialogue can show up
        self.erase=0  #when text has to be erase
        self.tLong=0  #when text is too long to be displayed in one shot
        self.i=0  #counting turns for tLong fonction
        self.lignes=[]  #list of lines for the text
        self.n2=0  #number of lines
        self.n3=0  #number of lines' turns

        self.texte0="" #text surface
        self.texte1=""
        self.texte2=""
        self.texte3=""
        self.bloc=pygame.image.load("transparent.png") #text background

        self.message=""  #text variable
        self.start= 1  #beginning text variable

        #variables texte

        #variables histoire/armes/objets

        self.arme = 0
        self.a_d = 0 #variable demande arme
        self.mission1 = 0
        self.can = 0
        self.fish = 0


        #variables histoire/armes/objets

    def hit(self):
        global  walkRight, walkLeft, walkUp, walkDown, charUP,  charDOWN

        self.life -=1

        walkRight = [pygame.image.load('mort/RIP.png')]
        walkLeft = [pygame.image.load('mort/RIP.png')]
        walkUp = [pygame.image.load('mort/RIP.png')]
        walkDown = [pygame.image.load('mort/RIP.png')]
        charUP = pygame.image.load('mort/RIP.png')
        charDOWN = pygame.image.load('mort/RIP.png')

    def you_are_dead(self):
        self.x = self.x
        self.y = self.y

    """###BACKGROUND"""

    def backGround(self):

        keys = pygame.key.get_pressed()



        #DESERT

        if self.zone == 'backgrounds/desert_1.png':

            if self.x < 0:
                # changing the character zone and so the background
                self.zone = 'backgrounds/sand_village.png'
                self.x = 1259
                self.y = self.y


            elif self.y > 692:
                # changing the character zone and so the background
                self.zone = 'backgrounds/sand_oasis.png'
                # we put the character at the top of the new area
                self.x = self.x
                self.y = 0

        elif self.zone == 'backgrounds/desert_2.png':

            if self.x > 1260:
                # changing the character zone and so the background
                self.zone = 'backgrounds/sand_oasis.png'
                # we put the character at the top of the new area
                self.x = 0
                self.y = self.y


            elif self.y < 0:
                # changing the character zone and so the background
                self.zone = 'backgrounds/sand_village.png'
                # we put the character at the top of the new area
                self.x = self.x
                self.y = 685


            elif self.x < 3:
                self.zone = 'backgrounds/foret_desert.png'
                self.x = 1210
                self.y = self.y

         # displaying the right background
        elif self.zone == 'backgrounds/sand_village.png':

            if self.x > 1260:
                # changing the character zone
                self.zone = 'backgrounds/desert_1.png'
                # we put the character at the top of the new area
                self.x = 5
                self.y = self.y


            elif self.y > 682:
                # changing the character zone and so the background
                self.zone = 'backgrounds/desert_2.png'
                # we put the character at the top of the new area
                self.x = self.x
                self.y = 0

            # the first house
            elif self.x > 180 and self.x < 244 and self.y > 509 and self.y < 550 and keys[pygame.K_w] :
                self.zone = "backgrounds/sand_maison_1.png"
                self.x = 620
                self.y = 620

            # the second house
            elif self.x > 988 and self.x < 1036 and self.y > 133 and self.y < 165 and keys[pygame.K_w] :
                self.zone = "backgrounds/sand_maison_2.png"
                self.x = 604
                self.y = 620


        # the first house in the desert
        elif self.zone == "backgrounds/sand_maison_1.png":
            if self.x > 524 and self.x < 708 and self.y > 625 and self.y < 720 and keys[pygame.K_w] :
                self.zone = "backgrounds/sand_village.png"
                self.x = 220
                self.y = 621

        # the second house in the desert
        elif self.zone == "backgrounds/sand_maison_2.png":
            if self.x > 516 and self.x < 708 and self.y > 625 and self.y < 720 and keys[pygame.K_w] :
                self.zone = "backgrounds/sand_village.png"
                self.x = 1012
                self.y = 166




        elif self.zone == 'backgrounds/sand_oasis.png':

            if self.x < 0:
                # changing the character zone and so the background
                self.zone = 'backgrounds/desert_2.png'
                # we put the character at the top of the new area
                self.x = 1265
                self.y = self.y


            elif self.y < 0:
                # changing the character zone and so the background
                self.zone = 'backgrounds/desert_1.png'
                # we put the character at the top of the new area
                self.x = self.x
                self.y = 685


        #DESERT


        #FORET

        elif self.zone == 'backgrounds/foret_desert.png':

            if self.x > 1260:
                # changing the character zone
                self.zone = 'backgrounds/desert_2.png'
                # we put the character at the top of the new area
                self.x = 20
                self.y = self.y


            elif self.x > 757 and self.x < 975 and self.y < 1:
                self.zone = 'backgrounds/foret_road.png'
                self.x = self.x
                self.y = 600

        elif self.zone == 'backgrounds/foret_road.png':

            # to the entry of the erae foret / desert
            if self.x > 757 and self.x < 975 and self.y > 630:
                # changing the character zone
                self.zone = 'backgrounds/foret_desert.png'
                # we put the character at the top of the new area
                self.x = self.x
                self.y = 3

            # to the area fleuve _ 1
            elif self.x >720 and self.x < 781 and self.y < 1 :
                # changing the character zone
                self.zone = 'backgrounds/fleuve_1.png'
                # we put the character at the bottom of the new area to be more real
                self.x = self.x
                self.y = 640


            elif self.x < 1 :
                self.zone = 'backgrounds/foret_fontaine.png'
                self.x = 1210
                self.y = self.y


        elif self.zone == 'backgrounds/foret_fontaine.png':

            if self.x > 1220 :
                # changing the character zone
                self.zone = 'backgrounds/foret_road.png'
                # we put the character at the top of the new area
                self.x = 5
                self.y = self.y

            if self.x > 800 and self.x < 1210 and self.y > 640:
                self.zone = 'backgrounds/foret_village.png'
                # we put the character at the top of the new area
                self.x = self.x
                self.y = 6

        elif self.zone == 'backgrounds/foret_village.png':

            if self.x > 800 and self.x < 1210 and self.y < 1:
                self.zone = 'backgrounds/foret_fontaine.png'
                # we put the character at the top of the new area
                self.x = self.x
                self.y = 600

            if self.y > 264 and self.y < 280 and self.x < 632 and self.x > 560 and keys[pygame.K_w] : #enter old man's house
                self.zone = "backgrounds/maison_vieux.png"
                self.y = 630
                self.x = self.x

        elif self.zone == "backgrounds/maison_vieux.png" :

            if self.y > 650 and keys[pygame.K_w] :
                self.zone = "backgrounds/foret_village.png"
                self.y = 280
                self.x = 600


        #FORET



        #FLEUVE

        elif self.zone == 'backgrounds/fleuve_1.png':

            if self.x >720 and self.x < 781 and self.y > 640 :
                self.zone = 'backgrounds/foret_road.png'
                self.x = self.x
                self.y = 3

            elif self.y < 2:
                self.zone = 'backgrounds/fleuve_2.png'
                self.x = self.x
                self.y = 640

            elif self.x > 1200:
                self.zone = 'backgrounds/montagne_1.png'
                self.x = 22
                self.y = self.y



        elif self.zone == 'backgrounds/fleuve_2.png':
            if self.x < 20 :
                self.zone = 'backgrounds/fleuve_3.png'
                self.x = 1190
                self.y = self.y

            elif self.y > 640:
                self.zone = 'backgrounds/fleuve_1.png'
                self.x = self.x
                self.y = 4



        elif self.zone == 'backgrounds/fleuve_3.png':

            if self.y > 640 :
                self.zone = 'backgrounds/fleuve_village.png'
                self.x = self.x
                self.y = 3

            elif self.x > 1210:
                self.zone = 'backgrounds/fleuve_2.png'
                self.x = 25
                self.y =self.y



        elif self.zone == 'backgrounds/fleuve_village.png':
            if self.y < 2 :
                self.zone = 'backgrounds/fleuve_3.png'
                self.x = self.x
                self.y = 635

            elif self.x > 1000 and self.x < 1096 and self.y > 516 and self.y < 600 and keys[pygame.K_w] :
                self.zone = "backgrounds/fleuve_maison_1.png"
                self.x = 644
                self.y = 620

            elif self.x > 120 and self.x < 208 and self.y > 516 and self.y < 590 and keys[pygame.K_w] :
                self.zone="backgrounds/fleuve_maison_2.png"
                self.x = 644
                self.y = 620



        elif self.zone =="backgrounds/fleuve_maison_1.png":
            if self.x > 564 and self.x < 708 and self.y > 625 and self.y < 720 and keys[pygame.K_w] :
                self.zone = "backgrounds/fleuve_village.png"
                self.x = 1050
                self.y =601



        elif self.zone == "backgrounds/fleuve_maison_2.png":
            if self.x > 572 and self.x < 820 and self.y > 625 and keys[pygame.K_w] :
                self.zone= "backgrounds/fleuve_village.png"
                self.x = 170
                self.y = 591


        #FLEUVE



        #MONTAGNE

        elif self.zone == "backgrounds/montagne_2.png":
            if self.y > 645:
                self.zone = "backgrounds/montagne_1.png"
                self.x = 948
                self.y = 9

            elif self.x > 1225:
                self.zone = "backgrounds/montagne_volcan.png"
                self.x = 11
                self.y = self.y

        elif self.zone == "backgrounds/montagne_volcan.png":
            if self.x < 10:
                self.zone = "backgrounds/montagne_2.png"
                self.x = 1220
                self.y = self.y

            elif self.y > 645:
                self.zone = "backgrounds/montagne_village.png"
                self.x = self.x
                self.y = 4

        elif self.zone == "backgrounds/montagne_village.png":
            if self.y < 2:
                self.zone = "backgrounds/montagne_volcan.png"
                self.x = self.x
                self.y = 640

        elif self.zone == "backgrounds/montagne_1.png" :

            if self.y < 8 :
                self.zone = "backgrounds/montagne_2.png"
                self.y = 650
                self.x = 204

            elif self.x < 20:
                self.zone = "backgrounds/fleuve_1.png"
                self.x = 1198
                self.y = self.y


        #MONTAGNE


        self.back = pygame.image.load(self.zone)

        # we display the modifications
        window.blit(self.back,(0, 0))

    """###BACKGROUND"""






    """###FONCTIONS MOUVEMENT"""


    def move_LEFT(self):

        if self.life == 1:

            # parametre for the character display
            self.right = False
            self.left = True
            self.up = False
            self.down = False
            self.x-=self.vel
        else:
            self.you_are_dead()

    def move_RIGHT(self):

        if self.life == 1:
        # parametre for the character display
            self.right = True
            self.left = False
            self.up = False
            self.down = False
            self.x+=self.vel
        else:
            self.you_are_dead()


    def move_UP (self) :

        if self.life == 1:
            self.up = True
            self.down = False
            self.right = False
            self.left =False
            self.y -= self.vel
        else:
            self.you_are_dead()


    def move_DOWN(self):
        if self.life == 1:
            # parametre for the character display
            self.up = False
            self.down = True
            self.right = False
            self.left =False
            self.y += self.vel
        else:
            self.you_are_dead()


    def not_move(self):


        self.up = False
        self.down = False
        self.right = False
        self.left =False



    """###FONCTIONS MOUVEMENT"""



    """###FONCTIONS LIMITES"""


    #LIMITE ET MOUVEMENT VILLAGE FORÊT

    def foret_village (self):

        # actions on the  keyboard
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:   #POUR ALLER A GAUCHE

            if self.x > 216 and self.x < 245 and self.y > 473 and self.y < 570 :  #limite marchand + maisons
                self.x = self.x
                self.y = self.y
                if self.a_d == 0 :
                    self.message = "textes/marchand_f.txt"
                else :
                    self.message ="textes/marchand_arme.txt"

                self.dia = 1

            elif self.x < 176 and self.x > 160 and self.y < 480 and self.y > 344 : #maison left middle
                self.y = self.y
                self.x = self.x


            elif self.x < 280 and self.x > 264 and self.y > 112 and self.y < 208: #limite chevalier fleur
                self.y = self.y
                self.x = self.x
                self.message = "textes/flower_man.txt"
                self.dia=1

            elif self.x < 790 and self.x > 776 and self.y > 496 and self.y < 630 : #limite arbre bottom
                self.y = self.y
                self.x = self.x

            elif self.x < 8 : #bordure
                self.y = self.y
                self.x = self.x

            elif self.x < 736 and self.x > 728 and self.y < 258 and self.y > 26 : #maison vieux
                self.y = self.y
                self.x = self.x

            else :

                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            if self.x > 160 and self.x < 176 and self.y < 208 and self.y > 136 : #limite chevalier fleur
                self.y = self.y
                self.x = self.x
                self.message = "textes/flower_man.txt"
                self.dia=1

            elif self.x > 448 and self.x < 464 and self.y < 570 and self.y > 496 :  #limite arbre bottom
                self.y = self.y
                self.x = self.x

            elif self.x < 896 and self.x > 880 and self.y < 630 and self.y > 536 : #maison droite
                self.y = self.y
                self.x = self.x

            elif self.x < 1070 and self.x > 1056 and self.y < 544 and self.y > 408 :#perso femme
                self.y = self.y
                self.x = self.x
                self.message = "textes/femme.txt"
                self.dia = 1

            elif self.x > 1120 and self.x < 1136 and self.y > 176 and self.y < 424 : #perso link
                self.y = self.y
                self.x = self.x
                self.message ="textes/link.txt"
                self.dia = 1

            elif self.x > 1262 : #bordure
                self.y = self.y
                self.x = self.x

            elif self.x > 448 and self.x < 464 and self.y > 32 and self.y < 258 : #maison vieux
                self.y = self.y
                self.x = self.x
                self.message = "textes/cat.txt"
                self.dia = 1



            else :

                self.move_RIGHT()



        elif keys[pygame.K_UP]:

            if self.x > 400 and self.x < 464 and self.y > 32 and self.y < 258 : #being assured we can talk to the cat going up
                self.message = "textes/cat.txt"
                self.dia = 1

            if self.y < 217  and self.y > 207 and self.x < 272 and self.x > 168 : #limite chevalier
                self.y = self.y
                self.x = self.x
                self.message = "textes/flower_man.txt"
                self.dia=1

            elif self.y < 8 and self.x < 808 : #bordure
                self.y = self.y
                self.x = self.x

            elif self.y < 280 and self.y > 242 and self.x < 736 and self.x > 456 : #maison vieux
                self.y = self.y
                self.x = self.x



            else:
                self.move_UP()


        # if we want to to on the bottom
        elif keys[pygame.K_DOWN]:

            if self.x > 232 and self.x < 464 and self.y > 560:  #limite maison bottom left
                self.x = self.x
                self.y = self.y

            elif self.y > 104 and self.y < 120 and self.x > 168 and self.x < 272 : #limite chevalier fleur
                self.y = self.y
                self.x = self.x
                self.message = "textes/flower_man.txt"
                self.dia=1

            elif self.y > 496 and self. y < 512 and self.x > 464 and self.x < 792 : #limite arbres bottom
                self.y = self.y
                self.x = self.x

            elif self.y > 616 and self.y < 630 and self.x > 776 and self.x < 896 : #limite arbres bottom
                self.y = self.y
                self.x = self.x

            elif self.y < 544 and self.y > 528 and self.x > 880  and self.x < 1070 : #maison droite
                self.y = self.y
                self.x = self.x

            elif self.y < 424 and self.y > 408 and self.x > 1056 and self.x < 1136 : #femme droite
                self.y = self.y
                self.x = self.x
                self.message = "textes/femme.txt"
                self.dia = 1

            elif self.y < 192 and self.y > 174 and self.x > 1120 and self.x < 1718 : #link
                self.y = self.y
                self.x = self.x

            elif self.y < 480 and self.y > 466 and self.x < 248 and self.x > 160 : #marchand down
                self.y = self.y
                self.x = self.x

            elif self.y < 352 and self.y > 336 and self.x < 176 : #maison middle left
                self.y = self.y
                self.x = self.x

            elif self.y < 40 and self.y > 26 and self.x < 744 and self.x > 448 : #maison vieux
                self.y = self.y
                self.x = self.x


            else :

                self.move_DOWN()


        else :

            self.not_move()




    """old man's house in forest"""


    def maison_vieux(self):

        keys = pygame.key.get_pressed()

        #print(self.zone)

        if keys[pygame.K_LEFT]:

            if self.x <32 and self.x > 16 and self.y < 652 and self.y > 406 : #bordure left
                self.y = self.y
                self.x = self.x

            elif self.x < 184 and self.x > 168 and self.y > 134 and self.y < 422 : #bordure gauche lit
                self.y = self.y
                self.x = self.x

            elif self.x < 248 and self.x > 232 and self.y > 454 and self.y < 550 : #vieux
                if self.arme == 0:
                    self.message="textes/vieux_quete.txt"
                    self.a_d = 1 #variabl demande arme
                else :
                    self.message="textes/vieux_quete2.txt"
                self.dia = 1
                self.y = self.y
                self.x = self.x

            elif self.x < 1104 and self.x > 1088 and self.y > 238 and self.y < 486 : #table
                self.y = self.y
                self.x = self.x


            else :

                self.move_LEFT()

        elif keys[pygame.K_RIGHT]:

            if self.x < 1216 and self.x > 1200 and self.y > 136 and self.y < 664 : #bordure droite
                self.y = self.y
                self.x = self.x

            elif self.x < 80 and self.x > 64 and self.y > 454 and self.y < 550 : #vieux
                self.y = self.y
                self.x = self.x

            elif self.x < 856 and self.x > 840 and self.y > 238 and self.y < 486 : #table
                self.y = self.y
                self.x = self.x



            else :

                self.move_RIGHT()


        elif keys[pygame.K_UP]:

            if self.y > 406 and self.y < 422 and self.x < 184 and self.x > 16 : #bordure lit bas
                self.y = self.y
                self.x = self.x

            elif self.y < 150 and self.y > 134 and self.x > 16 and self.x < 1216 : #bordure haute
                self.y = self.y
                self.x = self.x

            elif self.y < 566 and self.y > 550 and self.x < 248 and self.x > 64 : #vieux
                if self.arme == 0 :
                    self.message = "textes/vieux_quete.txt"
                    self.a_d = 1 #variabl demande arme
                else :
                    self.message = "textes/vieux_quete2.txt"
                self.dia = 1
                self.y = self.y
                self.x = self.x

            elif self.y > 478 and self.y < 494 and self.x > 840 and self.x < 1104 : #table
                self.y = self.y
                self.x = self.x


            else :

                self.move_UP()


        elif keys[pygame.K_DOWN]:

            if self.y < 662 and self.y > 646 and self.x > 16 and self.x < 1216 : #bordure bas
                self.y = self.y
                self.x = self.x

            elif self.y < 470 and self.y > 454 and self.x > 64 and self.x < 248 : #vieux
                self.y = self.y
                self.x = self.x

            elif self.y < 254 and self.y > 238 and self.x > 848 and self.x < 1096: #table
                self.y = self.y
                self.x = self.x


            else :
                self.move_DOWN()



        else :

            self.not_move()



    """ the fontain in the woods"""

    def foret_fontaine(self):

        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            if self.x < 10:
                self.not_move()

            # the fontain
            elif self.x > 700 and self.x < 750 and self.y > 320 and self.y < 390:
                self.not_move()

            #the higher part of the fontain
            elif self.x > 660  and self.x < 704 and self.y > 252 and self.y < 348 :
                self.not_move()

            #the shop on the left
            elif self.x > 100 and self.x < 120 and self.y > 180 and self.y < 436 :
                self.not_move()

            # the shop on the top
            elif self.x > 390 and self.x < 408 and self.y > -12 and self.y < 116 :
                self.not_move()

            # the vegetables
            elif self.x > 800 and self.x < 824 and self.y > 380 and self.y < 452 :
                self.not_move()

            elif self.x > 830 and self.x < 850 and self.y < 632 and self.y > 520 : #shop at first on left
                self.not_move()

            elif self.x < 184 and self.x > 168 and self.y < 376 and self.y > 288 : #shop guy
                self.not_move()
                self.message = "textes/vendeur.txt"
                self.dia = 1



            else :

                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:
            # the fontain
            if self.x > 490 and self.x < 700 and self.y > 320 and self.y < 390 :
                self.not_move()

            # the fontain second part
            elif self.x > 540 and self.x < 600 and self.y > 252 and self.y < 348 :
                self.not_move()

            # the shop on the top
            elif self.x > 216 and self.x < 290 and self.y > -12 and self.y < 116 :
                self.not_move()

            # the vegetables
            elif self.x > 448 and self.x < 500 and self.y > 380 and self.y < 452 :
                self.not_move()

            # the limit of the trees at the other side in the wood road on the top
            elif self.x > 1210 and self.y < 132:
                self.not_move()

            # the limit of the trees at the other side in the wood road on the bottom
            elif self.x > 1210 and self.y > 356:
                self.not_move()

            else:
                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:

            if self.y < 2:
                self.not_move()

            # the fontain
            elif self.x > 490 and self.x < 750 and self.y > 370 and self.y < 390 :
                self.not_move()

            # the fontain second part
            elif self.x >540 and self.x < 704 and self.y > 300 and self.y < 348 :
                self.not_move()

            # the shop on the left
            elif self.x > 0 and self.x < 120 and self.y > 400 and self.y < 436 :
                self.not_move()

            # the shop on the top
            elif self.x > 216 and self.x < 408 and self.y > 100 and self.y < 116 :
                self.not_move()

            # the vegetables
            elif self.x > 448 and self.x < 824 and self.y > 440 and self.y < 456 :
                self.not_move()
                self.message = "textes/vendeuse.txt"
                self.dia = 1

            elif self.y >368 and self.y < 384 and self.x < 176 and self.x > 112 : #shop guy
                self.not_move()
                self.message = "textes/vendeur.txt"
                self.dia = 1

            #the limit of the wall
            elif self.y < 136:
                self.not_move()
                self.message = "textes/chevalier_porte.txt"
                self.dia = 1



            else :

                self.move_UP()


        # if we want to go down
        elif keys[pygame.K_DOWN]:
            if self.x < 850 and self.y > 510 and self.y < 720 :
                self.not_move()

            # the fontain
            elif self.x > 490 and self.x < 750 and self.y > 320 and self.y < 340 :
                self.not_move()

            elif self.x > 540 and self.x < 704 and self.y > 250 and self.y < 300:
                self.not_move()

            # the shop on the left
            elif self.x > 0 and self.x < 120 and self.y > 180 and self.y < 200 :
                self.not_move()

            # the vegetables
            elif self.x > 448 and self.x < 824 and self.y > 380 and self.y < 400 :
                self.not_move()

            elif self.y < 294 and self.y > 280 and self.x < 176 and self.x > 112 : #shop guy
                self.not_move()



            else :
                self.move_DOWN()


        else :
           self.not_move()


    """ the fontain in the woods"""



    """ the road in the woods"""

    # limites of foret road

    def foret_road(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            # trees on the top
            if self.x >700 and self.x < 730 and self.y < 116:
                self.not_move()

            # trees on the bottom
            elif self.x >700 and self.x < 773 and self.y > 354:
                self.not_move()

            else :
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the trees on the bottom
            if self.x > 957 and self.y > 380:
                self.not_move()

            # the trees on the top
            elif self.x >  781 and self.y < 124:
                self.not_move()

            # the trees on the extrem right side
            elif self.x > 1117 :
                self.not_move()

            else :
                self.move_RIGHT()




        # if we want to to on the left
        elif keys[pygame.K_UP]:
            # the trees on the top left
            if self.x > 0 and self.x < 677 and self.y < 140 :
                self.not_move()

            # the trees on the top right
            elif self.x > 789 and self.x < 1270 and self.y < 140 :
                self.not_move()

            else :
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:
            #trees on the bottom left
            if self.x > 0 and self.x < 700 and self.y >354 :
                self.not_move()

            #trees on the bottom right
            elif self.x > 975 and self.x < 1270 and self.y > 354 :
                self.not_move()

            else :
                self.move_DOWN()


        else :
            self.not_move()


    """ the road in the woods"""



    """ the limit between desert and woods"""
    # limites of foret / desert

    def foret_desert(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            #the trees on the left
            if self.x > 0 and self.x < 110 and self.y > 0 and self.y <720:
                self.not_move()

            # trees on the top left
            elif self.x > 300 and self.x < 390 and self.y < 83:
                self.not_move()

            # trees on the bottom
            elif self.x > 400 and self.x < 490 and self.y > 483:
                self.not_move()

            else:
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:
            self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:
            # the trees on the top
            if self.x > 0 and self.x < 390 and self.y > 0 and self.y < 100:
                self.not_move()

            elif self.x > 953  and self.y < 4:
                self.not_move()

            # the passage limitation
            elif self.x > 390 and self.x < 730 and self.y < 2 :
                self.not_move()

            else:
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:
            # the trees on the bottom
            if self.x > 0 and self.x < 490 and self.y > 483 and self.y < 720 :
                self.not_move()

            #the bottom limitation
            elif self.x > 0 and self.x < 1270 and self.y > 600 :
                self.not_move()

            else :
                self.move_DOWN()


        else :
            self.not_move()

    """ the limit between desert and woods"""


    #ZONE FLEUVE

    """ the river village """

    def fleuve_village(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:
            # the limit
            if self.x < 20:
                self.not_move()

            elif self.x > 300 and self.x < 320 and self.y > 395 and self.y < 563 :
                self.not_move()

            elif self.x > 678 and self.x < 734 and self.y > 403 and self.y < 475 :
                self.not_move()

            elif self.x > 678 and self.x < 734 and self.y > 635 and self.y < 720 :
                self.not_move()

            elif self.x > 1210 and self.x < 1214 and self.y > 1190 and self.y < 571 :
                self.not_move()

            elif self.x > 1210 and self.x < 1214 and self.y > 1190 and self.y < 571 :
                self.not_move()

            elif self.x > 900 and self.x < 918 and self.y > 99 and self.y < 355 :
                self.not_move()

            # the first bridge
            elif self.x > 702 and self.x < 774 and self.y > 99 and self.y < 379 :
                self.not_move()

            elif self.x < 568 and self.x > 552 and self.y > 32 and self.y < 136 : #villager up
                self.not_move()
                self.message = "textes/fleuve_v.txt"
                self.dia = 1

            else :
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the limit
            if self.x > 1210:
                self.not_move()

            elif self.x > 10 and self.x < 20 and self.y > 451 and self.y < 563 :
                self.not_move()

            elif self.x > 470 and self.x < 480 and self.y > 403 and self.y < 467 :
                self.not_move()

            elif self.x > 470 and self.x < 480 and self.y > 643 and self.y < 720 :
                self.not_move()

            elif self.x > 894 and self.x < 900 and self.y > 419 and self.y < 563 :
                self.not_move()

            elif self.x > 710 and self.x < 720 and self.y > 147 and self.y < 347 :
                self.not_move()

            elif self.x >1054 and self.x < 1060 and self.y > 57 and self.y <70 :
                self.not_move()

            # the first bridge
            elif self.x > 838 and self.x < 894 and self.y > 83 and self.y < 363 :
                self.not_move()

            # the second bridge
            elif self.x > 454 and self.x < 500 and self.y > 530 and self.y < 477 :
                self.not_move()

            # first house
            elif self.x > 886 and self.x < 942 and self.y > 335 and self.y < 579 :
                self.not_move()

            elif self.x < 488 and self.x > 472 and self.y > 32 and self.y < 136 : #villager up
                self.not_move()

            elif self.x < 392 and self.x > 376 and self.y < 432 and self.y > 360 : #villager down
                self.not_move()

            else :
                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:
            if self.y < 2:
                self.not_move()

            elif self.x > 886 and self.x < 1214 and self.y > 283 and self.y < 331 :
                self.not_move()

            elif self.x > 918 and self.x < 1014 and self.y > 500 and self.y < 579 :
                self.not_move()

            elif self.x > 1126 and self.x < 1190 and self.y > 500 and self.y < 579 :
                self.not_move()

            elif self.x > 700 and self.x < 718 and self.y > 300 and self.y < 371 :
                self.not_move()

            elif self.x > 0 and self.x < 478 and self.y > 300 and self.y < 363 :
                self.not_move()

            elif self.x > 22 and self.x < 134 and self.y > 500 and self.y < 587 :
                self.not_move()

            elif self.x > 222 and self.x < 302 and self.y > 500 and self.y < 587 :
                self.not_move()

            elif self.x > 470 and self.x < 702 and self.y > 451 and self.y < 483 :
                self.not_move()

            elif self.y < 592 and self.y > 576 and self.x > 120 and self.x < 208 : #door house
                self.not_move()

            elif self.y < 590 and self.y > 568 and self.x < 1088 and self.x > 1000 : #door house
                self.not_move()

            elif self.y < 440 and self.y > 424 and self.x < 472 and self.x > 384 : #villager down
                self.not_move()


            else :
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:

            if self.y > 640:
                self.not_move()

            elif self.x > 0 and self.x < 750 and self.y > 131 and self.y < 339 :
                self.not_move()

            elif self.x >934 and self.x < 1070 and self.y > 43 and self.y < 236 :
                self.not_move()

            elif self.x > 470 and self.x < 702 and self.y > 595 and self.y < 600 :
                self.not_move()

            # the second house
            elif self.x > 30 and self.x < 294 and self.y > 379 and self.y < 411 :
                self.not_move()

            # the first house
            elif self.x > 926 and self.x < 1174 and self.y > 355 and self.y < 395 :
                self.not_move()

            elif self.y > 24 and self.y < 40 and self.x < 560 and self.x > 480 : #villager up
                self.not_move()

            else :
                self.move_DOWN()


        else :
            self.not_move()

    """ the river village """

    """ the second house of the river area """

    def fleuve_maison_2(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            if self.x < 44:
                self.not_move()

            # the first bed
            elif self.x > 0 and self.x < 180 and self.y > 108 and self.y < 292 :
                self.not_move()

            # the second bed
            elif self.x > 0 and self.x < 180 and self.y > 348 and self.y < 524 :
                self.not_move()

            # the kitchen
            elif self.x > 1004 and self.x < 1060 and self.y > 0 and self.y < 164 :
                self.not_move()

            # the table and bench
            elif self.x > 788 and self.x < 1004 and self.y > 316 and self.y < 444 :
                self.not_move()

            elif self.x > 284 and self.x < 300 and self.y < 220 and self.y > 132 : #marchand
                self.not_move()
                self.message = "textes/fleuve_marchand.txt"
                self.dia = 1

            else:
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            if self.x > 1212:
                self.not_move()

            # the kitchen
            elif self.x > 508 and self.x < 572 and self.y > 0 and self.y < 164 :
                self.not_move()

            # thetable and bench
            elif self.x > 780 and self.x < 1004 and self.y > 316 and self.y < 444 :
                self.not_move()

            elif self.x > 188 and self.x < 204 and self.y < 220 and self.y > 132 : #marchand
                self.not_move()
                self.message = "textes/fleuve_marchand.txt"
                self.dia = 1

            else :
                self.move_RIGHT()


        # if we want to to on the left
        elif keys[pygame.K_UP]:
            if self.y < 124 :
                self.not_move()

            # the first bed
            elif self.x > 0 and self.x < 156 and self.y > 228 and self.y < 292 :
                self.not_move()

            # the second bed
            elif self.x > 0 and self.x < 164 and self.y > 476 and self.y < 524 :
                self.not_move()

            # the kitchen
            elif self.x > 524 and self.x < 1060 and self.y > 0 and self.y < 172 :
                self.not_move()

            # the table and bench
            elif self.x > 788 and self.x < 1004 and self.y > 388 and self.y < 436 :
                self.not_move()

            elif self.y < 228 and self.y > 212 and self.x < 292 and self.x > 196 : #marchand
                self.not_move()
                self.message = "textes/fleuve_marchand.txt"
                self.dia = 1


            else:
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:
            ## the limits on the left
            if self.x > 0 and self.x < 628 and self.y > 628 :
                self.not_move()

            # the limits on the right
            elif self.x > 820 and self.x < 720 and self.y > 628 :
                self.not_move()

            # the second bed
            elif self.x > 0 and self.x < 164 and self.y > 355 and self.y < 404 :
                self.not_move()

            # the table and bench
            elif self.x > 788 and self.x < 1004 and self.y > 316 and self.y < 348 :
                self.not_move()

            elif self.y > 124 and self.y < 140 and self.x > 196 and self.x < 292 : #goddess
                self.not_move()

            else:
                self.move_DOWN()


        else :
            self.not_move()

    """ the second house of the river area """


    """ the first house of the river area"""

    def fleuve_maison_1(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            if self.x < 44:
                self.not_move()

            # the bed
            elif self.x > 172 and self.x < 228 and self.y > 0 and self.y < 228 :
                self.not_move()

            # the closet
            elif self.x > 460 and self.x < 540 and self.y > 0 and self.y < 164 :
                self.not_move()

            # the table and chairs
            elif self.x >1100 and self.x < 1132 and self.y > 284 and self.y < 428 :
                self.not_move()

            elif self.x < 684 and self.x > 668 and self.y > 204 and self.y < 292 : #goddess
                self.not_move()
                self.message = "textes/fleuve_goddess.txt"
                self.dia = 1

            else:
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            if self.x > 1220:
                self.not_move()

            # the bed
            elif self.x > 52 and self.x < 116 and self.y > 0 and self.y < 228 :
                self.not_move()

            # the closet
            elif self.x > 260 and self.x < 280 and self.y > 0 and self.y < 164 :
                self.not_move()

            # the kitchen
            elif self.x > 644 and self.x < 670 and self.y > 0 and self.y < 156 :
                self.not_move()

            # the table and chair
            elif self.x > 924 and self.x < 930 and self.y > 284 and self.y < 428 :
                self.not_move()

            # the limit area
            elif self.x > 1188 :
                self.not_move()

            elif self.x < 604 and self.x > 586 and self.y < 292 and self.y > 204 : #goddess
                self.not_move()
                self.message = "textes/fleuve_goddess.txt"
                self.dia = 1

            else :
                self.move_RIGHT()


        # if we want to to on the left
        elif keys[pygame.K_UP]:

            if self.y < 2 :
                self.not_move()

            # the bed
            elif self.x > 52 and self.x < 228 and self.y > 164 and self.y < 228 :
                self.not_move()

            # the closet
            elif self.x > 260 and self.x < 540 and self.y > 0  and self.y < 164 :
                self.not_move()

            # the kitchen
            elif self.x > 644 and self.x < 1270 and self.y > 0 and self.y < 156 :
                self.not_move()

            # the table and chairs
            elif self.x > 924 and self.x < 1132 and self.y > 380 and self.y < 428 :
                self.not_move()

            # the area limitation
            elif self.x > 0 and self.x < 1270 and self.y < 132 :
                self.not_move()

            elif self.y < 300 and self.y > 284 and self.x < 676 and self.x > 596 : #goddess
                self.not_move()
                self.message = "textes/fleuve_goddess.txt"
                self.dia = 1

            else:
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:

            # the table and chairs
            if self.x > 924 and self.x < 1132 and self.y > 284 and self.y < 290 :
                self.not_move()

            # the limits on the left
            elif self.x > 0 and self.x < 556 and self.y > 628 and self.y < 720 :
                self.not_move()

            # the limits on the right
            elif self.x > 724 and self.x < 1270 and self.y > 628 and self.y < 720 :
                self.not_move()

            elif self.y > 212 and self.y < 196 and self.x < 676 and self.x > 596 : #goddess
                self.not_move()

            else:
                self.move_DOWN()


        else :
            self.not_move()

    """ the first house of the river area """


    """ the river third part """

    def fleuve_3(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            # the bridge
            if self.x > 118 and self.x < 182 and self.y > 315 and self.y < 555 :
                self.not_move()

            # the limitation area
            elif self.x < 10 :
                self.not_move()

            else:
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the bridge
            if self.x > 262 and self.x < 334 and self.y > 315 and self.y < 555 :
                self.not_move()

            # the area limitation
            elif self.x > 1210 and self.y > 515 and self.y < 720 :
                self.not_move()

            else :
                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:
            if self.y < 2:
                self.not_move()

            # the river left side
            elif self.x > -6 and self.x < 134 and self.y > 390 and self.y < 555 :
                self.not_move()

            # the river right side
            elif self.x > 310 and self.x < 1270 and self.y > 390 and self.y < 555 :
                self.not_move()

            else :
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:

            # the river left side
            if self.x > -6 and self.x < 134 and self.y > 315 and self.y < 363 :
                self.not_move()

            # the right side of the river
            elif self.x > 310 and self.x < 1270 and self.y > 315 and self.y < 366 :
                self.not_move()

            else :
                self.move_DOWN()


        else :
            self.not_move()

    """ the river third part """

    """ the river second part """

    def fleuve_2(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            if self.x < 10:
                self.not_move()

            elif self.x > 500 and self.x < 512 and self.y > 252 and self.y < 548 :
                self.not_move()

            elif self.x > 500 and self.x < 512 and self.y > 0 and self.y < 92 :
                self.not_move()

            elif self.x < 25 and self.y > 320 and self.y < 720 :
                self.not_move()


            else :
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            if self.x > 264 and self.x < 320 and self.y > 0 and self.y < 76 :
                self.not_move()

            elif self.x > 264 and self.x < 320 and self.y > 256 and self.y < 372 :
                self.not_move()

            elif self.x > 1200:
                self.not_move()

            else:
                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:
            if self.y < 2:
                self.not_move()

            elif self.x > 0 and self.x < 296 and self.y > 370 and self.y < 596 :
                self.not_move()

            elif self.x > 264 and self.x < 504 and self.y > 316 and self.y < 573 :
                self.not_move()

            elif self.x > 264 and self.x < 504 and self.y > 0 and self.y < 92 :
                self.not_move()

            else :
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:

            if self.x > 272 and self.x < 520 and self.y > 252 and self.y < 500 :
                self.not_move()

            elif self.x > 0 and self.x < 280 and self.y > 360 and self.y < 370 :
                self.not_move()

            else:

                self.move_DOWN()


        else :
            self.not_move()

    """ the river second part """

    """ the river juste above the foret road"""

    def fleuve_1(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:
            # the limit
            if self.x < 20 :
                self.x = self.x
                self.y = self.y

            # the bridge
            elif self.x > 504 and self.x < 524 and self.y > 52 and self.y < 532 :
                self.not_move()

            else :

                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            #the limit
            if self.x > 1210  :
                self.not_move()

            # the bridge
            elif self.x > 600 and self.x < 640 and self.y > 52 and self.y < 532 :
                self.not_move()

            else:
                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:

            # the left part of the river
            if self.x > 0 and self.x < 488 and self.y >500 and self.y < 532 :
                self.not_move()

            #the right part of the river
            elif self.x >640 and self.x < 1270 and self.y > 500 and self.y < 532 :
                self.not_move()

            else :

                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:
            # the bottom limit
            if self.x < 720 and self.y > 640:
                self.not_move()

            elif self.x > 781 and self.y > 640:
                self.not_move()

             # the left part of the river
            elif self.x > 0 and self.x < 488 and self.y >28 and self.y < 50 :
                self.not_move()

            #the right part of the river
            elif self.x >640 and self.x < 1270 and self.y > 28 and self.y < 50 :
                self.not_move()

            else:
                self.move_DOWN()


        else :
            self.not_move()


    """ the river justt after the foret road """





    #ZONE SABLE

    """LIMITE ZONE SABLE OASIS"""

    def sand_oasis(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            #we can't get out of the map
            if self.x < 2:
                self.x = self.x

            else :
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            #we can't get out of the map
            if self.x > 710:
                self.x = self.x

            else :

                self.move_RIGHT()

        # if we want to to on the left
        if keys[pygame.K_UP]:

            self.move_UP()


        # if we want to to on the left
        if keys[pygame.K_DOWN]:

            #we can't get out of the map
            if self.y > 1255:
                self.y = self.y

            else:

                self.move_DOWN()

        else :

            self.not_move()



    #LIMITE ZONE SABLE 2

    def desert_2(self):

         # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            # the cactus on the top left
            if self.x > 138 and self.x < 198 and self.y > 128 and self.y < 208 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom left
            elif self.x >146  and self.x < 222  and self.y > 512  and self.y < 608 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top center
            elif self.x > 360 and self.x < 446  and self.y > 0  and self.y < 40 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom center
            elif self.x > 590 and self.x < 616 and self.y > 432 and self.y < 512  :
                self.x = self.x
                self.y = self.y

            # the cactus on the top right
            elif self.x > 1080 and self.x < 1110 and self.y > 8 and self.y < 64 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom right
            elif self.x > 1100 and self.x < 1126 and self.y > 496 and self.y < 584 :
                self.x = self.x
                self.y = self.y

            #we can't get out of the map
            elif self.x < 2:
                self.x=self.x

            else :

                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

             # the cactus on the top left
            if self.x > 118 and self.x < 142 and self.y > 128 and self.y < 208 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom left
            elif self.x >126  and self.x < 148  and self.y > 512  and self.y < 608 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top center
            elif self.x > 350 and self.x < 420  and self.y > 0  and self.y < 40 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom center
            elif self.x > 534 and self.x < 585 and self.y > 432 and self.y < 512  :
                self.x = self.x
                self.y = self.y

            # the cactus on the top right
            elif self.x > 1022 and self.x < 1075 and self.y > 8 and self.y < 64 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom right
            elif self.x > 1032 and self.x < 1090 and self.y > 496 and self.y < 584 :
                self.x = self.x
                self.y = self.y




            else :

                self.move_RIGHT()



        # if we want to go at the top
        elif keys[pygame.K_UP]  :

            # the cactus on the top left
            if self.x > 118 and self.x < 192 and self.y > 158 and self.y < 218 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom left
            elif self.x >126  and self.x < 198  and self.y > 520  and self.y < 608 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top center
            elif self.x > 350 and self.x < 430  and self.y > 20  and self.y < 40 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom center
            elif self.x > 534 and self.x < 616 and self.y > 490 and self.y < 512  :
                self.x = self.x
                self.y = self.y

            # the cactus on the top right
            elif self.x > 1022 and self.x < 1094 and self.y > 36 and self.y < 64 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom right
            elif self.x > 1032 and self.x < 1112 and self.y > 530 and self.y < 584 :
                self.x = self.x
                self.y = self.y



            else :

                self.move_UP()



        # if we want to go at the bottom
        elif keys[pygame.K_DOWN]:

             # the cactus on the top left
            if self.x > 118 and self.x < 182 and self.y > 128 and self.y < 150 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom left
            elif self.x >126  and self.x < 198  and self.y > 512  and self.y < 600 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top center
            elif self.x > 350 and self.x < 430  and self.y > 0  and self.y < 20 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom center
            elif self.x > 534 and self.x < 616 and self.y > 432 and self.y < 500  :
                self.x = self.x
                self.y = self.y

            # the cactus on the top right
            elif self.x > 1022 and self.x < 1094 and self.y > 8 and self.y < 44 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom right
            elif self.x > 1032 and self.x < 1112 and self.y > 496 and self.y < 544 :
                self.x = self.x
                self.y = self.y

            #we can't get out of the map
            elif self.y > 1260:
                self.y = self.y



            else :
                self.move_DOWN()

        else :

            self.not_move()




    #LIMITES ZONE SABLE 1

    def desert_1(self):

         # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            # the cactus on the top left
            if self.x > 138 and self.x < 198 and self.y > 128 and self.y < 208 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom left
            elif self.x >146  and self.x < 222  and self.y > 512  and self.y < 608 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top center
            elif self.x > 360 and self.x < 446  and self.y > 0  and self.y < 40 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom center
            elif self.x > 590 and self.x < 616 and self.y > 432 and self.y < 512  :
                self.x = self.x
                self.y = self.y

            # the cactus on the top right
            elif self.x > 1080 and self.x < 1110 and self.y > 8 and self.y < 64 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom right
            elif self.x > 1100 and self.x < 1126 and self.y > 496 and self.y < 584 :
                self.x = self.x
                self.y = self.y



            else :
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

             # the cactus on the top left
            if self.x > 118 and self.x < 142 and self.y > 128 and self.y < 208 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom left
            elif self.x >126  and self.x < 148  and self.y > 512  and self.y < 608 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top center
            elif self.x > 350 and self.x < 420  and self.y > 0  and self.y < 40 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom center
            elif self.x > 534 and self.x < 585 and self.y > 432 and self.y < 512  :
                self.x = self.x
                self.y = self.y

            # the cactus on the top right
            elif self.x > 1022 and self.x < 1075 and self.y > 8 and self.y < 64 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom right
            elif self.x > 1032 and self.x < 1090 and self.y > 496 and self.y < 584 :
                self.x = self.x
                self.y = self.y

            elif self.x > 1220:
                self.not_move()

            else :

                self.move_RIGHT()


        # if we want to go at the top
        elif keys[pygame.K_UP]  :

            # the cactus on the top left
            if self.x > 118 and self.x < 192 and self.y > 158 and self.y < 218 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom left
            elif self.x >126  and self.x < 198  and self.y > 520  and self.y < 608 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top center
            elif self.x > 350 and self.x < 430  and self.y > 20  and self.y < 40 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom center
            elif self.x > 534 and self.x < 616 and self.y > 490 and self.y < 512  :
                self.x = self.x
                self.y = self.y

            # the cactus on the top right
            elif self.x > 1022 and self.x < 1094 and self.y > 36 and self.y < 64 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom right
            elif self.x > 1032 and self.x < 1112 and self.y > 530 and self.y < 584 :
                self.x = self.x
                self.y = self.y

            elif self.y < 5:
                self.not_move()

            else :
                self.move_UP()


        # if we want to go at the bottom
        elif keys[pygame.K_DOWN]:

             # the cactus on the top left
            if self.x > 118 and self.x < 182 and self.y > 128 and self.y < 150 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom left
            elif self.x >126  and self.x < 198  and self.y > 512  and self.y < 600 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top center
            elif self.x > 350 and self.x < 430  and self.y > 0  and self.y < 20 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom center
            elif self.x > 534 and self.x < 616 and self.y > 432 and self.y < 500  :
                self.x = self.x
                self.y = self.y

            # the cactus on the top right
            elif self.x > 1022 and self.x < 1094 and self.y > 8 and self.y < 44 :
                self.x = self.x
                self.y = self.y

            # the cactus on the bottom right
            elif self.x > 1032 and self.x < 1112 and self.y > 496 and self.y < 544 :
                self.x = self.x
                self.y = self.y

            else :

                self.move_DOWN()

        else :

            self.not_move()


    #LIMITES ZONE SABLE VILLAGE

    def sand_village(self):

        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            #the first house
            if self.x > 100 and self.x < 280 and self.y > 308 and self.y < 532 :
                self.x = self.x
                self.y = self.y

            # the second house
            elif self.x > 1000  and self.x < 1070 and self.y > -60 and self.y < 164 :
                self.x = self.x
                self.y = self.y

            # the fontain's higher part
            elif self.x > 700 and self.x < 750 and self.y > 228 and self.y < 316 :
                self.x = self.x
                self.y = self.y

            # the fontain's lower part
            elif self.x > 730  and self.x < 800 and self.y >292 and self.y < 356 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top left
            elif self.x > 100  and self.x < 170 and self.y > -4 and self.y < 84 :
                self.x = self.x
                self.y = self.y

            #the cactus on the bottom left
            elif self.x > 300  and self.x < 330 and self.y > 428 and self.y < 524 :
                self.x = self.x
                self.y = self.y

            #the cactus on the top right
            elif self.x > 1140  and self.x < 1195 and self.y > 36 and self.y < 124 :
                self.x = self.x
                self.y = self.y

            #the cactus on the bottom right
            elif self.x > 1030  and self.x < 1056 and self.y > 476 and self.y < 564 :
                self.x = self.x
                self.y = self.y



            else :

                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the first house
            if self.x > 64 and self.x < 100  and self.y > 308 and self.y < 532:
                self.x = self.x
                self.y = self.y

            #the second house
            elif self.x >856  and self.x < 1000 and self.y > -60 and self.y < 164 :
                self.x = self.x
                self.y = self.y

            #the lower part of the fontain
            elif self.x >536  and self.x < 600 and self.y > 292 and self.y < 356 :
                self.x = self.x
                self.y = self.y

            # the higher part of the fontain
            elif self.x > 567  and self.x < 600 and self.y > 228 and self.y < 316 :
                self.x = self.x
                self.y = self.y

            # the cactus o the top left
            elif self.x > 96 and self.x < 110 and self.y > -4 and self.y < 84 :
                self.x = self.x
                self.y = self.y

            #the cactus on the top right
            elif self.x > 1120  and self.x < 1140 and self.y > 36 and self.y < 124 :
                self.x = self.x
                self.y = self.y

            #the cactus on the bottom right
            elif self.x > 976  and self.x < 900 and self.y > 476 and self.y < 564 :
                self.x = self.x
                self.y = self.y

            else :

                self.move_RIGHT()


        # if we want to go at the top
        elif keys[pygame.K_UP]  :

            #the first house
            if self.x > 72  and self.x < 280 and self.y > 400 and self.y < 532 :
                self.x = self.x
                self.y = self.y

            # the second house
            elif self.x >856  and self.x < 1070 and self.y > 100 and self.y < 164 :
                self.x = self.x
                self.y = self.y

            # the fontain's higher part
            elif self.x > 567 and self.x < 728 and self.y > 300 and self.y < 316 :
                self.x = self.x
                self.y = self.y

            # the fontain's lower part
            elif self.x > 536  and self.x < 778 and self.y > 330 and self.y < 356 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top left
            elif self.x >96  and self.x < 170 and self.y > 50 and self.y < 84 :
                self.x = self.x
                self.y = self.y

            #the cactus on the bottom left
            elif self.x > 256  and self.x < 330 and self.y > 500 and self.y < 524 :
                self.x = self.x
                self.y = self.y

            #the cactus on the top right
            elif self.x > 1120  and self.x < 1195 and self.y > 100 and self.y < 124 :
                self.x = self.x
                self.y = self.y

            #the cactus on the bottom right
            elif self.x > 976  and self.x < 1058 and self.y > 540 and self.y < 564 :
                self.x = self.x
                self.y = self.y


            else :

                self.move_UP()


        # if we want to go at the bottom
        elif keys[pygame.K_DOWN]:

            #the first house
            if self.x > 72  and self.x < 280 and self.y > 308 and self.y < 400 :
                self.x = self.x
                self.y = self.y

            # the second house
            elif self.x >856  and self.x < 1070 and self.y > -60 and self.y < 0 :
                self.x = self.x
                self.y = self.y

            # the fontain's higher part
            elif self.x > 567 and self.x < 728 and self.y > 228 and self.y < 240 :
                self.x = self.x
                self.y = self.y

            # the fontain's lower part
            elif self.x > 536  and self.x < 778 and self.y >292 and self.y < 300 :
                self.x = self.x
                self.y = self.y

            # the cactus on the top left
            elif self.x >96  and self.x < 170 and self.y > -4 and self.y < 10 :
                self.x = self.x
                self.y = self.y

            #the cactus on the bottom left
            elif self.x > 256  and self.x < 330 and self.y > 428 and self.y < 490 :
                self.x = self.x
                self.y = self.y

            #the cactus on the top right
            elif self.x > 1120  and self.x < 1195 and self.y > 36 and self.y < 50 :
                self.x = self.x
                self.y = self.y

            #the cactus on the bottom right
            elif self.x > 976  and self.x < 1058 and self.y > 476 and self.y < 500 :
                self.x = self.x
                self.y = self.y

            else :

                self.move_DOWN()

        else :

            self.not_move()


        """ the second house in the desert """

    def sand_maison_2(self):

        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        print(self.x, self.y)

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            # village limitation
            if self.x < 20 :
                self.x = self.x
                self.y = self.y

           #the wall on the left
            elif self.x > 0 and self.x < 100 and self.y > 0 and self.y < 720 :
                self.not_move()

            #the bed
            elif self.x > 300 and self.x < 380 and self.y > 0 and self.y < 252 :
                self.not_move()

            #the first house
            elif self.x > 900 and self.x < 956 and self.y > 0 and self.y < 188 :
                self.not_move()

            #the table
            elif self.x > 900 and self.x < 980 and self.y > 380 and self.y < 468 :
                self.not_move()

            #the bottom
            elif self.x > 700 and self.x < 750 and self.y > 620 and self.y < 720 :
                self.not_move()

            else :
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the first house
            if self.x > 64 and self.x < 100  and self.y > 308 and self.y < 532:
                self.not_move()

            #the bed
            elif self.x > 220 and self.x < 260 and self.y > 0 and self.y < 252 :
                self.not_move()

            #the shelf and the desk
            elif self.x > 508 and self.x < 600 and self.y > 0 and self.y < 164 :
                self.not_move()

            #the chair
            elif self.x > 860 and self.x < 900 and self.y > 0 and self.y < 188 :
                self.not_move()

            #the table
            elif self.x > 876 and self.x < 890 and self.y > 380 and self.y < 468 :
                self.not_move()

            #the bottom
            elif self.x > 500 and self.x < 516 and self.y > 620 and self.y < 720 :
                self.not_move()

            #the wall on the right
            elif self.x > 1180 and self.x < 1270 and self.y > 0 and self.y < 720 :
                self.not_move()


            else :
               self.move_RIGHT()


        # if we want to go at the top
        elif keys[pygame.K_UP]  :

            # the village limitations
            if self.y < 5 :
                self.not_move()

            #the dresser
            elif self.x > 0 and self.x < 212 and self.y > 0 and self.y < 156 :
                self.not_move()

            #the bed
            elif self.x > 220 and self.x < 380 and self.y > 0 and self.y < 252 :
                self.not_move()

            #the shelf and the desk
            elif self.x > 508 and self.x < 1270 and self.y > 0 and self.y < 164 :
                self.not_move()

            #the chair
            elif self.x > 860 and self.x < 956 and self.y > 0 and self.y < 188 :
                self.not_move()

            #the table
            elif self.x > 876 and self.x < 980 and self.y > 380 and self.y < 400 :
                self.not_move()

            else :
               self.move_UP()


        # if we want to go at the bottom
        elif keys[pygame.K_DOWN]:

            #the first house
            if self.x > 72  and self.x < 280 and self.y > 308 and self.y < 400 :
                self.not_move()

            #the table
            elif self.x > 876 and self.x < 980 and self.y > 410 and self.y < 468 :
                self.not_move()

            #the bottom
            elif self.x > 0 and self.x < 516 and self.y > 620 and self.y < 720 :
                self.not_move()


            elif self.x > 700 and self.x < 1270 and self.y > 620 and self.y < 720 :
                self.not_move()



            else :
                self.move_DOWN()

        else:
            self.not_move()


    """ the second house in the desert """

    """ the fisrt house in the desert """

    def sand_maison_1(self):

        # actions on the  keyboard
        keys = pygame.key.get_pressed()
        print(self.x, self.y)

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            # village limitation
            if self.x < 20 :
                self.x = self.x
                self.y = self.y

            #the first table
            elif self.x < 108 and self.y > 550  and self.y < 720  :
                self.not_move()

            #the first chair
            elif self.x > 0 and self.x < 124  and self.y > 484  and self.y < 556  :
                self.not_move()

            #the second table
            elif self.x > 0  and self.x < 92  and self.y > 276  and self.y < 420 :
                self.not_move()

            #the second chair
            elif self.x > 0 and self.x < 140 and self.y > 316 and self.y < 388 :
                self.not_move()

            #the first shelf
            elif self.x > 0 and self.x < 156 and self.y > 0 and self.y < 148 :
                self.not_move()

            #the first bed
            elif self.x > 212 and self.x < 292 and self.y > 0 and self.y < 204 :
                self.not_move()

            #the second shelf
            elif self.x > 400 and self.x < 436 and self.y > 0 and self.y < 148 :
                self.not_move()

            #the second bed
            elif self.x > 530 and self.x < 580 and self.y > 0 and self.y < 204 :
                self.not_move()

            #the third shelf
            elif self.x > 700 and self.x < 740 and self.y > 0 and self.y < 156 :
                self.not_move()

            #the first bench
            elif self.x > 1000 and self.x < 1052 and self.y > 0 and self.y < 140 :
                self.not_move()

            # the table and chair
            elif self.x > 1000 and self.x < 1084 and self.y > 252 and self.y < 484 :
                self.not_move()

            #the entrance
            elif self.x > 724 and self.x < 800 and self.y > 620 and self.y < 650 :
                self.not_move()



            else :
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the first house
            if self.x > 64 and self.x < 100  and self.y > 308 and self.y < 532:
                self.not_move()

            #the first bed
            elif self.x > 164 and self.x < 215 and self.y > 0 and self.y < 204 :
                self.not_move()

            #the second shelf
            elif self.x > 284 and self.x < 300  and self.y > 0 and self.y < 148 :
                self.not_move()

            #the second bed
            elif self.x > 468 and self.x < 500 and self.y > 0 and self.y < 204 :
                self.not_move()

            #the third shelf
            elif self.x > 596  and self.x < 600 and self.y > 0 and self.y < 156 :
                self.not_move()

            #the first bench
            elif self.x > 852 and self.x < 900 and self.y > 0 and self.y < 140 :
                self.not_move()

            #the table and chair
            elif self.x > 828 and self.x < 900 and self.y > 252 and self.y < 484 :
                self.not_move()

            #the bottom
            elif self.x > 724 and self.x < 800 and self.y > 620 and self.y < 650 :
                self.not_move()

            #the two bench
            elif self.x > 1164 and self.x < 1200 and self.y > 180 and self.y < 620 :
                self.not_move()


            else :
               self.move_RIGHT()


        # if we want to go at the top
        elif keys[pygame.K_UP]  :

            # the village limitations
            if self.y < 5 :
                self.not_move()

           #the first table
            elif self.x > 0 and self.x < 92 and self.y > 548 and self.y < 604 :
                self.not_move()

            #the first chair
            elif self.x > 0 and self.x < 124 and self.y > 501 and self.y < 556 :
                self.not_move()

            #the second table
            elif self.x > 0 and self.x < 92 and self.y > 276 and self.y < 300 :
                self.not_move()

            #the second chair
            elif self.x > 0 and self.x < 140 and self.y > 320 and self.y < 388 :
                self.not_move()

            #the first shelf
            elif self.x > 0 and self.x < 156 and self.y > 140 and self.y < 148 :
                self.not_move()

            #the second shelf
            elif self.x > 284 and self.x < 436 and self.y > 0 and self.y < 148 :
                self.not_move()

            #the second bed
            elif self.x > 468 and self.x < 580 and self.y > 0 and self.y < 204 :
                self.not_move()

            #the third shelf
            elif self.x > 596 and self.x < 740 and self.y > 0 and self.y < 156 :
                self.not_move()

            #the first bench
            elif self.x > 852 and self.x < 1052 and self.y > 0 and self.y < 140 :
                self.not_move()

            #the two bench
            elif self.x > 1164 and self.x < 1270 and self.y > 180 and self.y < 200 :
                self.not_move()

            #the table and chairs
            elif self.x > 828 and self.x < 1084 and self.y > 400 and self.y < 484 :
                self.not_move()

            #the first bed
            elif self.x > 164 and self.x < 292 and self.y > 199 and self.y < 204 :
                self.not_move()

            #the two bench
            elif self.x > 1164 and self.x < 1270 and self.y > 600 and self.y < 620 :
                self.not_move()

            #the table and chair
            elif self.x > 828 and self.x < 1084  and self.y > 260 and self.y < 300 :
                self.not_move()

            #the bottom limitations
            elif self.x > 0 and self.x < 524 and self.y > 620 and self.y < 650 :
                self.not_move()

            elif self.x > 724 and self.x < 1270 and self.y > 620 and self.y < 650 :
                self.not_move()

            else :
               self.move_UP()


        # if we want to go at the bottom
        elif keys[pygame.K_DOWN]:

            #the first house
            if self.x > 72  and self.x < 280 and self.y > 308 and self.y < 400 :
                self.not_move()

           #the first table
            elif self.x > 0 and self.x < 92 and self.y > 444 and self.y < 524 :
                self.not_move()

            #the first chair
            elif self.x > 0 and self.x < 124 and self.y > 484 and self.y < 500 :
                self.not_move()

            #the second table
            elif self.x > 0 and self.x < 92 and self.y > 400 and self.y < 420 :
                self.not_move()

            #the second chair
            elif self.x > 0 and self.x < 140 and self.y > 316 and self.y < 300 :
                self.not_move()



            else :
                self.move_DOWN()

        else:
            self.not_move()

    """ the first house in the desert"""


    """ the montain village """

    def montagne_village(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            # the old man mansion
            if self.x > 690 and self.x < 730 and self.y > 22 and self.y < 286 :
                self.not_move()

            else:
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the old man mansion
            if self.x > 448 and self.x < 504 and self.y > 28 and self.y < 276 :
                self.not_move()

            else :

                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:

            # the old man door on the left
            if self.x > 448 and self.x < 560 and self.y > 236 and self.y < 276 :
                self.not_move()

            # the old man door on the right
            elif self.x > 640 and self.x < 714 and self.y > 236 and self.y < 276 :
                self.not_move()

            else :

                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:

            self.move_DOWN()


        else :
            self.not_move()


    """ the montain village """



    """ the montain with the volcano """

    def montagne_volcan(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:
            # the higher level
            if self.x > 0 and self.x < 1270 and self.y > 283 and self.y < 300 :
                self.not_move()

            # the volcano
            elif self.x > 691 and self.x < 795 and self.y > 0 and self.y < 299 :
                self.not_move()

            else :
                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:

            # the lower level
            if self.x > 0 and self.x < 1270 and self.y > 50 and self.y < 531 :
                self.not_move()

            else :
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:

            # the higher level
            if self.x > 0 and self.x < 1270 and self.y > 283 and self.y < 300 :
                self.not_move()

            # the area limitation on the left
            elif self.x > 0 and self.x < 467 and self.y > 625 and self.y < 640 :
                self.not_move()

            # the area limitaion on the right
            elif self.x > 819 and self.x < 1270 and self.y > 627 and self.y < 640 :
                self.not_move()

            else :
                self.move_DOWN()


        else :
            self.not_move()

    """ the montain with the volcano """


    """ the montain second part"""

    def montagne_2(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:
            # the area top
            if self.x > 0 and self.x < 10 and self.y > 0 and self.y < 331 :
                self.not_move()

            #the area bottom
            elif self.x > 0 and self.x < 140 and self.y > 467 and self.y < 720 :
                self.not_move()

            # the ladder
            elif self.x > 156 and self.x < 212 and self.y > 283 and self.y < 507 :
                self.not_move()


            else :
                self.move_LEFT()


        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the ladder
            if self.x > 220 and self.x < 268 and self.y > 283 and self.y < 507 :
                self.not_move()

            else :

                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:
            # the bottom level left
            if self.x > 0 and self.x < 172 and self.y > 475 and self.y < 523 :
                self.not_move()

            # the level bottom right
            elif self.x > 260 and self.x < 1270 and self.y > 475 and self.y < 523 :
                self.not_move()

            # the limitation area
            elif self.y < 2 :
                self.not_move()


            else :
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:

            # the erea limitation
            if self.x > 308 and self.x < 1270 and self.y > 619 and self.y < 627 :
                self.not_move()

            # the level on the left
            elif self.x > 0 and self.x < 164 and self.y > 283 and self.y < 315 :
                self.not_move()

            # the level on the right
            elif self.x > 260 and self.x < 1270 and self.y > 283 and self.y < 315 :
                self.not_move()

            # the bottmo area limit
            elif self.x > 420 and self.x < 1270 and self.y > 635 and self.y < 720 :
                self.not_move()



            else :
                self.move_DOWN()


        else :
            self.not_move()

    """ the montain second part"""


    """ the montain area one """


    def montagne_1(self):
        # actions on the  keyboard
        keys = pygame.key.get_pressed()

        # if we want to to on the left
        if keys[pygame.K_LEFT]:

            # the limit level
            if self.x > 708 and self.x < 780 and self.y > 0 and self.y < 236 :
                self.not_move()


            # the river on the other side
            elif self.x < 30 and self.x < 1200 and self.y > 32 and self.y < 528 :
                self.not_move()

            # the ladder
            elif self.x > 956 and self.x < 1015 and self.y > 204 and self.y < 508 :
                self.not_move()

            else :
                self.move_LEFT()

        # if we want to go on the right
        elif keys[pygame.K_RIGHT]:

            # the arae limitation
            if self.x > 1220 :
                self.not_move()

            # level limit
            elif self.x > 724 and self.x < 756 and self.y > 0 and self.y < 500 :
                self.not_move()

            # the ladder
            elif self.x > 1020 and self.x < 1080 and self.y > 204 and self.y < 508 :
                self.not_move()

            else:

                self.move_RIGHT()



        # if we want to to on the left
        elif keys[pygame.K_UP]:

            # the top limit of the lower level
            if self.x > -20 and self.x < 740 and self.y > 0 and self.y < 10 :
                self.not_move()

            #the higher level
            elif self.x > 748 and self.x < 964 and self.y > 468 and self.y < 508 :
                self.not_move()

            # the higher level second part
            elif self.x > 1058 and self.x < 1270 and self.y > 468 and self.y < 508 :
                self.not_move()

            else:
                self.move_UP()


        # if we want to to on the left
        elif keys[pygame.K_DOWN]:

            # the level limit on the left
            if self.x > 755 and self.x < 964 and self.y > 204 and self.y < 228 :
                self.not_move()

            # the level limit on the right
            elif self.x > 1059 and self.x < 1270 and self.y > 204 and self.y < 228 :
                self.not_move()

            # the bottmo area limit
            elif self.x > 0 and self.x < 1270 and self.y > 620 and self.y <625 :
                self.not_move()

            else :

                self.move_DOWN()


        else :
            self.not_move()



    """ the montain are one """




    """###FONCTIONS LIMITES"""



    """###FONCTIONS TEXTE"""

    def displayTexte(self):   #displaying the dialogue

        window.blit(self.bloc,(0,0))
        self.back.blit(self.bloc,(0,0))

        window.blit(self.texte0,(20,560))
        self.back.blit(self.texte0,(20,560))
        self.bloc.blit(self.texte0,(20,560))

        window.blit(self.texte1,(20,600))
        self.back.blit(self.texte1,(20,600))
        self.bloc.blit(self.texte1,(20,600))

        window.blit(self.texte2,(20,640))
        self.back.blit(self.texte2,(20,640))
        bloc.blit(self.texte2,(20,640))

        window.blit(self.texte3,(20,680))
        self.back.blit(self.texte3,(20,680))
        self.bloc.blit(self.texte3,(20,680))



    def texte(self):

        myfont=pygame.font.SysFont('Times New Roman',30)

        if self.t==1 :

            self.bloc=pygame.image.load("textes/texte.png")



            with open(self.message, 'r') as mon_fichier: #counting how much lines there are
                a = mon_fichier.read()
                self.n2 = a.count("\n") + 1

            with open(self.message, 'r') as mon_fichier:  #counting if one line is superior than n characters
                for i in range(a.count("\n") + 1): #since the self.n2 will change

                    b = mon_fichier.readline()

                    if len(b) > n :   #if that's so, line is counted as double or more since the screen won't be able to print it either way
                        self.n2 += floor(len(b)/n)


            if self.n2>4:
                self.tLong=1  #if self.message is long
            else :
                self.erase=1 #if it's not so the list of lines will be erased properly


            self.n3=ceil(self.n2/4) #turns of 4 lines which will be printed


            with open(self.message, 'r') as mon_fichier:
                for i in range(self.n3*4):  #turns of 4 lines which will be printed, we do not put self.n3 here cuz self.n2 might change

                    l= mon_fichier.readline(n).strip()  #read all the lines properly

                    self.lignes.append(l) #put them in a list



            self.texte0=myfont.render(self.lignes[0],False,(250,250,250))  #makes list's text as surface
            self.texte1=myfont.render(self.lignes[1],False,(250,250,250))
            self.texte2=myfont.render(self.lignes[2],False,(250,250,250))
            self.texte3=myfont.render(self.lignes[3],False,(250,250,250))



            if self.erase == 1 :
                self.lignes=[]
                self.erase = 0






        else :

            #if there's no dialogue, transparent things are printed at the screen

            self.bloc=pygame.image.load("transparent.png")
            self.texte0=self.texte1=self.texte2=self.texte3=myfont.render("",False,(0,0,0))










    def Long(self):

        myfont=pygame.font.SysFont('Times New Roman',30)




        if self.i < self.n3-1:  #we print the next four lines which are in the list depending on which turn of self.n3 we are

            self.bloc=pygame.image.load("textes/texte.png")
            self.texte0=myfont.render(self.lignes[n4+(4*self.i)],False,(250,250,250))
            self.texte1=myfont.render(self.lignes[n4+1+(4*self.i)],False,(250,250,250))
            self.texte2=myfont.render(self.lignes[n4+2+(4*self.i)],False,(250,250,250))
            self.texte3=myfont.render(self.lignes[n4+3+(4*self.i)],False,(250,250,250))



        self.i+=1

        if self.i==self.n3:

            #variables histoire

            if self.message == "textes/marchand_arme.txt" :
                self.arme = 1
            if self.message == "textes/fleuve_goddess.txt" :
                self.mission1 = 1

            #variables histoire

            self.lignes=[]
            self.t=0
            self.tLong=0
            self.i=0


    """###FONCTIONS TEXTE"""




    """###CHANGEMENT POSITION/MAP + APPEL TEXTE + VARIABLES"""

    def area_perso(self):      #fonction main qui appelle toutes les autres fonctions qui font parties de l'interaction entre le joueur et le jeu
                                #et qui permet le changement de variables booléennes propres à l'histoire

        keys = pygame.key.get_pressed()

        #PARTIE LIMITES

        """desert"""

        if self.zone == 'backgrounds/sand_village.png':
            self.sand_village()

        # a fonction managing the limit of the zone and what is inside
        elif self.zone == 'backgrounds/sand_maison_1.png':
            self.sand_maison_1()

        # a fonction managing the limit of the zone and what is inside
        elif self.zone == 'backgrounds/sand_maison_2.png':
            self.sand_maison_2()


        elif self.zone == 'backgrounds/sand_oasis.png':
            self.sand_oasis()

        elif self.zone == 'backgrounds/desert_1.png':
            self.desert_1()

        elif self.zone == 'backgrounds/desert_2.png':
            self.desert_2()

        """desert"""


        """foret"""

        if self.zone == "backgrounds/foret_desert.png":
            self.foret_desert()

        elif self.zone == 'backgrounds/foret_road.png':
            self.foret_road()

        elif self.zone == 'backgrounds/foret_fontaine.png':
            self.foret_fontaine()

        elif self.zone == 'backgrounds/foret_village.png':
            self.foret_village()

        elif self.zone == "backgrounds/maison_vieux.png" :
            self.maison_vieux()

        """foret"""


        """fleuve"""


        if self.zone == 'backgrounds/fleuve_1.png':
            self.fleuve_1()

        elif self.zone == 'backgrounds/fleuve_2.png':
            self.fleuve_2()

        elif self.zone == 'backgrounds/fleuve_3.png':
            self.fleuve_3()

        elif self.zone == 'backgrounds/fleuve_village.png':
            self.fleuve_village()

        elif self.zone =="backgrounds/fleuve_maison_1.png" :
            self.fleuve_maison_1()

        elif self.zone == "backgrounds/fleuve_maison_2.png" :
            self.fleuve_maison_2()

        """fleuve"""


        """montagne"""

        if self.zone == 'backgrounds/montagne_1.png':
            self.montagne_1()

        elif self.zone == 'backgrounds/montagne_2.png':
            self.montagne_2()

        elif self.zone == 'backgrounds/montagne_volcan.png':
            self.montagne_volcan()

        elif self.zone == 'backgrounds/montagne_village.png':
            self.montagne_village()

        """montagne"""



        #PARTIE LIMITES

        #print(self.x,self.y,self.t,self.message)



        #PARTIE TEXTE

        if self.start == 1 :  #INTRO TEXTE
            self.message = "textes/debut.txt"
            self.t = 1
            self.start = 0

        if self.dia == 1 : #part for saying yes to display text
            if keys[pygame.K_q]:
                self.t=1
                self.dia = 0

        if self.fish == 1 :
            self.message = "textes/fin_fish.txt"
            self.t = 1
            self.fish = 0



        if self.tLong==0:
            self.texte()

        if self.tLong!=1 and keys[pygame.K_d]:
            self.t=0

        elif self.tLong==1 :
            if keys[pygame.K_d]:
                self.Long()
                time.sleep(0.2)


        #PARTIE TEXTE


        #PARTIE USING OBJECTS

        #print(self.can,self.mission1)

        if self.mission1 == 1 and keys[pygame.K_i]:
            self.can = 1

        if self.can == 1 and keys[pygame.K_d]:
            self.can = 0


        #PARTIE USING OBJECTS


    """###CHANGEMENT POSITION/MAP + APPEL TEXTE + VARIABLES"""



    """IMAGE POSITION PERSO"""

    def draw(self, window):

        self.backGround()   #on appelle les deux autres fonctions permettant l'affichage et les interactions joueur/jeu
        self.area_perso()   #cela permet de n'appeler que self.draw() dans la boucle main

        print(self.message)


        self.hitBox = (self.x -5 , self.y -2, self.width , self.height +35)
        #pygame.draw.rect(window, (255, 0, 0),self.hitBox, 2)


        # pour éviter les erreur d'index dans la liste, car en tout dans chaque liste il y a 9 images (la dernière a pour index 8)
        if self.walkCount  > 8:
            self.walkCount = 0


        # si on veut aller a droite
        if self.right and self.life == 1:
            # image à afficher et se position dans la fenêtre
            window.blit(walkRight[self.walkCount], (self.x, self.y))
            self.back.blit(walkRight[self.walkCount], (self.x, self.y))
            self.walkCount+=1

        # si on veut aller à gauche
        elif self.left and self.life == 1:
            # image à afficher et se position dans la fenêtre
            window.blit(walkLeft[self.walkCount], (self.x, self.y))
            self.back.blit(walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount+=1

        elif self.up and self.life == 1:
            window.blit(walkUp[self.walkCount], (self.x, self.y))
            self.back.blit(walkUp[self.walkCount], (self.x, self.y))
            self.walkCount+=1

        elif self.down and self.life == 1:
            window.blit(walkDown[self.walkCount], (self.x, self.y))
            self.back.blit(walkDown[self.walkCount], (self.x, self.y))
            self.walkCount+=1


        # si on ne fait rien
        else :

            window.blit(charDOWN, (self.x, self.y))
            self.back.blit(charDOWN, (self.x, self.y))



        self.displayTexte()



    """IMAGE POSITION PERSO"""













