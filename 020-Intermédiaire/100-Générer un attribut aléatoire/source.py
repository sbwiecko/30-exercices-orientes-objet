import random

class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance
        self.virements = {}
    
    def virement(self, montant):
        self.balance += montant
        identifiant = '' # initialisation de l'identifiant unique
        for char in range(15):
            identifiant += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        self.virements[identifiant] = montant


john = Compte(nom="John Smith", numero="123456", balance=20000)
john.virement(montant=5000)
print(john.virements)