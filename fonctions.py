from dictionnaires import * # importe les valeurs du fichier dictionnaires.py
import pygame # import le module pygame pour pouvoir charger des images
pygame.init() # démarre pygame

def deplacement(x,y,pile,en_combat):
    '''
    permet l'utilisation des boutons
    '''
    for i in range(4): # boucle pour chaque bouton
        if liste_fleches[i][0] <= x <= (liste_fleches[i][0]+100) and liste_fleches[i][1] <= y <= (liste_fleches[i][1]+40): # si on clique bien sur un bouton
            if donjon[pile[-1]]["sorties"][i] != None: #si le bouton correspond à une sortie
                pile.append(donjon[pile[-1]]["sorties"][i]) # met la salle en haut de la pile pour que le lieu apparaît
                if pile[-1] == "armurerie" and not perso["moments_cles"]["armurerie_ouverte"]: # si l'on a accès à l'armurerie
                    pile.pop() # retire l'armurerie si elle n'est pas débloquée

    if x >= 0 and x <= 100 and y >= 0 and y <= 40: # condition pour le bouton retour
        if len(pile) > 1: #si la pile a au moins deux salles
            pile.pop()
    try:
        if monstres[donjon[pile[-1]]["monstre"]]["pv"] > 0 : en_combat = True
        else: en_combat = False
    except:
        en_combat = False
    #print(pile[-1])
    fond = pygame.image.load(f"{pile[-1]}.png").convert_alpha() # charge l'image du fond
    return pile,fond, en_combat

def prendre_degats(degats):
    '''
    retire des points de vie au joueur
    '''
    perso["pv"] = perso["pv"] - degats//perso["def"] # choisit le nombre de points de vie à enlever par rapport à la défense du joueur
    print(f'Le joueur a maintenant {perso["pv"]}PV.')


def mettre_degats(cible):
    '''
    cible : ennemi de la salle
    inflige des dégâts par rapport à l'attaque du joueur
    '''
    cible["pv"] -= perso["atq"]
    return cible["pv"]

def combat(pile, tour, en_combat):
    if tour == "joueur" :
        mettre_degats(monstres[donjon[pile[-1]]["monstre"]])
        print(monstres[donjon[pile[-1]]["monstre"]]["pv"])
        if monstres[donjon[pile[-1]]["monstre"]]["pv"] <= 0 : en_combat = False
        tour = "monstre"
    elif tour == "monstre":
        prendre_degats(monstres[donjon[pile[-1]]["monstre"]]["atq"])
        print(perso["pv"])
        if perso["pv"] <= 0 : en_combat = False
        tour = "joueur"

    return tour, en_combat

def drop(pile):
    if donjon[pile[-1]]["monstre"] == "fantome" or donjon[pile[-1]]["monstre"] == "oeil":
        return

    elif donjon[pile[-1]]["monstre"] == "squelette":
        if armure == "armure_1":
            def_armure = 1.5
            perso["armure"] = "armure_1"
        elif armure == "armure_2":
            def_armure = 2
            perso["armure"] = "armure_2"
        else:
            def_armure = 3
            perso["armure"] = "armure_2"

    elif donjon[pile[-1]]["monstre"] == "rat":
        if atq_arme < 5 :
            atq_arme = 5
            perso["arme"] = "louche"

        perso["moments_cles"]["pass"] = True

    elif donjon[pile[-1]]["monstre"] == "gobelins":
        atq_objet += 2

    else:
        nb = random.randint(1,2)
        if nb:
            perso["pv_max"] += 5
        else:
            atq_objet += 3

    return perso, atq_arme, atq_objet, def_armure, def_objet

def recuperer(x1,y1,lieu, atq_arme, atq_objet, def_armure, def_objet):
    if lieu == "entree":
        if 841 <= x1 <= 965 and 415 <= y1 <= 490 and not perso["moments_cles"]["baton_recupere"]:
            perso["moments_cles"]["baton_recupere"] = True
            atq_arme = 2
            perso["arme"] = baton
    elif lieu == "hall":
        if 672 <= x1 <= 735 and 373 <= y1 <= 431 and not perso["moments_cles"]["chandelier_recupere"]:
            perso["moments_cles"]["chandelier_recupere"] = True
            atq_arme = 3
            perso["arme"] = "chandelier"
    elif lieu == "escaliers":
        if 786 <= x1 <= 841 and 296 <= y1 <= 523 and not perso["moments_cles"]["balai_recupere"]:
            perso["moments_cles"]["balai_recupere"] = True
            atq_arme = 4
            def_objet += 1
            perso["arme"] = "balai"
        elif 796 <= x1 <= 824 and 299 <= y1 <= 356 and not perso["moments_cles"]["armurerie_ouverte"]: perso["moments_cles"]["armurerie_ouverte"] = True

    return perso, atq_arme, atq_objet, def_armure, def_objet