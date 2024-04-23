# declaration de class
class Salaire:
    cmpt = 0
    tauxCS = 0.20
    departement="IT"
    def __init__(self,matricule="11",nom="sidqui",prenom="zakaria",salaire=float(1000)):
        Salaire.cmpt += 1
        self.__matricule =matricule
        self.nom=nom
        self.prenom=prenom
        self.__salaire=salaire
        self.tauxCS
        self.num = Salaire.cmpt
    def __str__(self):
        resultSalaire = f'bonjour {self.nom} {self.prenom} de matricule : {self.__matricule} votre salaire est : {self.__salaire} salaire Net est :{self.CalculerSalaireNet()} departement : {self.departement} n°:{self.num}'
        return resultSalaire 
    def CalculerSalaireNet(self):
        SalaireNet = self.__salaire-(self.__salaire*self.tauxCS)
        return SalaireNet
    def get_salaire(self):
        self.__test()
        return self.__salaire
    def set_salaire(self,x):
        self.__salaire = x
    def del_salaire(self):
        del self.__salaire
    def afficher_doc(self):
        return "this is doc"
    def __test(self):
        print("test work")
    def __del__(self):
        Salaire.cmpt-= 1
        print(f'objet supprimer nmbr rester  de cmpt : {Salaire.cmpt}')
    # 2 methode pour property
    @property
    def matricule(self):
        return self.__matricule
    
    @matricule.setter
    def matricule(self,z):
        self.__matricule=z   
    # matriculation = property(get_matricul)
    # autre methode
if __name__=='__main__':
    Salaire1=Salaire(1265,"sidqui","zakaria",3800)
    Salaire2=Salaire(1266,"marzoug","khalid",9800)
    Salaire3=Salaire(1260,"marzoug","khalid",9800)     
    print(Salaire1)
    print(Salaire2)
    print(Salaire3)
    print(Salaire1.matricule)
    # Salaire1.matricule=2222
    # print(Salaire1.matricule)
    print(Salaire.cmpt)
    print(Salaire1)





         
