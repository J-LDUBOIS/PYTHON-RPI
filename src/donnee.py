# -*-coding:Utf-8 -*
"""Ce module crée les données sur les capteurs qui vont être manipulé par le programme
    en fonction des données BLE scannées"""

from datetime import datetime
import csv

def initialiser_capteur():
    """récupérer email dans fichier parametre_email.csv et retourner une liste"""
    with open("/home/pi/Logiciel_RPI/data/capteur_a_creer.csv") as file:
        capteur_a_creer = list(csv.reader(file, delimiter=';'))
    return capteur_a_creer

CAPTEUR_A_CREER = initialiser_capteur()

LISTE_NOM_CAPTEURS = []
LISTE_ADRESSE_MAC = []
LISTE_CODE = []

#Creation des listes de nom capteur et des adresses mac
for nom, mac, code in CAPTEUR_A_CREER:
    LISTE_NOM_CAPTEURS.append(nom)
    LISTE_ADRESSE_MAC.append(mac)
    LISTE_CODE.append(code)

#creation du dictionnaire adresse mac et notification
LISTE_NOTIFICATION = {}
for capteurs in LISTE_ADRESSE_MAC:
    LISTE_NOTIFICATION[capteurs] = datetime.now()

def initialiser_non_capteur():
    """récupérer nom capteur de l'objet associé et retourner une liste"""
    with open("/home/pi/Logiciel_RPI/data/parametre_nom_capteur.csv") as file:
        capteur_a_creer = list(csv.reader(file, delimiter=':'))
    return capteur_a_creer

LISTE_COUPLE_NOM = initialiser_non_capteur() #liste de couple code et nom a associer

 #création d'une liste récupérant uniquement les noms à associer
LISTE_NOM_A_ASSOCIER = []
for code, nom in LISTE_COUPLE_NOM:
    LISTE_NOM_A_ASSOCIER.append(nom)

#creation du dictionnaire adresse mac et nom associé
LISTE_NOM_ASSOCIE = {}
for capteurs in LISTE_CODE:
    LISTE_NOM_ASSOCIE[LISTE_ADRESSE_MAC[LISTE_CODE.index(capteurs)]] = LISTE_NOM_A_ASSOCIER[LISTE_CODE.index(capteurs)]

#creation du dictionnaire adresse mac et heure notification
LISTE_NOTIFICATION_ASSOCIE = {}
for capteurs in LISTE_CODE:
    LISTE_NOTIFICATION_ASSOCIE[LISTE_ADRESSE_MAC[LISTE_CODE.index(capteurs)]] = datetime(2017, 12, 10, 14, 48)
