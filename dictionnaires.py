import random

liste_fleches = [(450,560),(0,280),(450,0),(900,280)]

nb = random.randint(1,100)
if nb == 1:
    baton = "le_baton"

else:
    baton = "baton"

nb = random.randint(1,6)
if nb == 1:
    armure = "armure_1"
elif nb <= 3:
    armure = "armure_2"
else:
    armure = "armure_3"

donjon = {
    "entree" : {
        "nom" : "Entrée",
        "sorties" : [None,"armurerie","hall",None],
        "objet" : baton,
        "monstre" : None
    },

    "hall" : {
        "nom" : "Hall Principal",
        "sorties" : ["entree", "cuisine", "bibliotheque", "escaliers"],
        "objet" : None,
        "monstre" : "fantome",
    },

    "escaliers" : {
        "nom" : "Escaliers",
        "sorties" : ["hall", None, "chambre", None],
        "objet" : "balai",
        "monstre" : None,
    },

    "chambre" : {
        "nom" : "Chambre",
        "sorties" : ["escaliers", None, "salle_de_bain", None],
        "objet" : "cle",
        "monstre" : "gobelins",
    },

    "salle_de_bain" : {
        "nom" : "Salle de Bain",
        "sorties" : ["chambre",None,None,None],
        "objet" : None,
        "monstre" : None,
    },

    "cuisine" : {
        "nom" : "Cuisine",
        "sorties" : ["hall",None,None,None],
        "objet" : "pass",
        "monstre" : "rat",
    },

    "armurerie" : {
        "nom" : "Armurerie",
        "sorties" : ["entree",None,None,None],
        "objet" : armure,
        "monstre" : "squelette",
    },

    "bibliotheque" : {
        "nom" : "Bibliotheque",
        "sorties" : ["hall", None, None, "boss"],
        "objet" : None,
        "monstre" : "sorcier",
    },

    "boss" : {
        "nom" : "Salle du Boss",
        "sorties" : ["bibliotheque", None, None, None],
        "objet" : None,
        "monstre" : "oeil",
    }
}


nom = input("Quel est votre nom ?")

perso = {
    "nom" : nom,
    "atq" : 1,
    "def" : 1,
    "pv" : 10,
    "niveau" : 1,
    "exp" : 0,
    "exp_niveau" : 5,
    "arme" : "poings",

    "moments_cles" : {
        "armurerie_ouverte" : False,
        "pass" : False,
        "cle" : False,
        "passage_bibliotheque" : False,
        "porte_boss" : False
    }
}

monstres = {
    "fantome" : {
        "pv" : 5,
        "atq" : 1,
        "exp" : 3,
        "drop" : []
    },
    "gobelins" : {
        "pv" : 30,
        "atq" : 6,
        "exp" : 20,
        "drop" : []
    },
    "rat" : {
        "pv" : 25,
        "atq" : 5,
        "exp" : 15,
        "drop" : []
    },
    "squelette" : {
        "pv" : 20,
        "atq" : 10,
        "exp" : 10,
        "drop" : []
    },
    "sorcier" : {
        "pv" : 45,
        "atq" : 8,
        "exp" : 50,
        "drop" : []
    },
    "oeil" : {
        "pv" : 100,
        "atq" : 20,
        "exp" : 100,
        "drop" : []
    },
}