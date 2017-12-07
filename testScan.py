# -*-coding:Utf-8 -*
"""Ce module contient la fonction qui permet de scanner les réseaux BLE du périmètre"""
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print (dev.addr)
        elif isNewData:
            print (dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
