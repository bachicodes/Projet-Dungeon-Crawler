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
atq_arme = 1
atq_objet = 0
def_armure = 1
def_objet = 0
tour = "joueur"
attente = 120
en_combat = False
index_texte = 0

textes_menu = [ # liste de tous les textes du menu
"Vous ne vous souvenez plus de qui vous êtes,",
"vous vous réveillez dans un manoir abandonné.",
"Votre but est d'en sortir.",
"Touches :",
"- ESPACE : attaquer",
"- ENTREE : Parler/Dialogue"
]

#importation des images

armurerie = pygame.image.load("armurerie.png").convert_alpha()
balai_escaliers = pygame.image.load("balai_escaliers.png").convert_alpha()
barre_de_vie = pygame.image.load("barre_de_vie.png").convert_alpha()
boite_dialogue = pygame.image.load("boite_dialogue.png").convert_alpha()
boss_ferme = pygame.image.load("boss_ferme.png").convert_alpha()
boss_ouvert = pygame.image.load("boss_ouvert.png").convert_alpha()
bouton_0 = pygame.image.load("bouton_0.png").convert_alpha()
bouton_1 = pygame.image.load("bouton_1.png").convert_alpha()
bouton_menu0 = pygame.image.load("bouton_menu0.png").convert_alpha()
bouton_menu1 = pygame.image.load("bouton_menu1.png").convert_alpha()
chandelier = pygame.image.load("chandelier.png").convert_alpha()
chandelier_hall = pygame.image.load("chandelier_hall.png").convert_alpha()
chaussons = pygame.image.load("chaussons.png").convert_alpha()
cle = pygame.image.load("cle.png").convert_alpha()
etagere = pygame.image.load("etagere.png").convert_alpha()
fantome = pygame.image.load("fantome.png").convert_alpha()
fond = pygame.image.load(f"entree.png").convert_alpha()
fond_menu = pygame.image.load("menu.png").convert_alpha()
gobelins = pygame.image.load("gobelins.png").convert_alpha()
golem = pygame.image.load("golem.png").convert_alpha()
grille_fermee = pygame.image.load("grille_fermee.png").convert_alpha()
grille_ouverte = pygame.image.load("grille_ouverte.png").convert_alpha()
levier_0 = pygame.image.load("levier_0.png").convert_alpha()
levier_1 = pygame.image.load("levier_1.png").convert_alpha()
livre = pygame.image.load("livre.png").convert_alpha()
majordome = pygame.image.load("majordome.png").convert_alpha()
ombre_gobelins = pygame.image.load("ombre_gobelins.png").convert_alpha()
ombre_golem = pygame.image.load("ombre_golem.png").convert_alpha()
ombre_majordome = pygame.image.load("ombre_majordome.png").convert_alpha()
ombre_rat = pygame.image.load("ombre_rat.png").convert_alpha()
ombre_squelette = pygame.image.load("ombre_squelette.png").convert_alpha()
oeil = pygame.image.load("oeil.png").convert_alpha()
potion = pygame.image.load("potion.png").convert_alpha()
ragout = pygame.image.load("ragout.png").convert_alpha()
rat_face = pygame.image.load("rat_face.png").convert_alpha()
rat_dos = pygame.image.load("rat_dos.png").convert_alpha()
retour_0 = pygame.image.load("retour_0.png").convert_alpha()
retour_1 = pygame.image.load("retour_1.png").convert_alpha()
rideau_ferme = pygame.image.load("rideau_ferme.png").convert_alpha()
rideau_ouvert = pygame.image.load("rideau_ouvert.png").convert_alpha()
savon = pygame.image.load("savon.png").convert_alpha()
slot_arme = pygame.image.load("slot_arme.png").convert_alpha()
slot_armure = pygame.image.load("slot_armure.png").convert_alpha()
socle = pygame.image.load("socle.png").convert_alpha()
sorcier = pygame.image.load("sorcier.png").convert_alpha()
squelette = pygame.image.load(f"squelette_{armure}.png").convert_alpha()
surb_balai = pygame.image.load("surb_balai.png").convert_alpha()
surb_baton = pygame.image.load("surb_baton.png").convert_alpha()
surb_chandelier = pygame.image.load("surb_chandelier.png").convert_alpha()
surb_chaussons = pygame.image.load("surb_chaussons.png").convert_alpha()
surb_cle = pygame.image.load("surb_cle.png").convert_alpha()
surb_livre = pygame.image.load("surb_livre.png").convert_alpha()
surb_potion = pygame.image.load("surb_potion.png").convert_alpha()
surb_ragout = pygame.image.load("ragout.png").convert_alpha()
surb_rideau = pygame.image.load("surb_rideau.png").convert_alpha()
surb_savon = pygame.image.load("surb_savon.png").convert_alpha()
surb_tiroir = pygame.image.load("surb_tiroir.png").convert_alpha()
tiroir_ferme = pygame.image.load("tiroir_ferme.png").convert_alpha()
tiroir_ouvert = pygame.image.load("tiroir_ouvert.png").convert_alpha()

