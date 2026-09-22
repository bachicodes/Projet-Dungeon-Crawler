import random, pygame
from dictionnaires import *
from fonctions import *
from pygame.locals import *

pygame.init()
pygame.font.init()
fenetre = pygame.display.set_mode((1000,600))

#Variables
m = False
font = pygame.font.Font("PressStart2P.ttf",32)
pile_lieu = ["entree"]

#importation des images
fond =  pygame.image.load("fond.jpg").convert_alpha()
bouton_0 =  pygame.image.load("bouton_0.png").convert_alpha()
bouton_1 =  pygame.image.load("bouton_1.png").convert_alpha()
retour_0 =  pygame.image.load("retour_0.png").convert_alpha()
retour_1 =  pygame.image.load("retour_1.png").convert_alpha()
fond = pygame.transform.scale(fond,(1000,600))
ratface =  pygame.image.load("ratface.png").convert_alpha()
ratface = pygame.transform.scale(ratface,(217,369))

if donjon["entree"]["objet"] == "baton":
    baton = pygame.image.load("baton.png").convert_alpha()
else:
    baton = pygame.image.load("le_baton.png").convert_alpha()
baton = pygame.transform.scale(baton,(100,100))

def menu():
    texte = font.render("BONJOUR", True, (0,0,0))
    fenetre.blit(texte,(0,0))


def rafraichissement():
    fenetre.fill((255,255,255))
    if m:
        menu()
        pygame.display.update()
        return
    fenetre.fill((255,0,0))
    for i in range(4):
        if donjon[pile_lieu[-1]]["sorties"][i] != None:
            if liste_fleches[i][0]+100 >= pygame.mouse.get_pos()[0] >= liste_fleches[i][0] and liste_fleches[i][1]+40 >= pygame.mouse.get_pos()[1] >= liste_fleches[i][1]:
                fenetre.blit(bouton_1,liste_fleches[i])
            else:
                fenetre.blit(bouton_0,liste_fleches[i])
            #texte = font.render(donjon[pile_lieu[-1]]["sorties"][i], True, (0,0,0))
            #fenetre.blit(texte,(liste_fleches[i][0]+10,liste_fleches[i][1]+10))
            if len(pile_lieu) > 1:
                if 100 >= pygame.mouse.get_pos()[0] >= 0 and 40 >= pygame.mouse.get_pos()[1] >= 0:
                    fenetre.blit(retour_1,(0,0))
                else:
                    fenetre.blit(retour_0,(0,0))




    pygame.display.update()


clock = pygame.time.Clock()
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type==QUIT:
            continuer = False
        if event.type == MOUSEBUTTONUP :
            (x1,y1)=event.pos
            print(x1,y1)
            pile_lieu = deplacement(x1,y1,pile_lieu)

    rafraichissement()
    clock.tick(60)

pygame.font.quit()
pygame.quit()