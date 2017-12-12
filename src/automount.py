import os
from time import sleep

def auto_mount():

#La fonction essaie de monter une clé usb durant 1 minute, ou jusqu'a 
#quelle y arrive. Puis elle copie
#les fichiers de conf de la clé dans son repertoire de travail.
#la copie supprime les anciens fichiers si ils existent.
#si il ny a pas de fichiers ou pas de clé usb, les fichiers de conf 
#précédents sont utilisés.
#Si ils ne sont pas présents le programme sarretera. Puis se relancera


     error_mount = 8192 # erreur renvoyée si il n'y a pas de clé usb
     compteur = 0
     while (error_mount == 8192) and (compteur < 10): #on essaye de 
#monter une clé usb pendant une minute
         error_mount = os.system("sudo mount /dev/sda1 /mnt/Disk-usb") 
#commande pour monter
         sleep(1)
         if error_mount == 8192:
             sleep(5)
             compteur+=1

     #copie des fichiers de conf

     os.system("cp -f /mnt/Disk-usb/capteur_a_creer.csv /home/pi/logiciel_RPI/data/capteur_a_creer.csv")
     os.system("cp -f /mnt/Disk-usb/parametre_email.csv /home/pi/logiciel_RPI/data/parametre_email.csv")
     os.system("cp -f /mnt/Disk-usb/parametre_nom_capteur.csv /home/pi/logiciel_RPI/data/parametre_nom_capteur.csv")
     sleep(1)


     os.system("sudo umount /mnt/Disk-usb") #on demonte