if donjon["entree"]["objet"] == "baton":
    baton_entree = pygame.image.load("baton_entree.png").convert_alpha()
else:
    baton_entree = pygame.image.load("le_baton_entree.png").convert_alpha()

def menu():
    fenetre.blit(fond_menu,(0,0))
    fenetre.blit(bouton_menu0,(0,0))
    if 347 <= pygame.mouse.get_pos()[0] <= 606 and 492 <= pygame.mouse.get_pos()[1] <= 545:
        fenetre.blit(bouton_menu1,(0,0))
    for i in range(6):
        texte = font.render(textes_menu[i], True, (255,255,255))
        fenetre.blit(texte,((1000-font.size(textes_menu[i])[0])//2,200+20*i))

def dialogue(index_texte):
    fenetre.blit(boite_dialogue,(17,411))
    if type(dialogues[index_texte]) == tuple:
        texte = font.render(dialogues[index_texte][0], True, (255,255,255))
        fenetre.blit(texte,(35,440))
        texte = font.render(dialogues[index_texte][1], True, (255,255,255))
        fenetre.blit(texte,(35,480))
    else:
        texte = font.render(dialogues[index_texte], True, (255,255,255))
        fenetre.blit(texte,(35,440))  
    
    

def rafraichissement(index_texte):
    if menu_affiche:
        menu()
        pygame.display.update()
        return

    if perso["pv"] <= 0:
        fenetre.fill((0,0,0))
        texte = font2.render("VOUS ÊTES MORT", True, (255,0,0))
        fenetre.blit(texte,(248,200))
        pygame.display.update()
        return

    fenetre.blit(fond,(0,0))

    if pile_lieu[-1] == "entree":
        fenetre.blit(socle,(0,0))
        fenetre.blit(ombre_majordome,(0,0))
        fenetre.blit(majordome,(0,0))
        if not perso["moments_cles"]["baton_recupere"]:
            fenetre.blit(baton_entree,(0,0))
            if 841 <= pygame.mouse.get_pos()[0] <= 965 and 415 <= pygame.mouse.get_pos()[1] <= 490:
                fenetre.blit(surb_baton,(0,0))
        if perso["moments_cles"]["armurerie_ouverte"]:
            fenetre.blit(grille_ouverte,(0,0))
        else:
            fenetre.blit(grille_fermee,(0,0))

    elif pile_lieu[-1] == "hall":
        fenetre.blit(ombre_golem,(0,0))
        fenetre.blit(golem,(0,0))
        if not perso["moments_cles"]["chandelier_recupere"]:
            fenetre.blit(chandelier_hall,(0,0))
            if 672 <= pygame.mouse.get_pos()[0] <= 735 and 373 <= pygame.mouse.get_pos()[1] <= 431:
                    fenetre.blit(surb_chandelier,(0,0))
        if monstres["fantome"]["pv"] > 0 :
            fenetre.blit(fantome,(0,0))
        

    elif pile_lieu[-1] == "escaliers":
        if perso["moments_cles"]["armurerie_ouverte"]: fenetre.blit(levier_1,(0,0))
        else: fenetre.blit(levier_0,(0,0))

        if not perso["moments_cles"]["balai_recupere"]:
            fenetre.blit(balai_escaliers,(0,0))
            if 786 <= pygame.mouse.get_pos()[0] <= 841 and 296 <= pygame.mouse.get_pos()[1] <= 523:
                    fenetre.blit(surb_balai,(0,0))

    elif pile_lieu[-1] == "armurerie":
        if monstres["squelette"]["pv"] > 0 : 
            fenetre.blit(ombre_squelette,(0,0))
            fenetre.blit(squelette,(0,0))
    
    elif pile_lieu[-1] == "cuisine":
        if monstres["rat"]["pv"] > 0 : 
            fenetre.blit(ombre_rat,(0,0))
            if en_dialogue : fenetre.blit(rat_dos,(0,0))
            else: fenetre.blit(rat_face,(0,0))
        elif not perso["moments_cles"]["ragout"]:
            fenetre.blit(ragout,(0,0))
            if 458 <= pygame.mouse.get_pos()[0] <= 539 and 284 <= pygame.mouse.get_pos()[1] <= 319:
                    fenetre.blit(surb_ragout,(0,0))

    elif pile_lieu[-1] == "chambre":
        if monstres["gobelins"]["pv"] > 0 : 
            fenetre.blit(ombre_gobelins,(0,0))
            fenetre.blit(gobelins,(0,0))
        if not perso["moments_cles"]["chaussons"]:
            fenetre.blit(chaussons,(0,0))
            if 860 <= pygame.mouse.get_pos()[0] <= 927 and 540 <= pygame.mouse.get_pos()[1] <= 592:
                    fenetre.blit(surb_chaussons,(0,0))
        if not perso["moments_cles"]["tiroir"]:
            fenetre.blit(tiroir_ferme,(0,0))
            if 727 <= pygame.mouse.get_pos()[0] <= 800 and 334 <= pygame.mouse.get_pos()[1] <= 400:
                    fenetre.blit(surb_tiroir,(0,0))
        else: 
            fenetre.blit(tiroir_ouvert,(0,0))
            if not perso["moments_cles"]["cle"]:
                fenetre.blit(cle,(0,0))
                if 725 <= pygame.mouse.get_pos()[0] <= 754 and 349 <= pygame.mouse.get_pos()[1] <= 377:
                        fenetre.blit(surb_cle,(0,0))

    elif pile_lieu[-1] == "salle_de_bain":
        if not perso["moments_cles"]["rideau"]:
            fenetre.blit(rideau_ferme,(0,0))
            if 363 <= pygame.mouse.get_pos()[0] <= 659 and 75 <= pygame.mouse.get_pos()[1] <= 434:
                    fenetre.blit(surb_rideau,(0,0))
        else: fenetre.blit(rideau_ouvert,(0,0))
        if not perso["moments_cles"]["savon"]:
            fenetre.blit(savon,(0,0))
            if 40 <= pygame.mouse.get_pos()[0] <= 97 and 375 <= pygame.mouse.get_pos()[1] <= 402:
                    fenetre.blit(surb_savon,(0,0))
    elif pile_lieu[-1] == "bibliotheque":
        if monstres["sorcier"]["pv"] > 0 :
            fenetre.blit(sorcier,(0,0))
        if not perso["moments_cles"]["couloir"]:
            fenetre.blit(etagere,(0,0))
            fenetre.blit(livre,(0,0))
            if 79 <= pygame.mouse.get_pos()[0] <= 144 and 212 <= pygame.mouse.get_pos()[1] <= 275:
                    fenetre.blit(surb_livre,(0,0))
        if not perso["moments_cles"]["potion"]:
            fenetre.blit(potion,(0,0))
            if 958 <= pygame.mouse.get_pos()[0] <= 997 and 328 <= pygame.mouse.get_pos()[1] <= 383:
                    fenetre.blit(surb_potion,(0,0))

    elif pile_lieu[-1] == "couloir":
        if perso["moments_cles"]["cle"]: fenetre.blit(boss_ouvert,(0,0))
        else : fenetre.blit(boss_ferme,(0,0))

    for i in range(4):
        if donjon[pile_lieu[-1]]["sorties"][i] != None and not en_dialogue:
            if liste_fleches[i][0]+100 >= pygame.mouse.get_pos()[0] >= liste_fleches[i][0] and liste_fleches[i][1]+40 >= pygame.mouse.get_pos()[1] >= liste_fleches[i][1]:
                fenetre.blit(bouton_1,liste_fleches[i])
            else:
                fenetre.blit(bouton_0,liste_fleches[i])
            if len(pile_lieu) > 1:
                if 100 >= pygame.mouse.get_pos()[0] >= 0 and 40 >= pygame.mouse.get_pos()[1] >= 0:
                    fenetre.blit(retour_1,(0,0))
                else:
                    fenetre.blit(retour_0,(0,0))
    if en_dialogue:
        dialogue(index_texte)

    if en_combat:
        texte = font.render(f"{donjon[pile_lieu[-1]]["monstre"]}: {monstres[donjon[pile_lieu[-1]]["monstre"]]["pv"]}PV", True, (255,255,255))
        fenetre.blit(texte,(250,586))


    pygame.draw.rect(fenetre, (0,255,0), (894, 14, (100/perso["pv_max"])*perso["pv"], 14))
    fenetre.blit(barre_de_vie,(890,10))
    texte = font.render(f"PV {perso['pv']}", True, (255,255,255))
    fenetre.blit(texte,(825,15))
    texte = font.render(f"ATQ {perso['atq']}", True, (255,255,255))
    fenetre.blit(texte,(925,40))
    texte = font.render(f"DEF {perso['def']}", True, (255,255,255))
    fenetre.blit(texte,(925,60))
    fenetre.blit(slot_arme,(940,80))
    if perso['arme'] != None:fenetre.blit(arme,(940,80))
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
            if menu_affiche:
                if 347 <= x1 <= 606 and 492 <= y1 <= 545:
                    menu_affiche = False
            elif perso["pv"] > 0 :
                if not en_dialogue and not menu_affiche and not en_combat:
                    pile_lieu, fond, en_combat, index_texte, en_dialogue = deplacement(x1,y1,pile_lieu,en_combat, index_texte, en_dialogue)
                    perso, atq_arme, atq_objet, def_armure, def_objet = recuperer(x1,y1,pile_lieu[-1], atq_arme, atq_objet, def_armure, def_objet)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not en_dialogue and not menu_affiche:
                    if attente == 120 and en_combat == True:
                        tour, en_combat = combat(pile_lieu, tour, en_combat, atq_arme, atq_objet, def_armure, def_objet)
                        attente = 0

            if event.key == K_RETURN and not en_combat:
                if pile_lieu[-1] == "entree":
                    if not en_dialogue: 
                        en_dialogue = True
                        index_texte = 0
                    elif index_texte < 3:
                        index_texte += 1
                    elif index_texte == 3:
                        en_dialogue = False
                elif pile_lieu[-1] == "hall":
                    if not en_dialogue: 
                        en_dialogue = True
                        index_texte = 4 + perso["moments_cles"]["pass"]
                    elif index_texte in (4,5):
                        en_dialogue = False
                elif pile_lieu[-1] in ("cuisine","chambre","bibliotheque","boss") and monstres[donjon[pile_lieu[-1]]["monstre"]]["pv"] > 0:
                    if en_dialogue:
                        en_dialogue = False
                        en_combat = True
                elif pile_lieu[-1] == "salle_de_bain" and perso["moments_cles"]["rideau"]:
                    if not en_dialogue: 
                        en_dialogue = True
                        index_texte = 8
                    elif index_texte < 9:
                        index_texte += 1
                    elif index_texte == 9:
                        en_dialogue = False
                        perso["pv"] = 0

                        
                        
    if attente == 120 and en_combat == True and tour == "monstre":
        tour, en_combat = combat(pile_lieu, tour, en_combat, atq_arme, atq_objet, def_armure, def_objet)
        attente = 0

    if attente < 120: attente += 1
    perso,  atq_objet, def_objet = levelUp(atq_objet, def_objet)
    perso["atq"] = atq_arme + atq_objet
    perso["def"] = def_armure + def_objet
    if perso['arme'] != None:arme = pygame.image.load(f"{perso['arme']}.png").convert_alpha()
    
    if perso["armure"] != None: armure = pygame.image.load(f"{perso['armure']}.png").convert_alpha()
    rafraichissement(index_texte)
    clock.tick(60)

pygame.font.quit()
pygame.quit()