# Exo 1  Operations sur les chaines de caractères

personne = int(input('combien de personne y a t-il '))

for i in range(personne):
    nom = str(input('entrer votre nom est prénom des personnes'))
    prenom = nom.split(" ")
    if prenom[0] <= prenom[2]:
        print(str.upper(prenom[0]), str.capitalize(prenom[1]))
        print(str.upper(prenom[2]), str.capitalize(prenom[3]))
    else :
        print(str.upper(prenom[2]), str.capitalize(prenom[3]))
        print(str.upper(prenom[0]), str.capitalize(prenom[1]))
    

# Exercice 2 : Notes

moyenne = []
coefficient = []

for i in range(5):
    notes = (input("Veuillez entrer la note du module 1 et le coefficient correspondant :"))
    coeff = notes.split(" ")
    print(coeff)
    if float(coeff[0]) < 8 :
        print("Vous n'êtes pas admis ")
    else :
        notes2 = float(coeff[0]) * int(coeff[1])
        moyenne.append(notes2)
        coefficient.append(int(coeff[1]))

print(moyenne)
print(coefficient)
sum(moyenne)
sum(coefficient) 

vraisMoyenne = moyenne[0] / coefficient[0]
print(vraisMoyenne)

if vraisMoyenne < 10 :
    print("Vous n'êtes pas admis")
else :
    print("Vous etes admis")


# Exo 3 Palindromes

pal = str(input("Entrez un mot ou une phrase :"))
pal = ''.join(filter(str.isalnum, pal)) 
pal = str.lower(pal)
print(pal)

if str(pal) == str(pal[::-1]) :
    print("C'est un palimdrome !")
else :
    print("Ce  n'est pas un palimdrome !")



#Esope reste ici et se repose

# Exo 4 La monnaie (TD1)

nombre = int(input("Entrez un nombre"))
initnombre = nombre
B100 = 0
B50 = 0
B10 = 0
P2 = 0
P1 = 0
if nombre > 100 :
    B100 = int(nombre / 100)
    nombre = nombre % 100

if nombre >  50 :
   B50 = int(nombre / 50)
   nombre = nombre % 50

if nombre >  10 :
   B10 = int(nombre / 10)
   nombre = nombre % 10

if nombre >  2 :
   P2 = int(nombre / 2)
   nombre = nombre % 2

if nombre ==  1 :
   P1 = 1
    
    
print(f"{initnombre} euros, c’est donc {B100} billets de 100, {B50} de 50, {B10} de 10, {P2} pièces de 2 et {P1} pièce 1.")
    
# Exo 5 Fiche de paye (TD2)

horraire = int(input("entrer le nombre d'heure travailler"))
salaire = int(input("entrer votre salaire par heure"))


if horraire in range(1, 160):
    total = horraire * salaire
    print(total)
    horaire = horraire - 160

if horraire > 0 :
    total = (total*1.25) *horraire
    

print(f"Votre salaire et de {total} ")    
