# -*-coding:Utf-8 -*
"""Contrôle que les paramètres minimum pour lancer le programme
on teste :
la connexion wifi via un ping
le paramétrage des adresses emails pour l'envoi des notifications
le paramétrage des noms associés aux capteurs"""
import csv
from src.donnee import LISTE_NOM_A_ASSOCIER

def test_ping():
    """tester le ping de google pour vérifier la connexion au wifi"""
    import os
    hostname = "8.8.8.8"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = True
    else:
        pingstatus = False
    return pingstatus

def extraire_email():
    """récupérer email dans fichier parametre_email.csv et retourner une liste"""
    with open("/home/pi/Logiciel_RPI/data/parametre_email.csv") as file:
        parametre_email = list(csv.reader(file, delimiter=';'))
    return parametre_email

def test_adresse_email(parametre_email):
    """vérifier qu'une adresse email au moins est dans les destinataires"""
    if parametre_email is not "":
        return True
    return False

def test_un_nom_capteur(liste_non_associe):
    """vérifier qu'un capteur au moins à un nom attribué"""
    if liste_non_associe is not "":
        return True
    return False

#creation des variables de controle
PING_TEST = test_ping()
PARAMETRE_EMAIL = extraire_email()
ADRESSE_EMAIL = test_adresse_email(PARAMETRE_EMAIL)
UN_NOM_CAPTEUR = test_un_nom_capteur(LISTE_NOM_A_ASSOCIER)

def test_parametre():
    """ la fonction test la connexion wifi, les emails destinataires et le paramétrage des noms"""
    if (PING_TEST is True) & (ADRESSE_EMAIL is not "") & (UN_NOM_CAPTEUR is True):
        return True
    return False
