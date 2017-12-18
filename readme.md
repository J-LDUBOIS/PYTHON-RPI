# Logiciel pour Raspberry Pi de suivi de déplacement de capteur en bluetooth

## Versions

Version disponible : 1.0\
Dernière mise à jour : 19/12/2017\
Licence : MIT

## Materiel et versions comptatibles

Raspberry Pi 3 \
Raspbian Stretch Lite - version: November 2017 - Kernel version: 4.9\
Python 3.5\
Bibliothèque Bluepy release 1.1.2

## Presentation

Ce logiciel de détection de flux bluetooth BLE4 a été créer dans le cadre d'un projet au sein du CESI.

A partir d'un paramètrage d'un profil client (nombre et identification de capteur, email à notifié) et d'une connexion wifi, le logiciel installé sur un Raspberry Pi est capable de scanner son environnement BLE, identifié les capteurs de mouvements connus et notifier la personne adéquate en fonction d'un délai prédéfini entre deux notifications.

## MODULES DISPONIBLES

### Index

Logiciel qui comprend la boucle principale. Elle doit durer moins de 5 secondes soit le temps d'émission d'un capteur déplacé. Le logiciel ne faisant pas de multi-thread.

### Module donnée

Ce module contient la classe capteur, son constructeur, 3 méthodes et X fonctions associées

### Module controle parametrage

Permet d'initialiser la boucle infini de scan du bluetooth via la validation :

- de la connexion wifi
- du paramétrage d'un email à notifier
- du paramétrage des noms associés aux capteurs

### Module traitement

Permet de réaliser deux traitement :

- reconnaissance des adresses mac des capteurs enregistrés
- validation d'une latence de 60 secondes entre deux notification

### Module notification

Permet d'effectuer un envoi d'email vers un ou plusieurs destinataires avec les informations détaillés sur le capteur déplacé.

### Stockage de données

- Capteur à créer : liste des capteurs à enregistrer
- Paramètre nom capteur : nom de l'objet associé à chaque capteur
- Paramètre email : email du ou des destinataires des notifications
- Log historique : historique de toutes les notifications