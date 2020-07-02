class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def calcul_aire(self):
        print(f"{self.longueur * self.largeur}m²")
    
    def __enter__(self):
        print(f"L'aire d'un rectangle de {self.longueur}m par {self.largeur}m est de :")
        return self # pour l'application de la méthode dans le context manager
        
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    

with Rectangle(6, 12) as r:
    r.calcul_aire()