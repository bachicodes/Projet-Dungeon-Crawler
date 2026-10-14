from dictionnaires import *
import pygame
pygame.init()

def deplacement(x,y,pile):
    for i in range(4):
        if liste_fleches[i][0] <= x <= (liste_fleches[i][0]+100) and liste_fleches[i][1] <= y <= (liste_fleches[i][1]+40):
            if donjon[pile[-1]]["sorties"][i] != None:
                print(i)
                pile.append(donjon[pile[-1]]["sorties"][i])
                if pile[-1] == "armurerie" and not perso["moments_cles"]["armurerie_ouverte"]:
                    pile.pop(-1)

    if x >= 0 and x <= 100 and y >= 0 and y <= 40:
        if len(pile) > 1:
            pile.pop()
    print(pile[-1])
    fond = pygame.image.load(f"{pile[-1]}.png").convert_alpha()
    return pile,fond

def prendre_degats(degats):
    perso["pv"] = perso["pv"] - degats//perso["def"]
    print(perso["pv"])
def mettre_degats(cible):
    cible["pv"] = cible["pv"] - perso["atq"]
    return cible["pv"]

def combat(pile):
    prendre_degats(1)
    #prendre_degats(monstres[donjon[pile[-1]]["monstre"]]["atq"])

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

    return perso, atq_arme, atq_objet, def_armure, def_objet