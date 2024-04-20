# reviser cours 19/04/2024
class Voiture():
    def __init__(self,marque="",model="",puissanceFiscale=0,matricul="",propriétaire=""):
        self.marque=marque
        self.model=model
        self.puissanceFiscale=puissanceFiscale
        self.__matricul=matricul
        self.propriétaire=propriétaire
    def __str__(self):
        infoVoiture=f"cette voiture pour {self.propriétaire} est de le marque {self.marque} modele{self.model} ca puissance Fiscale :{self.puissanceFiscale} matriculation {self.__matricul}  "
        return infoVoiture
    def get_matricule(self):
        return self.__matricul
    def set_matricul(self,x):
        self.__matricul = x
    def del_matricul(self):
        del self.__matricul
    matriculation = property(get_matricule,set_matricul,del_matricul,"this is the documetation")
if __name__=='__main__':
    Voiture1 = Voiture("bmw","525",13,1656,"sidqui")
    print(Voiture1)
    print(Voiture1.get_matricule())
    print(Voiture1.matriculation)
    # print(Voiture1.matriculation)
    # print(f'test{Voiture1.propriétaire} alah{Voiture1.get_matricule()}')
    print(Voiture.matriculation.__doc__)

