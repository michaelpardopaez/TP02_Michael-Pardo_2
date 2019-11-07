"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""
### Déclaration des constantes
NB_SAND: int = 1
NB_CHIP: int = 2
NB_BARR: int = 3
NB_BON: int = 4
NB_TEA: int = 5
NB_LIMO: int = 6
offre_pro: str = "#POU"

### Déclaration des variables

SANDWICH: float
CHIPS: float
BARRE: float
BONBONS: float
TEA: float
LIMONADE: float

monnaie: float
produit: int
monnaie_insufi: float
prix: float
###Initialisation des variables
SANDWICH: float = 4.90
CHIPS: float = 2.50
BARRE: float = 2.00
BONBONS: float = 3.30
TEA: float = 2.20
LIMONADE: float = 1.90
monnaie: float = None
produit: int = None
monnaie_insufi: float = None
prix: float = None
### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")

# Demande à l'utilisateur
monnaie: float = None
produit: int = None
monnaie_insufi: float = None
# tester tout d'abord si le produit existe dans la liste des produits
while produit is None or produit >= 0:
    produit: int = int(input("Veuillez sélectionner un produit  et votre offre promotionnelle: "))
    if produit > 6: # si le produit n'exite pas in demande jusque le bon produit soit sélectionné
        print("Le produit sélectionné n'existe pas !")
    elif produit <= 6: # Affiche le prix du produit sélectionné
        if produit == NB_SAND:
            prix = SANDWICH
            print("Le prix à payer est de {:.2f}:".format(prix))
        elif produit == NB_CHIP:
            prix = CHIPS
            print("Le prix à payer est de {:.2f}:".format(prix))
        elif produit == NB_BARR:
            prix = BARRE
            print("Le prix à payer est de {:.2f}:".format(prix))
        elif produit == NB_BON:
            prix = BONBONS
            print("Le prix à payer est de {:.2f}:".format(prix))
        elif produit == NB_TEA:
            prix = TEA
            print("Le prix à payer est de {:.2f}:".format(prix))
        elif produit == NB_LIMO:
            prix = LIMONADE
            print("Le prix à payer est de {:.2f}:".format(prix))
        break
while monnaie is None or monnaie <= prix:
    monnaie : float = float(input("Veuillez introduire votre monnaie :"))
    if monnaie > SANDWICH and produit == NB_SAND:
        print("Monnaie à rendre {:.2f}: ".format(monnaie - SANDWICH))
        print("Sandwich au poulet servie ! Bon appétit ! ")
    elif monnaie > CHIPS and produit == NB_CHIP:
        print("Monnaie à rendre {:.2f}: ".format(monnaie - CHIPS))
        print("Chips servies ! Bon appétit ! ")
    elif monnaie > BARRE and produit == NB_BARR:
        print("Monnaie à rendre {:.2f}: ".format(monnaie - BARRE))
        print("Barre chocolatée servie ! Bon appétit ! ")
    elif monnaie > BONBONS and produit == NB_BON:
        print("Monnaie à rendre {:.2f}: ".format(monnaie - BONBONS))
        print("Bonbons servies ! Bon appétit ! ")
    elif monnaie > TEA and produit == NB_TEA:
        print("Monnaie à rendre {:.2f}: ".format(monnaie - TEA))
        print("Ice tea servie ! Santé ! ")
    elif monnaie > LIMONADE and produit == NB_LIMO:
        print("Monnaie à rendre {:.2f}: ".format(monnaie - LIMONADE))
        print("Limonade servie ! Santé ! ")
    elif monnaie < prix:
        print("Le montant est insuffisant. Veuillez ajouter encore {:.2f} :".format(prix - monnaie))
