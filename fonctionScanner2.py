# -*-coding:Utf-8 -*

#fonction scan des données bluetooth

from bluepy.btle import Scanner
Resultat = []

scan = Scanner()
Resultat = scan.scan(3.0, True)

print (Resultat)


def cmd_list_devices(self, *args):
    try:
        self.last_scan = ScanDelegate()
        scanner = Scanner().withDelegate(self.last_scan)
        print('Listing Bluetooth LE devices in range for 5 minutes.'
              'Press CTRL+C to stop searching.')
        print('{: <5} {: <30} {: <12}'.format('ID', 'Name', 'Mac address'))
        print('{: <5} {: <30} {: <12}'.format('--', '----', '-----------'))
        scanner.scan(350)

     
from bluepy.btle import Scanner
scan = btle.Scanner()
resultat = scan.scan()

result[0].addr