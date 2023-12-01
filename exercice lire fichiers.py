notes = []
with open("notes.txt", "r") as filin:

    ligne = filin.readline()
    while ligne != "":
        notes.append(float(ligne))

        print(float(ligne))
        ligne = filin.readline()
    print(notes)

# Calculer la moyenne des éleves

moyenne = 0
nombre_de_notes = len(notes)
if nombre_de_notes > 0:
    somme_notes = sum(notes)
    moyenne = somme_notes / nombre_de_notes 

# Affichage de la moyenne avec deux décimales
moyenne_arrondie = round(moyenne, 2)

print("La moyenne des éleves est de : ", moyenne_arrondie)

# Ecrire notes2.txt et faire un script pour admis et recalé

with open("notes2.txt", "w") as filout:
    for notes_des_eleves in notes:
        if notes_des_eleves >= 10.0:
            notes_des_eleves = str(notes_des_eleves) + " admis"
        else:
            notes_des_eleves = str(notes_des_eleves) + " recalé"
        filout.write(str(f"{notes_des_eleves}\n"))
        print(notes_des_eleves)




