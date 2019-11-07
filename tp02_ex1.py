"""
Considérons les opérations suivantes applicables à un nombre entier (positif) :
    — si ce nombre est divisible par 3, on lui ajoute 4 ;
    — s’il n’est pas divisible par 3 mais divisible par 4, on le divise par 2;
    — s’il n’est divisible ni par 3, ni par 4, on lui soustrait 1.
On répète ces opérations successivement jusqu’à arriver à 0.

Ecrivez un programme affichant le nombre d'opérations pour arriver à 0 pour
chaque chiffre entier compris entre deux valeurs demandées à l'utilisateur.

"""
###Déclaration et Initialisation des variables
nb : int = None
nbmin : int =None
nbmax : int = None
# Saisir les valeurs
while nbmin is None:
    nbmin : int = int (input("Saisir le 1er nombre entier et positif :"))

while nbmax is None or nbmin > nbmax:
    nbmax : int = int (input("Saisir le 2ème nomnre entier et positif :"))


### Séquence d'opération

for i in range(nbmin, nbmax + 1):
     print(1,"->", end= "")
     nb = 0
     while 1 != 0:
        if i % 3 == 0:
             i + 4
        elif i % 4 == 0:
            i //= 2
        else:
            i -=1
        nb += 1

        print(nb)
