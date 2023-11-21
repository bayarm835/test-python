greeting = 'Hello'
greeting += ' world!'
greeting
print(greeting)

number = 1
number += 1
number
print(number)

my_list = ['item']
my_list *=3
my_list
print(my_list)

print(my_var:="Hello World!")

my_var="Yes"
print(my_var)

print(my_var:="Hello")

prénom = ['moon', 'hadjer', 'bassam']
for word in prénom :
    print(word, end=' ')
    
print('moon', 'beau', 'gosse', sep=' ')


my_name = input('What is your name? : ')
print('Hi, {}'.format(my_name))

my_name = input('What is your name? : ')
print(f'Hi, {my_name}')


len('hello') #len compte le nombre des lettres dans le cas
len(['cat', 'chien', 15, 'salut']) # ici il compte le nombre d'objets présent

x = 1.2 + 1.4
if x == 2.6 : 
    print("c'est vrai")
else : 
    print("c'est faux")

Nombre_de_personne = int(input('Entrez le nombre de personne : '))
Nombre_de_bonbons = int(input('Entrez votre nombre de bonbons : '))
Nombre_de_bonbons_a_casser = Nombre_de_bonbons% Nombre_de_personne
print('Le nombre de bonbons a casser est de : ', Nombre_de_bonbons_a_casser )

mot_de_passe = 'moon'
demande = input('Quel est le mot de passe : ')
if demande == mot_de_passe :
    print(True)
else : 
    print(False)