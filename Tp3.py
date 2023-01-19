# TP3
# Exo 1

n = int(input("Choisisser un nombre :"))
som = 0

for i in range(0,n+1):
    som += i
print("La somme est :", som)

# ---------------------------------------------------------------------------

n = 0

while n != 100:
    n = int(input("Entrez 100 :"))

# ----------------------------------------------------------------------------------------

def number():
    n = int(input("entrez une valeur :"))
    if (n < 0 and n > 20):
        n = int(input("entrez une valeur :"))
    else :
        return n

V10 = 0
V1015 = 0
V15 = 0

l = []
for i in range(0,10):
    l.append(number())

for x in l :
    if x < 10:
        V10 += 1
    elif x <= 15:
        V1015 += 1
    else :
        V15 += 1

print("Le nombre de valeurs inférieur strictement à 10", V10)
print("Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15", V1015)
print(" Le nombre de valeurs supérieur ou égale à 15", V15)



def number():
    k = int(input("Veuillez rentrer un réel :"))
    while (k < 0 or k > 20) :
        k = int(input("Veuillez rentrer un réel :"))
    else:
        return k

v_10 = 0
v_105 = 0
v_15 = 0

n = []
for i in range(0,10):
    n.append(number())

for x in n:
    if x < 10:
        v_10 += 1
    elif x >= 15:
        v_15 += 1
    else:
        v_105 += 1
print(f"Le nombre de valeurs inférieur à 10 est {v_10}",
      f"Le nombre de valeurs superieur ou egale à 15 est {v_15}",
      f"Le nombre de valeurs superieur ou egale à 10 et inferieur à 15 est {v_105}", sep="\n")

# ------------------------------------------------------------------------------------------------------------

n = int(input("Veuillez entrez un nombre : "))
som = 0

if n > 1 :
    for i in range(0,n+1):
        som += i
        if som <= n :
            print(i)

# ----------------------------------------------------------------------------------------------
# Exo 2

import time

n = int(input("entrez une valeur entiere positif :"))
for i in range(0,n+1):
    print(n-i)
    time.sleep(0.2)

n = int(input("entrez une valeur entiere positif :"))
while n >= 0:
    print(n)
    n-= 1
    time.sleep(0.2)

# ------------------------------------------------------------------------------------
# Exo 3

import random

n = random.randint(0,100)
x = 0
print(n)
i = int(input("Entrez un nombre"))
while i != n :
    if i < n :
        print("le nombre choisit et plus grand")
        i = int(input("Entrez un nombre"))
        x += 1
    elif i >n :
        print("Le nombre choisie est plus petit")
        i = int(input("Entrez un nombre"))
        x += 1
print("nombre correcte trouvez !")
print("en",x+1," essaye.")

# ------------------------------------------------------------------------------
# Exo 4

print("choisisser votre boucle !")
print("1- pour une boucle for !")
print("2 - pour une boucle while !")
bl = int(input("faites un choix !"))
n = int(input("choisissez un nombre !"))

fact = 1
fac = 1

if n == 0 :
    print("Le factoriel de ",n,"est",fact)

if bl == 1:
    for i in range(0,n):
        fac *= n-i
    print("le factoriel de",n,"est",fac)

if bl == 2 :
    i = 0
    while ((n-i)) != 0:
        fac *= (n-i)
        i += 1
    print("le factoriel de ",n,"est", fac)





#Exo 5 location de vélo 1 euro par heure si le vélo est loué entre 0h et 7h 
# ou entre 17h et 24h ;2 euros par heure si le vélo est loué entre 7h et 17h.

n = int(input("Donnez l’heure de début de la location (un entier) :"))
nf = int(input("Donnez l’heure de fin de la location (un entier) : "))
h = nf - n
heure = 0
heure1 = 0

if h < 0 :
    print("vous ne pouvez pas louée un vélo plus de 24h !")
else :
    print("Vous avez loué votre vélo pendant ")
    for i in range(n, nf): 
        print(i)  
        if i in range(10,17):
            heure += 1 
            print(heure)
        elif i in range(0,7) or i in range(17,24): 
            heure1 += 1
            print(heure1)

if heure and heure1 > 0 :
    print(f"{heure1} heure(s) au tarif horraire de 1.0 euro(s)")
    print(f"{heure} heure(s) au tarif horraire de 2.0 euro(s)")
elif heure < 1 :
     print(f"{heure1} heure(s) au tarif horraire de 1.0 euro(s)")
elif heure1 < 1 : 
    print(f"{heure} heure(s) au tarif horraire de 2.0 euro(s)")
        
print(f"le montant total a payer est de {heure*2 + heure1} euro (s)") 


# Fini ************************************************************