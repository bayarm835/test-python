coordonnees = [
    0.50000, 0.00000, 
    0.59700, 0.05990,
    0.68605, 0.13907,
    0.76427, 0.23642, 
    0.82895, 0.35048, 
    0.87758, 0.47943
]

chemin_fichier_dat = "C:/Users/moon/spirale.dat"

with open(chemin_fichier_dat, "w") as fichier_dat:
    for i in range(0, len(coordonnees), 2):
        coordonnee1 = round(coordonnees[i], 5)
        coordonnee2 = round(coordonnees[i + 1], 5)
        fichier_dat.write(f"{coordonnee1:.5f} {coordonnee2:.5f}\n")

print(f"Fichier {chemin_fichier_dat} créé avec succès.")

import matplotlib.pyplot as plt

x = []
y = []
with open("spirale.dat", "r") as f_in:
    for line in f_in:
        coordonnee = line.split()
        x.append(float(coordonnee[0]))
        y.append(float(coordonnee[1]))

plt.figure(figsize=(8,8))
mini = min(x+y) * 1.2
maxi = max(x+y) * 1.2
plt.xlim(mini, maxi)
plt.ylim(mini, maxi)
plt.plot(x, y)
plt.savefig("spirale.png")

