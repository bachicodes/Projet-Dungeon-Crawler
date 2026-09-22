from dictionnaires import *

def deplacement(x,y,pile):
    for i in range(4):

        if x >= liste_fleches[i][0] and x <= (liste_fleches[i][0]+100) and y >= liste_fleches[i][1] and y <= (liste_fleches[i][1]+40):
            if donjon[pile[-1]]["sorties"][i] != None:
                print(i)
                pile.append(donjon[pile[-1]]["sorties"][i])
                return pile
    if x >= 0 and x <= 100 and y >= 0 and y <= 40:
        if len(pile) > 1:
            pile.pop()
            return pile
    return pile

def prendre_degats(degats):
    perso["pv"] = perso["pv"] - degats//perso["def"]
    return perso["pv"]

def mettre_degats(cible):
    cible["pv"] = cible["pv"] - perso["atq"]
    return cible["pv"]

def combat(pile):
    #print(prendre_degats(monstres[donjon[pile[-1]]["monstre"]]["atq"]))
    pass