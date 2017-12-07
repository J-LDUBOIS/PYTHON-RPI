# -*-coding:Utf-8 -*
"""Contrôle que les paramètres minimum pour lancer le programme
on teste :
la connexion wifi via un ping
le paramétrage des adresses emails pour l'envoi des notifications
le paramétrage des noms associés aux capteurs"""

def test_parametre():
    """ la fonction test la connexion wifi, les emails destinataires et le paramétrage des noms"""
    notif_value = True #définition de la valeur à retourner
    if (ping is True) & (adresse_email is not "") & (at_least_one_capteur.nom is not ""):
        notif_value is True
    return notif_value

