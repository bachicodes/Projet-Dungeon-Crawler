from dictionnaires import * # importe les valeurs du fichier dictionnaires.py
import pygame # import le module pygame pour pouvoir charger des images
pygame.init() # démarre pygame

def deplacement(x,y,pile,en_combat, index_texte, en_dialogue):
    '''
    permet l'utilisation des boutons
    '''
    for i in range(4): # boucle pour chaque bouton
        if liste_fleches[i][0] <= x <= (liste_fleches[i][0]+100) and liste_fleches[i][1] <= y <= (liste_fleches[i][1]+40): # si on clique bien sur un bouton
            if donjon[pile[-1]]["sorties"][i] != None: #si le bouton correspond à une sortie
                if donjon[pile[-1]]["sorties"][i] == "hall":
                    monstres["fantome"]["pv"] = 5  
                pile.append(donjon[pile[-1]]["sorties"][i]) # met la salle en haut de la pile pour que le lieu apparaît
                if pile[-1] == "armurerie" and not perso["moments_cles"]["armurerie_ouverte"]: # si l'on a accès à l'armurerie
                    pile.pop() # retire l'armurerie si elle n'est pas débloquée
                elif pile[-1] == "bibliotheque" and not perso["moments_cles"]["pass"]:
                    pile.pop()
                elif pile[-1] == "boss" and not perso["moments_cles"]["cle"]:
                    pile.pop()

    if x >= 0 and x <= 100 and y >= 0 and y <= 40: # condition pour le bouton retour
        if len(pile) > 1: #si la pile a au moins deux salles
            pile.pop()
    if pile[-1] == "cuisine": index_texte = 6
    elif pile[-1] == "chambre": index_texte = 7
    elif pile[-1] == "bibliotheque": index_texte = 10
    elif pile[-1] == "boss": index_texte = 11
    if pile[-1] in ("cuisine","chambre","bibliotheque","boss") and monstres[donjon[pile[-1]]["monstre"]]["pv"] > 0: en_dialogue = True
    if pile[-1] == "armurerie" or pile[-1] == "hall":     
        if monstres[donjon[pile[-1]]["monstre"]]["pv"] > 0 : 
            en_combat = True
        else: en_combat = False
    
    fond = pygame.image.load(f"{pile[-1]}.png").convert_alpha() # charge l'image du fond
    return pile,fond, en_combat, index_texte, en_dialogue

def levelUp(atq_objet, def_objet):
    
    while perso["exp"] >= perso["exp_niveau"]:
        perso["exp"] -= perso["exp_niveau"]
        perso["exp_niveau"] += 3
        atq_objet += 1
        def_objet += 1
        perso["pv_max"] += 2
        perso["pv"] = perso["pv_max"]
        print("Vous montez de niveau ! (+1 ATQ et DEF, +2 PV max)")
    return perso, atq_objet, def_objet

def prendre_degats(degats):
    '''
    retire des points de vie au joueur
    '''
    perso["pv"] = perso["pv"] - degats//perso["def"] # choisit le nombre de points de vie à enlever par rapport à la défense du joueur
    
def mettre_degats(cible):
    '''
    cible : ennemi de la salle
    inflige des dégâts par rapport à l'attaque du joueur
    '''
    cible["pv"] -= perso["atq"]
    return cible["pv"]

def combat(pile, tour, en_combat, atq_arme, atq_objet, def_armure, def_objet):
    if tour == "joueur" :
        mettre_degats(monstres[donjon[pile[-1]]["monstre"]])
        if monstres[donjon[pile[-1]]["monstre"]]["pv"] <= 0 : 
            en_combat = False
            drop(pile, atq_arme, atq_objet, def_armure, def_objet)
        else: tour = "monstre"
    elif tour == "monstre":
        prendre_degats(monstres[donjon[pile[-1]]["monstre"]]["atq"])
        if perso["pv"] <= 0 : 
            en_combat = False
            perso["pv"] = 0
            print(f'Le joueur a maintenant {perso["pv"]}PV.')
        tour = "joueur"

    return tour, en_combat

def drop(pile, atq_arme, atq_objet, def_armure, def_objet):
    perso["pv"] = perso["pv_max"]
    perso["exp"] += monstres[donjon[pile[-1]]["monstre"]]["exp"]
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
            def_objet += 3
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
    elif lieu == "cuisine":
        if 458 <= x1 <= 539 and 284 <= y1 <= 319 and not perso["moments_cles"]["ragout"]:
            perso["moments_cles"]["ragout"] = True
            atq_objet += 1
    elif lieu == "chambre":
        if 860 <= x1 <= 927 and 540 <= y1 <= 592 and not perso["moments_cles"]["chaussons"]:
            perso["moments_cles"]["chaussons"] = True
            def_objet += 1
        if 727 <= x1 <= 800 and 334 <= y1 <= 400 and not perso["moments_cles"]["tiroir"]:
            perso["moments_cles"]["tiroir"] = True
        if 725 <= x1 <= 754 and 349 <= y1 <= 377 and not perso["moments_cles"]["cle"]:
            perso["moments_cles"]["cle"] = True
    elif lieu == "salle_de_bain":
        if 363 <= x1 <= 659 and 75 <= y1 <= 434 and not perso["moments_cles"]["rideau"]:
            perso["moments_cles"]["rideau"] = True
        if 40 <= x1 <= 97 and 375 <= y1 <= 402 and not perso["moments_cles"]["savon"]:
            perso["moments_cles"]["savon"] = True
            perso["pv_max"] += 1
            perso["pv"] = perso["pv_max"]
    elif lieu == "bibliotheque":
        if 958 <= x1 <= 997 and 328 <= y1 <= 383:
            perso["moments_cles"]["potion"] = True
            perso["pv_max"] += 2
            perso["pv"] = perso["pv_max"]
        if 79 <= x1 <= 144 and 212 <= y1 <= 275:
            perso["moments_cles"]["couloir"] = True


    return perso, atq_arme, atq_objet, def_armure, def_objet