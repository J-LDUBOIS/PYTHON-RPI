# -*-coding:Utf-8 -*
"""
Ce module crée les données sur les capteurs qui vont être manipulé par le programme
en fonction des données BLE scannées

"""
from datetime import datetime
import csv


def initialiser_capteur():
    """récupérer email dans fichier parametre_email.csv et retourner une liste"""
    with open("/home/pi/logiciel_RPI/data/capteur_a_creer.csv") as file:
        capteur_a_creer = list(csv.reader(file, delimiter=';'))
    return capteur_a_creer


CAPTEUR_A_CREER = initialiser_capteur()
liste_nom_capteurs = []
liste_adresse_mac = []
liste_code = []

# Creation des listes de nom capteur et des adresses mac
for nom, mac, code in CAPTEUR_A_CREER:
    liste_nom_capteurs.append(nom)
    liste_adresse_mac.append(mac)
    liste_code.append(code)

# creation du dictionnaire adresse mac et notification
liste_notification = {}
for capteurs in liste_adresse_mac:
    liste_notification[capteurs] = datetime.now()


def initialiser_non_capteur():
    """récupérer nom capteur de l'objet associé et retourner une liste"""
    with open("/home/pi/logiciel_RPI/data/parametre_nom_capteur.csv") as file:
        capteur_a_creer = list(csv.reader(file, delimiter=':'))
    return capteur_a_creer


# liste de couple code et nom a associer
LISTE_COUPLE_NOM = initialiser_non_capteur()

# création d'une liste récupérant uniquement les noms à associer
LISTE_NOM_A_ASSOCIER = []
for code, nom in LISTE_COUPLE_NOM:
    LISTE_NOM_A_ASSOCIER.append(nom)

# creation du dictionnaire adresse mac et nom associé
LISTE_NOM_ASSOCIE = {}
for capteurs in liste_code:
    LISTE_NOM_ASSOCIE[liste_adresse_mac[liste_code.index(
        capteurs)]] = LISTE_NOM_A_ASSOCIER[liste_code.index(capteurs)]

# creation du dictionnaire adresse mac et heure notification
LISTE_NOTIFICATION_ASSOCIE = {}
for capteurs in liste_code:
    LISTE_NOTIFICATION_ASSOCIE[liste_adresse_mac[liste_code.index(
        capteurs)]] = datetime(2017, 12, 10, 14, 48)
