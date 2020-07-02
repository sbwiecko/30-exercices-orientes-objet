class Eleve:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    
    def __repr__(self):
        return "{} {}".format(self.prenom, self.nom)


class Classe:
    
    eleves = [] # liste des élèves
    
    @staticmethod
    def ajouter_eleve(prenom, nom):
        Classe.eleves.append(Eleve(prenom, nom))


Classe.ajouter_eleve("John", "Smith")
print(Classe.eleves)