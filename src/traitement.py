# -*-coding:Utf-8 -*

from datetime import datetime, timedelta
from src.donnee import *

def test_adresse_mac(adresses_mac, liste_capteur):
    """traitement des adresses mac scannées pour vérifier s'il y a un capteur enregistré"""
    capteurs_scannes = []
    for mac2 in adresses_mac:
        if mac2 in liste_capteur:
            print ("Réseau {} trouvé".format(LISTE_NOM_ASSOCIE[mac2]))
            capteurs_scannes.append(mac2)
    return capteurs_scannes

def comparaison_heure(capteur_valide):
    """traitement des capteurs identifié pour contrôler si dernière notification est > 60 sec"""
    for amac in capteur_valide:
        capteur_notifie = []
        ecart_notif = datetime.now().replace(microsecond=0) - LISTE_NOTIFICATION_ASSOCIE[amac]
        if ecart_notif.seconds > 60:
            capteur_notifie.append(amac)
            LISTE_NOTIFICATION_ASSOCIE[amac] = datetime.now().replace(microsecond=0)
    return capteur_notifie
