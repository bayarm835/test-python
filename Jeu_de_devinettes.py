def main():
    print("Bonjour, et bienvenue dans le jeu de la dichotomie !")
    userName = input("Entrez un nom d'utilisateur : ")
    print("Bonjour", userName, ", votre nom d'utilisateur est validé")

    minValue = int(input('Entrez le nombre minimum : '))
    maxValue = int(input('ENtrez le nombre maximum : '))

    print(userName, ", pensez à un nombre entre", minValue, "et", maxValue)

    jeu_lance = True

    nombre_de_tentative = 0

    while jeu_lance:
        
        milieu = (minValue + maxValue) // 2

        question = input(f"Est-ce que votre nombre est supérieur (+), égal (=), ou inférieur (-) à {milieu}? ")

        if question == '+':
            minValue = milieu + 1
            nombre_de_tentative += 1
        elif question == '-':
            maxValue = milieu - 1
            nombre_de_tentative += 1
        elif question == '=':
            jeu_lance = False
            print(milieu, " est votre nombre")
            print("Votre nombre été trouvé au bout de ", nombre_de_tentative, " tentative")
        else:
            print("Réponse invalide. Veuillez répondre avec '+', '=', ou '-'.")
            continue

        if minValue > maxValue:
            print("Erreur: Les valeurs de minimum et maximum se sont croisées.")
            jeu_lance = False

    print("Le jeu est terminé.")
    
main()





            


    


    

    