import random, pygame
from dictionnaires import *
from fonctions import *
from pygame.locals import *

pygame.init()
pygame.font.init()
fenetre = pygame.display.set_mode((1000,600))

#Variables
en_dialogue = False
menu_affiche = True
font = pygame.font.Font("PressStart2P.ttf",12)
font2 = pygame.font.Font("PressStart2P.ttf",36)
pile_lieu = ["entree"]
index_texte = 0
atq_arme = 1
atq_objet = 0
def_armure = 1
def_objet = 0

#importation des images

armurerie = pygame.image.load("armurerie.png").convert_alpha()

barre_de_vie = pygame.image.load("barre_de_vie.png").convert_alpha()

boite_dialogue = pygame.image.load("boite_dialogue.png").convert_alpha()

bouton_0 = pygame.image.load("bouton_0.png").convert_alpha()
bouton_1 = pygame.image.load("bouton_1.png").convert_alpha()
chandelier = pygame.image.load("chandelier.png").convert_alpha()
chandelier_hall = pygame.image.load("chandelier_hall.png").convert_alpha()

bouton_menu0 = pygame.image.load("bouton_menu0.png").convert_alpha()
bouton_menu1 = pygame.image.load("bouton_menu1.png").convert_alpha()

fond = pygame.image.load(f"entree.png").convert_alpha()

grille_fermee = pygame.image.load("grille_fermee.png").convert_alpha()
grille_ouverte = pygame.image.load("grille_ouverte.png").convert_alpha()

fond_menu = pygame.image.load("menu.png").convert_alpha()
ratface = pygame.image.load("ratface.png").convert_alpha()
ratface = pygame.transform.scale(ratface,(217,369))

retour_0 = pygame.image.load("retour_0.png").convert_alpha()
retour_1 = pygame.image.load("retour_1.png").convert_alpha()

slot_arme = pygame.image.load("slot_arme.png").convert_alpha()
slot_armure = pygame.image.load("slot_armure.png").convert_alpha()

socle = pygame.image.load("socle.png").convert_alpha()

surb_baton = pygame.image.load("surb_baton.png").convert_alpha()
surb_chandelier = pygame.image.load("surb_chandelier.png").convert_alpha()


if donjon["entree"]["objet"] == "baton":
    baton_entree = pygame.image.load("baton_entree.png").convert_alpha()
else:
    baton_entree = pygame.image.load("le_baton_entree.png").convert_alpha()

def menu():
    fenetre.blit(fond_menu,(0,0))
    fenetre.blit(bouton_menu0,(0,0))
    if 347 <= pygame.mouse.get_pos()[0] <= 606 and 492 <= pygame.mouse.get_pos()[1] <= 545:
        fenetre.blit(bouton_menu1,(0,0))
    for i in range(3):
        texte = font.render(textes[i], True, (255,255,255))
        fenetre.blit(texte,((1000-font.size(textes[i])[0])//2,200+20*i))

def dialogue():
    fenetre.blit(boite_dialogue,(17,411))

def rafraichissement():
    if menu_affiche:
        menu()
        pygame.display.update()
        return

    if perso["pv"] <= 0:
        fenetre.fill((0,0,0))
        texte = font2.render("VOUS ÊTES MORT", True, (255,0,0))
        fenetre.blit(texte,(248,200))
        texte = texte = font.render(f"Recommencer", True, (255,255,255))
        if 347 <= pygame.mouse.get_pos()[0] <= 606 and 492 <= pygame.mouse.get_pos()[1] <= 545:
            texte = font.render(f"Recommencer", True, (255,255,0))
        fenetre.blit(texte,(400,250))
        pygame.display.update()
        return

    fenetre.blit(fond,(0,0))

    if pile_lieu[-1] == "entree":
        fenetre.blit(socle,(0,0))
        if not perso["moments_cles"]["baton_recupere"]:
            fenetre.blit(baton_entree,(0,0))
            if 841 <= pygame.mouse.get_pos()[0] <= 965 and 415 <= pygame.mouse.get_pos()[1] <= 490:
                fenetre.blit(surb_baton,(0,0))
        if perso["moments_cles"]["armurerie_ouverte"]:
            fenetre.blit(grille_ouverte,(0,0))
        else:
            fenetre.blit(grille_fermee,(0,0))
    elif pile_lieu[-1] == "hall":
        if not perso["moments_cles"]["chandelier_recupere"]:
            fenetre.blit(chandelier_hall,(0,0))
            if 672 <= pygame.mouse.get_pos()[0] <= 735 and 373 <= pygame.mouse.get_pos()[1] <= 431:
                    fenetre.blit(surb_chandelier,(0,0))

    for i in range(4):
        if donjon[pile_lieu[-1]]["sorties"][i] != None and not en_dialogue:
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
    if en_dialogue:
        dialogue()

    pygame.draw.rect(fenetre, (0,255,0), (894, 14, (100/perso["pv_max"])*perso["pv"], 14))
    fenetre.blit(barre_de_vie,(890,10))
    texte = font.render(f"PV {perso['pv']}", True, (255,255,255))
    fenetre.blit(texte,(825,15))
    texte = font.render(f"ATQ {perso['atq']}", True, (255,255,255))
    fenetre.blit(texte,(930,40))
    texte = font.render(f"DEF {perso['def']}", True, (255,255,255))
    fenetre.blit(texte,(930,60))
    fenetre.blit(slot_arme,(940,80))
    fenetre.blit(arme,(940,80))
    fenetre.blit(slot_armure,(940,135))
    if perso["armure"] != None: fenetre.blit(armure,(940,135))


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
            if menu_affiche:
                if 347 <= x1 <= 606 and 492 <= y1 <= 545:
                    menu_affiche = False
            elif perso["pv"] > 0 :
                #combat(pile_lieu)
                if not en_dialogue and not menu_affiche:
                    pile_lieu,fond = deplacement(x1,y1,pile_lieu)
                    perso, atq_arme, atq_objet, def_armure, def_objet = recuperer(x1,y1,pile_lieu[-1], atq_arme, atq_objet, def_armure, def_objet)




    perso["atq"] = atq_arme + atq_objet
    perso["def"] = def_armure + def_objet
    arme = pygame.image.load(f"{perso['arme']}.png").convert_alpha()
    if perso["armure"] != None: armure = pygame.image.load(f"{perso['armure']}.png").convert_alpha()
    rafraichissement()

    clock.tick(60)

pygame.font.quit()
pygame.quit()