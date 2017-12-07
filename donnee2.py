# -*-coding:Utf-8 -*
"""Ce module crée les objets Capteurs qui vont être manipulé par le programme 
    en fonction des données BLE scannées"""

from datetime import datetime

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

    def associer_nom(self, nom):
        """fonction pour associer un nom manuellement à un capteur déjà existant"""
        self.nom = nom

    def associer_liste_nom(self, liste_noms):
        """associer automatiquement l'ensemble des noms d'une liste aux capteurs"""
        i = 0
        for capteur in liste_noms:
            capteur.associer_nom(liste_noms[i])
            i += 1

    def changer_temps_notification(self, temps_notif):
        """fonction pour que le programme sauvegarde le temps de la dernière notification"""
        self.notification = temps_notif

    def compter_alerte(self, alerte):
        """fonction pour que le programme sauvegarde le nombre de notification par capteur"""
        self.nbre_alerte = alerte


#déclaration des objets
capteur1 = Capteur("7b:2c:fd:3d:24:a4", "code 1")
capteur2 = Capteur("49:b3:1e:96:ea:97", "code 2")
capteur3 = Capteur("62:97:b0:b1:e8:fa", "code 2")
capteur4 = Capteur("53:56:7e:14:e1:96", "code 2")
capteur5 = Capteur("66:a8:e3:8a:81:44", "code 2")
capteur6 = Capteur("55:c6:67:7c:87:46", "code 2")

liste_capteurs = ["capteur1", "capteur2", "capteur3", "capteur4", "capteur5", "capteur6"]
liste_nom = ["nom 1", "nom 2", "nom 3", "nom 4", "nom 5", "nom 6"]


def testUnitaire(listeCapteur)
for capteurs in liste_capteurs:
    print("{} = {} ".format(capteurs.mac, capteurs.nom))

#fichier de nom à importer par cle USB
dictionnaire_nom = {"code 1" : "nom 1", "code 2": "nom 2", "code 3": "nom 3",\
 "code 4" : "nom 4", "code 5" : "nom 5", "code 6" : "nom 6"}