#Exo 1 
nom = str(input("entrer votre nom :"))
prenom = str(input("entrer votre prenom :"))
math = float(input("entrer votre note de math"))
anglais = float(input("entrer votre note d'anglais"))
info = float(input("entrer votre note d'info"))
promotion = int(input("entrer l'année de votre premiere années"))
moy = (anglais + math + info)/ 3

print(f"<< Létudiant {nom} {prenom} de la promotion {promotion} a une moyenne de {(round(moy, 1))}>>")

# Exo 2 
jour = 20
heure = 12
minute = 31

if jour in range(0, 32):
    jour = jour * 1440
else : 
    print("ce jour n'existe pas !")
    
if heure in range(0, 24):
    heure = heure * 60
else : 
    print("cette heure n'existe pas !")
    
if minute in range(0, 60):
    minute = minute
else : 
    print("ces minute n'existe pas !")
    
total = jour + heure + minute
print(f"dans ce mois il ces écouler {total} minutes")

#---------------
# Exo 3 

jour = int(input("Entrer un jour :"))
heure = int(input("Entrer une heure :"))
minute = int(input("Entrer une minute :"))

if jour in range(0, 32):
    jour = jour * 1440
else : 
    print("ce jour n'existe pas !")
    
if heure in range(0, 24):
    heure = heure * 60
else : 
    print("cette heure n'existe pas !")
    
if minute in range(0, 60):
    minute = minute
else : 
    print("ces minute n'existe pas !")
    
total = jour + heure + minute
print(f"dans ce mois il ces écouler {total} minutes")

# Exo 4 a finir !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

temps = int(input("enter un nombre de minute : "))
fin = temps  
heure = 0
jour = 0 
minute = 0

if temps >= 1440 :
    print(temps / 1440)
    print(temps % 1440)
    jour = round((temps / 1440), 0)
    temps = temps % 1440

if temps >= 60 :
    print(temps / 60)
    print(temps % 60)
    heure = round((temps / 60), 1)
    temps = temps % 60
    
if temps < 60 :
     minute = round(temps,1)

print(f"Dans {fin} minute il y a {jour} jour, {heure} heure, {minute} minute ")

# Exo 5 

import random as rd 

print(rd.randint(0, 100))

# Fini ************************************************************