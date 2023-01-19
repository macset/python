# Exo 1 

num = float(input("vous chercherr la table de multiplication de quelle nombre ?"))



for i in range(1,11):
    multiple = num*i
    print(f"{num} * {i} = {multiple}")
    
    
# exo 2 

# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []  

for i in range(nombreEtudiants):
    notesEtudiants = float(input(f"entrer la notes de l'eleve {i}"))
    if notesEtudiants in range (0,20):
        notes.append(notesEtudiants)
        print(f"notes étudiants {i} : {notesEtudiants}")
        moyenne += notesEtudiants
moyenne = moyenne / nombreEtudiants

print(f"moyenne de classe: {moyenne}")

for i in range(nombreEtudiants):
    print(f"{i} | {notes[i]} | {notes[i] - moyenne}")
    
    
# Exo 3 

nMax = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))

v1 = []
v2 = []

for i in range(nMax): 
    vecteur = int(input("Saisie du premier vecteur : "))
    print(f"v1[{i}] = {vecteur}")
    v1.append(vecteur)
    
for i in range(nMax): 
    vecteur2 = int(input("Saisie du deuxieme vecteur : "))
    print(f"v2[{i}] = {vecteur2}")
    v2.append(vecteur2)

for i in range(len(v1)):
    scalaire = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2] 

print(f"le produit scalaire de v1 et v2 vaut {scalaire}")

# Exo 4 

L1 = {2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6}

occurrences = {}
for item in L1:
    if item in occurrences:
        occurrences[item] += 1
    else:
        occurrences[item] = 1

most_frequent = max(occurrences, key=occurrences.get)


print(f"L'élément le plus fréquent est: {str(most_frequent)}")
print(f"Fréquence d'apparition: {str(occurrences[most_frequent])}")

# Exo 5 

dates = str(input("entrer une date au format jjmmaaaa"))
print(dates)

while len(dates) != 8: 
        dates = str(input("mauvais format veuiller ecrire une date de format jjmmaaaa"))
        

annee = dates[4]+dates[5]+dates[6]+dates[7]
mois = dates[2]+dates[3]
jour = dates[0]+dates[1]


if int(annee) % 4 == 0:
    if int(mois) == 2 :
        if int(jour) > 29 :
            print("date invalide")
        else :
            print("Date valide")
            
    if int(mois) == 1 or  int(mois) == 3 or int(mois) == 5 or int(mois) == 7 or int(mois) == 8 or int(mois) == 10 or int(mois) == 12 :
        if int(jour) < 32 and int(jour) > 0 :
            print("Date correcte")
        else :
            print("Date incorrect")
    if int(mois) == 4 or  int(mois) == 6 or int(mois) == 9 or int(mois) == 11 :
        if int(jour) < 31 and int(jour) > 0 :
            print("Date correcte")
        else :
            print("Date incorrect")
else :
    if int(mois) == 2 :
        if int(jour) > 28 :
            print("date invalide")
        else :
            print("Date valide")
            
    if int(mois) == 1 or  int(mois) == 3 or int(mois) == 5 or int(mois) == 7 or int(mois) == 8 or int(mois) == 10 or int(mois) == 12 :
        if int(jour) < 32 and int(jour) > 0 :
            print("Date correcte")
        else :
            print("Date incorrect")
    if int(mois) == 4 or  int(mois) == 6 or int(mois) == 9 or int(mois) == 11 :
        if int(jour) < 31 and int(jour) > 0 :
            print("Date correcte")
        else :
            print("Date incorrect")

# Exo 6  !!!!!!!!!

L2 = []

taille = int(input("entrer la taille de la listes"))


for i in range(taille):
    tirage = (input("entrer un nomdre !"))
    L2.append(tirage)
    print(L2)
    

for i in range(len(L2)-1, 0, -1):
    for j in range(i): 
        if L2[j] > L2[j+1]:
            L2[j], L2[j+1] = L2[j+1], L2[j] 
    print(L2)


# Exo 7 tuple 

binnome = ('trepier', 'Timothee', 'Mourot', 'Corentin')

login1, login2 = 'Trepier' ' Timothee', 'Mourot ''Corentin'


print(f"l'étudiant {login1} et en binome avec l'étudiant {login2}")

