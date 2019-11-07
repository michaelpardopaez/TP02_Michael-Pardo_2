import random

"""
    Programme simulant un jeu de BlackJack avec des lancés de dés. L'objectif du jeu est d'arriver au plus proche de
    21 sans dépasser 21. Pour se faire l'utilisateur peut lancer un nombre de dés de son choix. Le programme simule un
    lancer de dés (en générant aléatoirement des valeurs entre 1 et 6) et obtiens une somme. L'utilisateur peut décider
    de continuer de lancer des dés supplémentaires ou de s'arrêter (entrer 0 lorsque l'on demande le nombre de dés).
    L'ordinateur joue également en parallèle avec sa propre somme et son score est affiché également. Le jeu se termine lorsque le
    joueur ET l'ordinateur ont terminé de jouer.

    Indications:
        - Si le joueur entre 0 comme nombre de dés à lancer, cela signifie qu'il arrête de lancer plus de dés et sa partie se termine
        - Voici le détail sur la stratégie de jeu de l'ordinateur:
            - Si la somme de l'ordinateur est inférieure à 6, il demande 3 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 6 et inférieure à 12, il demande 2 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 12 et inférieure à 18, il demande 1 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 18, il s'arrête de jouer

"""
### Déclaration et initialisation de variables
des : int = None
score_jouer : int

### Séquence d'opérations
while des is None or score_jouer <= 0:
    des : int = int(input("Combien des dés souhaitez-vous lancer ?"))
    for i in range (des):
        score_jouer = (random.randint(1,6))
if sum(score_jouer) >21:
    print("Vous avez perdu {}".format(score_jouer))
print(score_jouer)
