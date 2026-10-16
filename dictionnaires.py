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
        "sorties" : ["hall", "couloir", None, None],
        "objet" : "potion",
        "monstre" : "sorcier",
    },
    "couloir" : {
        "nom" : "Couloir",
        "sorties" : ["bibliotheque", None, "boss", None],
        "objet" : None,
        "monstre" : None,
    },
    "boss" : {
        "nom" : "Salle du Boss",
        "sorties" : ["couloir", None, None, None],
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
    "arme" : None,
    "armure" : None,

    "moments_cles" : {
        "baton_recupere" : False,
        "chandelier_recupere" : False,
        "louche_recupere" : False,
        "balai_recupere" : False,
        "armurerie_ouverte" : False,
        "pass" : False,
        "ragout": False,
        "chaussons" : False,
        "savon" : False,
        "tiroir" : False,
        "cle" : False,
        "rideau" : False,
        "potion" : False,
        "couloir" : False,
    }
}

perso = base.copy() #crée une copie du dictionnaire base pour que le redémmarage (mort du joueur) soit plus simple

monstres = {
    #Répertorie les caractéristiques de chaque monstre
    "fantome" : {
        "pv" : 5,
        "atq" : 2,
        "exp" : 3,
    },
    "squelette" : {
        "pv" : 20,
        "atq" : 10,
        "exp" : 7,
    },
    "rat" : {
        "pv" : 25,
        "atq" : 15,
        "exp" : 10,
    },
    "gobelins" : {
        "pv" : 33,
        "atq" : 15,
        "exp" : 15,
    },
    "sorcier" : {
        "pv" : 50,
        "atq" : 20,
        "exp" : 50,
    },
    "oeil" : {
        "pv" : 100,
        "atq" : 25,
        "exp" : 100,
    }
}

dialogues = [ # liste de tous les textes possibles

#majordome
("Oh, vous êtes réveillé.",
"Bonjour, je suis le majordome de cette demeure."),
("Enfin... je l'étais avant qu'il prenne le contrôle de ce manoir..",
"Est-ce que je pourrais vous demander un service ?"),
("Je sais qu'il se cache dans ce manoir mais je ne sais pas où,","mais vu votre carrure, je pense que vous serez capable de le vaincre."),
"Je compte sur vous.",
#golem
("Votre laissez passer s'il vous plaît","Oh vous n'en avez pas, je suis désolé je ne peux pas vous laisser passer"),
("Votre laissez passer s'il vous plaît","Très bien, vous pouvez rentrer"),
#rat
("Qui ose me déranger pendant que je cuisine ?","Vous avez affaire à un rat en colère !"),
#gobelins
"Areuh-areuh-areuh !! (On te laissera pas passer !!)",
#maman gobelin
("Comment avez vous pu rentrer ici ? Mes petits montaient la garde..","Attendez, vous n'auriez tout de même pas..."),
"Prenez vous donc ce canard explosif en pleine figure",
#sorcier
"Vous n'auriez pas dû rentrer ici...",
#oeil
("Vous êtes donc venu à bout de tous mes sbires, c'est remarquable","Mais aurez vous la force nécessaire pour me vaincre ?")
]