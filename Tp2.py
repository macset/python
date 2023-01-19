# TD2 exo 1
x = int(input("entrez x :"))
y = int(input("Entrez y :"))

print("avant permutation :")
print("x = ", x)
print("y = ", y)

z = x
x = y
y = z
print("après permutation :")
print("x =", x)
print("y =", y)

# ---------------------------------------------------------------
# Exo 2

age = int(input("Donner votre age :"))

annee = 2022-age

print("Votre annee de naissance est :", annee)

# ---------------------------------------------------------------------------------
# Exo 3

a = input("Entrez la premiere  valeur : ")
b = input("Entrez la deuxieme  valeur : ")
c = input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
"""      *******************************************
         * Completez le programme a partir d'ici.
         *******************************************
"""
temp = a
temp1 = b
temp2 = c
b = temp
a = temp2
c = temp1





"""     *******************************************
         * Ne rien modifier apres cette ligne.
         *******************************************
"""

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)

# ----------------------------------------------------------------------------------------------
# Exo 4

BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Veuillez rentrer le nombre de convives : "))
sum = 0
NouvelleQuantite = 0
Qtf = " "
Check = False

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")

for sum in [fromage,eau,ail,pain]:

    if sum == fromage or sum == pain:
        if sum == fromage:
            Qtf = "gr de fromage"
        else:
            Qtf = "gr de pain"
    elif sum == eau and Check == False:
        Qtf = "dl d'eau"
        Check = True
    else:
        Qtf = "gousse(s) d'ail"
    nouvelleQuantite = ((sum *nbConvives)/BASE)

    print("- {} {}".format(nouvelleQuantite,Qtf))

# ------------------------------------------------------------------------------------------------------------------
# TP2 exo 5 Ecrivez un programme Python qui lit un nombre et indique 
# s'il est positif, négatif ou s'il vaut zéro ets'il est pair ou impair.

nombre = int(input("Entrer un nombre"))

if nombre > 0:
    if (nombre % 2) == 0:
        print(f"{nombre} est positif et paire ")
    else :
        print(f"{nombre} est positif et impaire ")
else :
    if (nombre % 2) == 0:
        print(f"{nombre} est négatif et paire ")
    else :
        print(f"{nombre} est négatif et impaire ")


# ------------------------------------------------------------------------------------------------------------------
# Exo 6 Ecrire un script nommé « tp2exo6.py » qui simule le lancer d’une pièce avec un nombre
# aléatoire entre 0 et 100, si le nombre est plus petit que 50, le résultat à afficher est « Pile !»
# sinon c’est « Face !»

import random 

cote =random.randint(0, 100)
print(cote)

if cote < 50 :
    print("Pile !")
else :
    print("Face !")


# ------------------------------------------------------------------------------------------------------------------
# Exo 7
import random 

cote =random.randint(0, 100)
print(cote)

if cote < 75 :
    print("Pile !")
else :
    print("Face !")
    
# autre méthode 
import random 

for i in range (2) :
    cote2 =random.randint(0, 50)
    print(cote)
    if cote < 75 :
        print("Pile !")
    else :
        print("Face !")



# ------------------------------------------------------------------------------------------------------------------
# Exo 8 Soit I = [2,3[ U ]0,1] U [-10,-2]  20, -10, -2, -1, 0, 1, 1.5, 2, 3 et 4.


reel = int(input("entrer un reel"))

if reel in range (1,2)or reel in range (-2, -10) :
    print(f"le reel '{reel}' appatient a l !")
else :
    print(f"le reel '{reel}' n'appartient pas a l")
    
 # avec les operateur conditionnelle 
 
reel2 = int(input("entrer un reel"))
 
if reel2 == 2 or reel2 == 1 or reel2 >= -10 and reel2 <= -2 :
    print(f"le reel '{reel2}' appatient a l !")
else :
    print(f"le reel '{reel2}' n'appartient pas a l")


# Fini ************************************************************