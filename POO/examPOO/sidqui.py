# Exercice 1
import datetime
class Artiste:
    # Exercice 5 
    pays = "USA"
# exercice 10
    list_Artiste = []
    def __init__(self,nom="",age=0,actif=False,anneeDebut=0,domain="",realisation=[],adresse=""):
        Artiste.list_Artiste.append(self)
        self.nom=nom
        self.age=age
        self.actif=actif
        self.anneeDebut = anneeDebut
        self.domain = domain
        self.realisation = realisation
        self._age = age
        self._adresse = adresse
    # Exercice 9
    def __str__(self):
        return f"c'est {self.nom} mon age est {self.age} mon domain est {self.domain} de pays {Artiste.pays}"
# Exercice 3 
    # get and set for Age
    def getAge(self):
        return self._age
    def setAge(self,a):
        self._age = a

    # get and set for Adresse    
    def getAdresse(self):
        return self._adresse
    def setAdresse(self,b):
        self._adresse = b    
#  
# Exercice 4
    adresse = property(getAdresse,setAdresse)
# Exercice 6 
    def ajouter_realisation(self,n):
        self.realisation.append(n)
# Exercice 7
    def anciennete(self):
        d = datetime.date.today().year - self.anneeDebut
        return d
# Exercice 8
    @classmethod
    def modifier_pays(cls,a):
            cls.pays = a
# exercice 11 
    @staticmethod
    def rechercher_par_nom(aa):
        l = []
        for artiste in Artiste.list_Artiste:
            if artiste.nom == aa:
                print(artiste)
                l.append(artiste)
        return l

# exercice 12
class Musicien(Artiste):
# exercice 13
    nb_concerts = 0
    def __init__(self, nom="", age=0, actif=False, anneeDebut=0, domain="", realisation=[], adresse="",instruments=[]):
        super().__init__(nom, age, actif, anneeDebut, domain, realisation, adresse)
        self.instruments = instruments
        Musicien.nb_concerts+=1
# exercice 14
    def __str__(self):
        return super().__str__() +" "+ f"les instrumant que je maitrise{self.instruments} le nombre de concerts est {Musicien.nb_concerts}"
    


if __name__=='__main__':
    # Exercice 2
    artiste1 = Artiste("Denzel washington",69,False,1980,"Cinema",realisation=["Training Day"])
    artiste2 = Artiste("Cindy sherman",70,False,2004,"Photographie",realisation=["Film Stills"])
    artiste3 = Artiste("Cindy sherman",10,False,2005,"Photographie",realisation=["Film Stills"])
    musicien1 = Musicien("sidqui zakria",23,False,2020,"Musicien",realisation=["bakhta"],instruments=["guitar","piano"])
    musicien2 = Musicien("marzoug khalid",24,False,2022,"Musicien",realisation=["bakhta"],instruments=["baterie","violant"])
    print(Artiste.rechercher_par_nom("Cindy sherman"))
    print(artiste1.realisation)
    artiste1.ajouter_realisation("dark")
    print(artiste1.realisation)
