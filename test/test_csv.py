# -*-coding:Utf-8 -*
import csv
import donnee2
from donnee import *

def exploiter_nom_capteur():
    """récupérer nom du capteur dans fichier parametre_nom_capteur.csv et retourner une liste (code capteur : nom capteur associé"""
    with open("/home/alexis/Dropbox/Projet_Python/Logiciel_PRI/parametre_nom_capteur.csv") as file:
        parametre_nom_capteur = dict(csv.reader(file, delimiter=':'))
    return parametre_nom_capteur

LISTE_NOM_CAPTEUR = exploiter_nom_capteur()

print(LISTE_NOM_CAPTEUR)

for item in LISTE_NOM_CAPTEUR:
    print(LISTE_NOM_CAPTEUR[item])

"""

for item in LISTE_CAPTEURS:
    item.associer_nom(LISTE_NOM_CAPTEUR[item.code])

for item in LISTE_CAPTEURS:
    print(item.nom)
    """