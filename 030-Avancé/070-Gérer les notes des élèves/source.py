class Note:
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return "{} / 20".format(self.valeur)

class Notes(list):
    notes = [] # like to keep track of all the notes of the class but WAS WRONG (should use instance)
    valeur_notes = [note.valeur for note in notes]
    
    def ajouter_note(self, note):
        Notes.notes.append(note)

    def notes_parfaites(self):
        return valeur_notes.count(20)

    def moyenne(self):
        return round(sum(valeur_notes) / len(valeur_notes), 1)


valeur_notes = [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17]
notes = Notes()

for valeur_note in valeur_notes:
    notes.ajouter_note(note=Note(valeur=valeur_note))
    print(Notes.notes)

print(notes.notes_parfaites())
print(notes.moyenne())
