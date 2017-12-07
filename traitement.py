# -*-coding:Utf-8 -*

from datetime import datetime, timedelta
import donnee
"""
def testAdresseMac(AdressesScannees, listeCapteur):
    for mac in AdressesScannees:
        for mac2 in listeCapteur:
            if mac == mac2:
                print ("Réseau {} trouvé".format(donnee.nomCapteur[mac]))
                donnee.capteursScannes.append(mac)
    return donnee.capteursScannes
"""
def test_adresse_aac(AdressesScannees, listeCapteur):
    for mac in AdressesScannees:
            if mac in listeCapteur:
                print "Réseau {} trouvé".format(donnee.nomCapteur[mac])
                donnee.capteursScannes.append(mac)
    return donnee.capteursScannes

def comparaison_heure(capteurValide, dictNotif):
    for mac in capteurValide:
        ecartNotif = datetime.now().replace(microsecond=0) - dictNotif[mac]
        print(ecartNotif)
        if ecartNotif.seconds > 60:
            print ("envoi notification car temps supérieur à 60sec")
            dictNotif[mac] = datetime.now().replace(microsecond=0)
        else:
            print ("pas d'envoi de notification")
    return donnee.dictionnaireNotif
