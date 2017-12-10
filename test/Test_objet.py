# -*-coding:Utf-8 -*
"""Ce module crée les objets Capteurs qui vont être manipulé par le programme
    en fonction des données BLE scannées"""

from datetime import datetime
import csv

class Capteur(object):
    """classe définissant les capteurs et leur propriétés.
        Elle prend en valeur d'entrée l'adresse mac et le code d'identification visuel.
        Le client via le formulaire attribue un nom à chacun d'eux."""
    def __init__(self, mac, code):
        self.mac = mac
        self.code = code
        self.nom = ""
        self.notification = datetime.now()
        self.nbre_alerte = 0

    def creation_dynamique(self, mac, code):
        """fonction de creation d'objet dynamique"""
        self.mac = mac
        self.code = code

    def associer_nom(self, nom):
        """fonction pour associer un nom manuellement à un capteur déjà existant"""
        self.nom = nom

    def changer_temps_notification(self, temps_notif):
        """fonction pour que le programme sauvegarde le temps de la dernière notification"""
        self.notification = temps_notif

    def compter_alerte(self, alerte):
        """fonction pour que le programme sauvegarde le nombre de notification par capteur"""
        self.nbre_alerte = alerte

def initialiser_capteur():
    """récupérer email dans fichier parametre_email.csv et retourner une liste"""
    with open("/home/alexis/Dropbox/Projet_Python/Logiciel_PRI/capteur_a_creer.csv") as file:
        capteur_a_creer = list(csv.reader(file, delimiter=';'))
    return capteur_a_creer

CAPTEUR_A_CREER = initialiser_capteur()

LISTE_NOM_CAPTEURS = []
LISTE_ADRESSE_MAC = []

for nom, mac, code in CAPTEUR_A_CREER:
    LISTE_NOM_CAPTEURS.append(nom)
    LISTE_ADRESSE_MAC.append(nom)

#exemple d'instantiation dynamique
#Déclaration de la classe :
class A():
  def bonjour(self):
    print ("Un petit bonjour de la fonction 'bonjour' de la classe 'A' !")
 
liste=[]
 
for i in range(6):
    liste.append(A())
for e in liste:
    e.bonjour()