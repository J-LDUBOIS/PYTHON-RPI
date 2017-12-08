#Déclaration de la classe :
class A():
  def bonjour(self):
    print ("Un petit bonjour de la fonction 'bonjour' de la classe 'A' !")
 
liste=[]
 
for i in range(6):
    liste.append(A())
for e in liste:
    e.bonjour()