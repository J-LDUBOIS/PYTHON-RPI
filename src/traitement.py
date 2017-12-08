# -*-coding:Utf-8 -*

from datetime import datetime, timedelta
import src.donnee

def test_adresse_mac(adresses_scannees, liste_capteur):
    """traitement des adresses mac scannées pour vérifier s'il y a un capteur enregistré"""
    capteurs_scannes = []
    for mac in adresses_scannees:
        if mac in liste_capteur:
            print "Réseau {} trouvé".format("nomCapteur[mac]") # A corriger avec liste
            capteurs_scannes.append(mac)
    return capteurs_scannes

def comparaison_heure(capteur_valide):
    """traitement des capteurs identifié pour contrôler si dernière notification est > 60 sec"""
    for mac in capteur_valide:
        capteur_notifie = []
        ecart_notif = datetime.now().replace(microsecond=0) - mac.notification
        if ecart_notif.seconds > 60:
            print ("envoi notification car temps supérieur à 60sec")
            capteur_notifie.append(mac.mac)
            mac.notification = datetime.now().replace(microsecond=0)
        else:
            print ("pas d'envoi de notification")
    return capteur_notifie
