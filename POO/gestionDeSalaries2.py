import math
class Salarie:
    cmptS = 0
    departement = "IT"
    tauxCs = 0.23
    def __init__(self,nom="",prenom="",salaire=0):
        Salarie.cmptS+=1
        self.__matricul =Salarie.cmptS
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
    def __str__(self):
        return f'salaire n°: {self.__matricul} nom :{self.nom} prenom {self.prenom} salaire {self.salaire}'
    def __calculerSalaireNet(self):
       t =  self.salaire-(self.salaire * Salarie.tauxCs)
       return t
    def  __del__(self):
        Salarie.cmptS-=1
    @classmethod
    def afficherNbrSalarie(cls):
        return f'nombre de salarie est {cls.cmptS}'
    def afficher_salair_net(self):
        return self.__calculerSalaireNet()
    @staticmethod
    def compareSalaire(s1,s2):
        d = max(s1.salaire,s2.salaire)
        return f'le salaire le plus grand est {d}'
class Manager(Salarie):
    def __init__(self,nom="",prenom="",salaire=0,equipe=[]):
        self.equipe=equipe    
        super().__init__(nom,prenom,salaire)
    def ajout_salarie(self,a):
        self.equipe.append(a.nom)
class ChefProjet:
    def __init__(self,projet):
        self.projet = projet
class Gestionnaire(Salarie,ChefProjet):
    def __str__(self):
        return f"c'est {self.prenom} de salaire {self.salaire}"
    def __init__(self, nom="", prenom="", salaire=0,projet=""):
        super().__init__(nom, prenom, salaire)
        ChefProjet.__init__(self,projet)


if __name__=='__main__':
    salarie1 = Salarie("sidqui","zakaria",2000)
    salarie2 = Salarie("marzoug","khalid",2500)
    salarie3 = Salarie("mahfoud","anas",2000)
    print(Salarie.cmptS)
    manager1 = Manager("marzoug","khalid",30000,["ana","lakhur","ou sahbo"])
    # print(salarie1)
    # print(salarie2)
    # print(salarie3)
    # print(Salarie.afficherNbrSalarie())
    # print(salarie3.afficher_salaire_net()) 
    print(salarie1.afficher_salair_net())
    print(Salarie.compareSalaire(salarie1,salarie2))
    print(Salarie.cmptS)
    manager1.ajout_salarie(salarie3)
    print(manager1.equipe)
    gestionnaire1 = Gestionnaire("anas","mahfod",40000,"it")
    print(gestionnaire1)