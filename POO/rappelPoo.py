class Perssone :
    def __init__ (self, n, p, a, c) :
        self.nom = n
        self.prenom = p
        self.age = a 
        self.__cine = c
    def __str__ (self) :
        return f"Nom : {self.nom} {self.prenom} age : {self.age}"
    def get_cine(self) :
        return self.__cine
    def set_cine(self,x) :
        self.__cine = x
    def del_cine(self):
        del self.__cine

    cine = property(get_cine,set_cine,del_cine)
    


firstPerssone = Perssone("mazoug","khalid","24","EA223262")
print(firstPerssone)
print(firstPerssone.get_cine())
print(cine.get_cine)