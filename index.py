# -*-coding:Utf-8 -*

#declaration des variables & dictionnaires
from src.donnee import LISTE_ADRESSE_MAC
from src.scanner import fonction_scanner
from src.traitement import test_adresse_mac, comparaison_heure
from src.notification import boucle_notification
from src.controle_parametrage import test_parametre
from datetime import datetime


NOTIFICATION_ACTIVE = False #définition du booleen qui active la boucle infinie

#validation du paramétrage
while NOTIFICATION_ACTIVE is False:
    NOTIFICATION_ACTIVE = test_parametre() #programme d'alerte actif ou inactif

#boucle infini tant que la notification est activée
while NOTIFICATION_ACTIVE is True:
    print(datetime.now())
    RESEAUX_SCANNES = [] #stock les adresses Mac scannees
    try:
        RESEAUX_SCANNES = fonction_scanner(4.0) #scan de X secondes des BLE du périmètre
    except:
        print("error relance scan")
        RESEAUX_SCANNES = fonction_scanner(4.0) #scan de X secondes des BLE du périmètre
    print("scan BLE ok")
    print(RESEAUX_SCANNES)

    RESEAUX_TRAITEMENT = [] #stockage provisoire des adresses Mac à traiter
    RESEAUX_TRAITEMENT = RESEAUX_SCANNES #liberation de la liste de BLE scannes

    if RESEAUX_TRAITEMENT != []: #traitement adresse mac si data du scan
        CAPTEURS_SCANNES = []
        #vérification liste de capteur scannes
        CAPTEURS_SCANNES = test_adresse_mac(RESEAUX_TRAITEMENT, LISTE_ADRESSE_MAC)
        print("adresse mac reconnues ok")
        print(CAPTEURS_SCANNES)

        if CAPTEURS_SCANNES != []: #traitement délai notification si data du traitement adresse mac
            CAPTEURS_NOTIFIES = []
            #vérification latence notification > 60 secondes
            CAPTEURS_NOTIFIES = comparaison_heure(CAPTEURS_SCANNES)
            print("délai notification controle")
            print(CAPTEURS_NOTIFIES)

            if CAPTEURS_NOTIFIES != []: #envoi d'une notification si data du traitement délai notification
                #envoi notification
                boucle_notification(CAPTEURS_NOTIFIES)
                print("emails envoyé")

print(CAPTEURS_NOTIFIES)