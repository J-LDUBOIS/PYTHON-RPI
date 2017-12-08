# -*-coding:Utf-8 -*

from src.donnee import *

CAPTEUR_A_CREER = initialiser_capteur()

LISTE_NOM_OBJET = []
LISTE_CAPTEURS = []

for nom, mac, code in CAPTEUR_A_CREER:
    LISTE_NOM_OBJET.append(nom)
    LISTE_CAPTEURS.append(Capteur(mac, code))
