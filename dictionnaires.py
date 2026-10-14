import random #importe le module random

liste_fleches = [(450,560),(0,280),(450,0),(900,280)] #liste des coordonnees de chaque bouton

nb = random.randint(1,100) # 1 chance sur 100 d'avoir un bâton spécial
if nb == 1:
    baton = "le_baton"
else:
    baton = "baton"

nb = random.randint(1,6) # choisis quel armure on obtient après le combat contre le squelette
if nb <= 1:
    armure = "armure_1"
elif nb <= 5:
    armure = "armure_2"
else:
    armure = "armure_3"

donjon = {
    #Range chaque salle avec:
    #- nom
    #- une liste de sorties correspondant aux boutons
    #- l'objet de la salle si il y en a un
    #- le monstre de la salle si il y en a un

    "entree" : {
        "nom" : "Entrée",
        "sorties" : [None,"armurerie","hall",None],
        "objet" : baton,
        "monstre" : None
    },

    "hall" : {
        "nom" : "Hall Principal",
        "sorties" : ["entree", "cuisine", "bibliotheque", "escaliers"],
        "objet" : "chandelier",
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
        "objet" : "chaussons",
        "monstre" : "gobelins",
    },

    "salle_de_bain" : {
        "nom" : "Salle de Bain",
        "sorties" : ["chambre",None,None,None],
        "objet" : "savon",
        "monstre" : None,
    },

    "cuisine" : {
        "nom" : "Cuisine",
        "sorties" : ["hall",None,None,None],
        "objet" : "ragout",
        "monstre" : "rat",
    },

    "armurerie" : {
        "nom" : "Armurerie",
        "sorties" : ["entree",None,None,None],
        "objet" : None,
        "monstre" : "squelette",
    },

    "bibliotheque" : {
        "nom" : "Bibliotheque",
        "sorties" : ["hall", None, None, "boss"],
        "objet" : "chapeau",
        "monstre" : "sorcier",
    },

    "boss" : {
        "nom" : "Salle du Boss",
        "sorties" : ["bibliotheque", None, None, None],
        "objet" : None,
        "monstre" : "oeil",
    }
}




base = {
    
    #crée la structure du joueur : nom, pv, expérience, et autres types de statistiques

    "atq" : 1,
    "def" : 1,
    "pv" : 10,
    "pv_max" : 10,
    "niveau" : 1,
    "exp" : 0,
    "exp_niveau" : 5,
    "arme" : "balai",
    "armure" : None,

    "moments_cles" : {
        "baton_recupere" : False,
        "chandelier_recupere" : False,
        "louche_recupere" : False,
        "balai_recupere" : False,
        "armurerie_ouverte" : False,
        "pass" : False,
        "cle" : False,
        "passage_bibliotheque" : False,
        "porte_boss" : False,

    }
}

perso = base.copy() #crée une copie du dictionnaire base pour que le redémmarage (mort du joueur) soit plus simple


monstres = {
    '''
    Répertorie les caractéristiques de chaque monstre
    '''
    "fantome" : {
        "pv" : 5,
        "atq" : 1,
        "exp" : 3,
    },
    "squelette" : {
        "pv" : 20,
        "atq" : 8,
        "exp" : 10,
    },
    "rat" : {
        "pv" : 25,
        "atq" : 5,
        "exp" : 15,
    },
    "gobelins" : {
        "pv" : 30,
        "atq" : 6,
        "exp" : 20,
    },
    "sorcier" : {
        "pv" : 45,
        "atq" : 8,
        "exp" : 50,
    },
    "oeil" : {
        "pv" : 100,
        "atq" : 15,
        "exp" : 100,
    },
}

textes = [ # liste de tous les textes possibles
"Vous ne vous souvenez plus de qui vous êtes,",
"vous vous réveillez dans un manoir abandonné.",
"Votre but est d'en sortir.",




]