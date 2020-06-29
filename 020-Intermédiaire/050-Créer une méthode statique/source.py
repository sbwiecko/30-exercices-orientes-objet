class Chanson:
    paroles = """Joyeux anniversaire,
Joyeux anniversaire,
Joyeux anniversaire {prenom},
Joyeux anniversaire."""

    @classmethod
    def chante_pour(cls, prenom):
        return cls.paroles.format(prenom=prenom)


print(Chanson.chante_pour(prenom="Paul"))