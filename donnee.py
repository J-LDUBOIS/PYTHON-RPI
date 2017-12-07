# -*-coding:Utf-8 -*


from datetime import datetime, timedelta

#déclaration des adresses Mac
macCapteur1 = "7b:2c:fd:3d:24:a4"
macCapteur2 = "49:b3:1e:96:ea:97"
macCapteur3 = "62:97:b0:b1:e8:fa"
macCapteur4 = "53:56:7e:14:e1:96"
macCapteur5 = "66:a8:e3:8a:81:44"
macCapteur6 = "55:c6:67:7c:87:46"


capteursEnregistres = [macCapteur1,macCapteur2, macCapteur3, macCapteur4, macCapteur5, macCapteur6] #stock les adresses Mac connues


##dictionnaire des adresses capteurs et leur noms d'objet associé
nomCapteur = {\
macCapteur1 : "capteur 1",\
macCapteur2 : "capteur 2",\
macCapteur3 : "capteur 3",\
macCapteur4 : "capteur 4",\
macCapteur5 : "capteur 5",\
macCapteur6 : "capteur 6"}

#dictionnaire des heures de notification
"""dictionnaireNotif = {
    macCapteur1: datetime(2017,1,1, 0,0,0),\
    macCapteur2: datetime(2017,1,1, 0,0,0),\
    macCapteur3: datetime(2017,1,1, 0,0,0),\
    macCapteur4: datetime(2017,1,1, 0,0,0),\
    macCapteur5: datetime(2017,1,1, 0,0,0),\
    macCapteur6: datetime(2017,1,1, 0,0,0)} 
"""
dictionnaireNotif = {}