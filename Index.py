# -*-coding:Utf-8 -*

#declaration des variables & dictionnaires
import donnee
from scanner import fonction_scanner
from traitement import test_adresse_mac, comparaison_heure
from notification import boucle_notification
from controle_parametrage import test_parametre

NOTIFICATION_ACTIVE = False #définition du booleen qui 

#validation du paramétrage
while NOTIFICATION_ACTIVE is False:
    NOTIFICATION_ACTIVE = test_parametre() #programme d'alerte actif ou inactif

#boucle infini tant que la notification est activée
while NOTIFICATION_ACTIVE is True:
    RESEAUX_SCANNEES = [] #stock les adresses Mac scannees
    RESEAUX_SCANNEES = fonction_scanner(5) #scan de 5 secondes des BLE du périmètre

    RESEAUX_TRAITETEMENT = [] #stockage provisoire des adresses Mac à traiter
    RESEAUX_TRAITETEMENT = RESEAUX_SCANNEES #liberation de la liste de BLE scannes

    if RESEAUX_TRAITETEMENT != "": #traitement adresse mac si data du scan
        CAPTEURS_SCANNES = []
        #vérification liste de capteur scannes
        CAPTEURS_SCANNES = test_adresse_mac(RESEAUX_TRAITETEMENT, capteur.mac)

        if CAPTEURS_SCANNES != "": #traitement délai notification si data du traitement adresse mac
            CAPTEURS_NOTIFIES = []
            #vérification latence notification > 60 secondes
            CAPTEURS_NOTIFIES = comparaison_heure(CAPTEURS_SCANNES, donnee.dictionnaireNotif)

            if CAPTEURS_NOTIFIES != "": #envoi d'une notification si data du traitement délai notification
                #envoi notification
                boucle_notification(CAPTEURS_NOTIFIES)
    RESEAUX_TRAITETEMENT = []
