# -*-coding:Utf-8 -*
""" Monte puis copie les fichiers puis demonte la clé"""
import os
from time import sleep


def auto_mount():
    """ La fonction essaie de monter une clé usb durant 1 minute, ou jusqu'a
    quelle y arrive.

    Puis elle copie
    les fichiers de conf de la clé dans son repertoire de travail.
    la copie supprime les anciens fichiers si ils existent.
    si il ny a pas de fichiers ou pas de clé usb, les fichiers de conf
    précédents sont utilisés.
    Si ils ne sont pas présents le programme sarretera. Puis se relancera
    """
    error_mount = 8192  # erreur renvoyée si il n'y a pas de clé usb
    compteur = 0
    # on essaye de monter une clé usb pendant une minute
    while (error_mount == 8192) and (compteur < 10):
         # commande pour monter
        error_mount = os.system("sudo mount /dev/sda1 /mnt/Disk-usb")
        sleep(1)
        if error_mount == 8192:
            sleep(5)
            compteur += 1

    # copie des fichiers de conf
    os.system("cp -f /mnt/Disk-usb/capteur_a_creer.csv /home/pi/logiciel_RPI/data/capteur_a_creer.csv")
    os.system("cp -f /mnt/Disk-usb/parametre_email.csv /home/pi/logiciel_RPI/data/parametre_email.csv")
    os.system("cp -f /mnt/Disk-usb/parametre_nom_capteur.csv /home/pi/logiciel_RPI/data/parametre_nom_capteur.csv")
    
    with open("/mnt/Disk-usb/wpa_supplicant.conf")as file:
        wpa_supplicant_cle = file.read()
        print(wpa_supplicant_cle)
    with open("/etc/wpa_supplicant/wpa_supplicant.conf")as file:
        wpa_supplicant_rpi = file.read()
        print ("wpa_supplicant_rpi")

    if wpa_supplicant_cle != wpa_supplicant_rpi:
        os.system("sudo cp -f /mnt/Disk-usb/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf")
        os.system("sudo reboot")
        sleep(1)
    # on demonte
    os.system("sudo umount /mnt/Disk-usb")
