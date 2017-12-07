# -*-coding:Utf-8 -*
import donnee
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#parametre de l'email 
def envoiEmail(adresseMac):
    fromaddr = "email"
    mdpfroaddr = "mdp"
    toaddr = "alexi.bdn@gmail.com"
    cc = "copie"
    bcc = "copie caché"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['to'] = toaddr
    msg['Subject'] = "Alarme détecteur n°{}".format(nonCapteur[adresseMac])
    
    body = "Votre détecteur n° {} à été déplacé. Il s'agit de l'objet : {}. Il a été déplacé à : {}".format(adresseMac,\
     nonCapteur[adresseMac], dictionnaireNotif[adresseMac])
    msg.attach(MIMEText(body, 'plain'))

    rcpt = cc.split(",") + bcc.split(",") + [toaddr]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, mdpfroaddr)
    text = msg.as_string()
    server.sendmail(fromaddr, rcpt, text)
    server.quit()


def boucleNotification(listeCapteur):
    for mac in listeCapteur:
        envoiEmail(listeCapteur[mac])