etudiants_partis = []


class Etudiant:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def __del__(self): # action appelée (en sus!) à la suppression de l'instance
        etudiants_partis.append("{0} {1}".format(self.prenom, self.nom))

john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")

del marc
print(etudiants_partis)