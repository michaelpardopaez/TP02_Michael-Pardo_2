"""
    Programme permettant de savoir si un trajet ou une série de trajet sont réalisable par rapport
    au réservoir d'essence d'une voiture. Pour ce faire il faut spécifier une distance en kilometres
    et un nombre de passagers à bord(sans compte le conducteur).
    Indications:
        - Le véhicule a les caractéristiques suivantes :
            - Une consommation fixe de 5.0 litre pour 100km
            - Le recervoir a une capacité de 32.5 litres
            - Pour chaque personne ajoutée (le conducteur ne compte pas), l'essence utilisée augmente de 30%
              en rapport à la consommation normale
                - Exemple : pour 1 personne en plus du conducteur, la consommation vaut 1.3 fois la consommation normale
                            pour 2 personnes en plus du conducteur, la consommation vaut 1.6 fois la consommation normale
        - Lors de la saisie de la distance, si l'utilisateur met 0, le programme rempli le réservoir d'essence
          du véhicule
        - Lorsque qu'un voyage est réalisable, un message affiche le nombre de litres restants
        - Le programme se termine uniquement si une panne d'essence se produit. Si cela arrive,
          Un message affiche que la panne arrivera lors de ce trajet. Un second message affichera
          la distance parcourue avec tous les trajets.

"""
# Déclaration et initialisation des constantes
CONSO_FIXE: float = 5.0
RECERVOIR: float = 32.5
PERSONNE_1: float = 1.3
PERSONNE_2: float = 1.6
PERSONNE_3: float = 1.9
PERSONNE_4: float = 2.1

### Déclaration et  Initialisation des variables
distance: float = None
nb_personnes: int = None
reservoir_rest: float = 32.5
nb_km: float = 0

### Séquence d'opération
while distance is None or reservoir_rest > 0 or reservoir_rest == RECERVOIR: # on demande la distance juaqu'au on a plus d'essences
    distance: float = float(input("Entrez la distance de votre destination ou entrez 0 pour faire le plein :"))
    nb_km: float = nb_km + distance ## Stock la distance parcoru jusqu'au on a plus d'essences

    if distance == 0:
        reservoir_rest = RECERVOIR ## si l'utilisateru tape 0 on remplie le recervoir
        print("Le recervoir est rempli totalement")
        if reservoir_rest == RECERVOIR: ## si le recervoir est plein on redemande la distance
            distance: float = float(input("Entrez la distance de votre destination ou entrez 0 pour faire le plein :"))
## Ici on calcule combien nous reste après le parcours
    while nb_personnes is None or reservoir_rest > 0:
        nb_personnes: int = int(input("Combien de personnes font parties du trajet en plus du conducteur ?"))
        if nb_personnes > 4: ## J'ai pensé que c'est un véhicule à 5 places, donc si il y plus de 5 personne on peut pas faire le parcours
            print("Le véhicule n'as que 4 plasces (avec le conducteur) !")
        elif nb_personnes == 1:
            reservoir_rest = reservoir_rest - (CONSO_FIXE * distance / 100 * PERSONNE_1)
            print("Il vous reste encore {:.2f}".format(reservoir_rest), "litres")
        elif nb_personnes == 2:
            reservoir_rest = reservoir_rest - (CONSO_FIXE * distance / 100 * PERSONNE_2)
            print("Il vous reste encore {:.2f}".format(reservoir_rest), "litres")
        elif nb_personnes == 3:
            reservoir_rest = reservoir_rest - (CONSO_FIXE * distance / 100 * PERSONNE_3)
            print("Il vous reste encore {:.2f}".format(reservoir_rest), "litres")
        elif nb_personnes == 4:
            reservoir_rest = reservoir_rest - (CONSO_FIXE * distance / 100 * PERSONNE_4)
            print("Il vous reste encore {:.2f}".format(reservoir_rest), "litres")
        elif nb_personnes == 0:
            reservoir_rest = reservoir_rest - (CONSO_FIXE * distance / 100)
            print("Il vous reste encore {:.2f}".format(reservoir_rest), "litres")
        if reservoir_rest <= 0:
            print("Vous allez tomber en panne d'essence lors de ce traje ! "
                  "Pensez à le raccousrcir ou faire le plein")
        break ## J'arrête la boucle
print()
## Affiche les kms parcourus
if reservoir_rest <= 0:
    print("Vous aurez parcouru {:.2f}".format(nb_km), "km")
