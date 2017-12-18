# -*-coding:Utf-8 -*

""" Verifie les parametres email et envoie un mail pour chaque adresse mac trouvé"""

import smtplib
from data import DATA_DIR
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.controle_parametrage import PARAMETRE_EMAIL
from src.donnee import LISTE_NOM_ASSOCIE, LISTE_NOTIFICATION_ASSOCIE
from datetime import date

# parametre de l'email
def exploiter_email(liste_email):
    """ Permet de creer une liste des destinataires global."""
    liste_email_utilisable = []
    for item in liste_email:
        for item2 in item:
            liste_email_utilisable.append(item2)
    return liste_email_utilisable


DESTINATAIRE_GLOBAL = exploiter_email(PARAMETRE_EMAIL)
DESTINATAIRE_PRINCIPAL = DESTINATAIRE_GLOBAL[0]
DESTINATAIRE_SECONDAIRE = ','.join(map(str, DESTINATAIRE_GLOBAL[1:]))


def envoi_email(mac):
    """Permet de notifier les adresses mails du .csv"""
    fromaddr = "projetrpi2017@gmail.com"
    mdpfroaddr = "Cesi2017"
    toaddr = DESTINATAIRE_PRINCIPAL
    cc = DESTINATAIRE_SECONDAIRE
    bcc = ""

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['to'] = toaddr
    msg['Subject'] = "Alarme détecteur : {}".format(LISTE_NOM_ASSOCIE[mac])

    body = "Votre détecteur associé à l'objet : {} a été déplacé à : {}\n".format(
        LISTE_NOM_ASSOCIE[mac], LISTE_NOTIFICATION_ASSOCIE[mac].strftime("%d %B %Y à %H:%M"))
    msg.attach(MIMEText(body, 'plain'))

    rcpt = [toaddr] + cc.split(",") + bcc.split(",")
    print(rcpt)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, mdpfroaddr)
    text = msg.as_string()
    server.sendmail(fromaddr, rcpt, text)
    server.quit()

    print(DATA_DIR)
    today = date.today().strftime("%d-%B-%Y")
    with open(DATA_DIR + "/Historique_des_logs/historique{}.csv".format(today), "a") as file:
        file.write(body)
    print(body)

def boucle_notification(capteur_notifie):
    """Envoie un email pour chaque adresse mac """
    for mac in capteur_notifie:
        envoi_email(mac)
        print("email envoyé {}".format(mac))
