# Ex 1 class vehicule
class Vehicule:
    couleur = "blue"
    def __init__(self,max_speed=0,kilometrage=0,nbP=0):
        self.max_speed = max_speed
        self.kilometrage = kilometrage
        self.nbP = nbP
    def __str__(self):
        return f"c'est Vehicule top speed est {self.max_speed} kilometrage {self.kilometrage} nombre deplace est {self.afficher_nbr_place()} "
    def afficher_nbr_place(self):
        return self.nbP
    # surcharge de ==
    def __eq__(self,a):
        return self.max_speed == a.max_speed and self.kilometrage == a.kilometrage and self.nbP == a.nbP
    # surcharge de !=
    def __ne__(self,other):
        return self.max_speed != other.max_speed and self.kilometrage != other.kilometrage and self.nbP != other.nbP
    # surcharge de <
    def __it__(self,other):
        return self.nbP < other.nbP
    # surcharge de >
    def __gt__(self,other):
        return self.nbP > other.nbP
#  Ex 2 class enfant Bus
class Bus(Vehicule):
    def __init__(self,max_speed=0,kilometrage=0,nbP=50):
        super().__init__(max_speed, kilometrage,nbP)
    def __str__(self):
        return f"c'est Bus top speed est {self.max_speed} kilometrage {self.kilometrage} nombre deplace est {self.afficher_nbr_place()} "


test = Bus(293,83)

test2= Vehicule(22,12,19)

print(test2)
print(test)