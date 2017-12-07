# -*-coding:Utf-8 -*
"""Ce module contient la fonction qui permet de scanner les réseaux BLE du périmètre"""
from bluepy.btle import Scanner, DefaultDelegate

def fonction_scanner():
    """cette fonction scan les réseaux bluetooth à proximité et renvoie une liste d'adresse mac"""
    class ScanDelegate(DefaultDelegate):
        """ """
        def __init__(self):
            DefaultDelegate.__init__(self)
 
        def handleDiscovery(self, dev, isNewDev, isNewData):
            scanBle = []
            scanBle.append(dev.addr)
            print ("%s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
            return scanBle

    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(3.0)
    
fonction_scanner()
