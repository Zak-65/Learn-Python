import gestionDeSalaire

class Manager(gestionDeSalaire.Salaire):
    def __init__(self,nom,prenom,equipe):
        gestionDeSalaire.Salaire.__init__(self,nom,prenom)
        self.equipe=equipe

# if __name__=='__main__':
#     s=Manager("sidqui","zakaria","tt")
#     print(s)    
print(Manager.departement)