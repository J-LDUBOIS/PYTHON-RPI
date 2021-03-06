# -*-coding:Utf-8 -*
"""
Ce module contient la fonction qui permet de scanner les réseaux BLE du périmètre

:param duree: Durée du scan en secondes.
:type duree: int
:return: Une liste des objets bluetooth scannés.
:rtype: list
:Exemple: scan(12)

"""

from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    """class sans explication, voir bluepy"""
    def __init__(self):
        DefaultDelegate.__init__(self)

def scan(seconde):
    """fonction qui scanne le reseau bluetooth environnent pendant les secondes paramétrées"""
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(seconde)
    liste_scan = []
    for dev in devices:
        liste_scan.append(dev.addr)
    return liste_scan
