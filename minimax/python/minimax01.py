## Mathgame
## Parcours d'arbres


######
## A. Définition de la classe Noeud


# Objet  'Noeud' c'est un sommet avec une valeur et une liste d'enfants (qui sont eux mêmes des Noeuds)
class Noeud:
    def __init__(self, val):
        self.enfants = []
        self.val = val

# Exemple 
racine = Noeud(1)
enfant1 = Noeud(2)
enfant2 = Noeud(3)
enfant3 = Noeud(4)
racine.enfants = [enfant1, enfant2, enfant3]

petitenfant1 = Noeud(5)
petitenfant2 = Noeud(6)
enfant2.enfants = [petitenfant1, petitenfant2]

petitenfant3 = Noeud(7)
petitenfant4 = Noeud(8)
enfant3.enfants = [petitenfant3, petitenfant4]


######
## B. Parcours d'arbre en profondeur

def parcours_arbre_profondeur(noeud):
    """ Parcours de l'arbre du haut vers le bas, de la gauche vers la droite. """
    print(noeud.val)
    for enfant in noeud.enfants:
        parcours_arbre_profondeur(enfant)

# Test
print("--- Parcours en profondeur ---")
parcours_arbre_profondeur(racine)


## Version avec affichage hiérachisé
def parcours_arbre_profondeur_niveau(noeud, niveau=0):
    """ Parcours de l'arbre du haut vers le bas, de la gauche vers la droite.
    Affichage avec décalage selon niveau """
    print("\t"*niveau, noeud.val)
    for enfant in noeud.enfants:
        parcours_arbre_profondeur_niveau(enfant, niveau=niveau+1)

# Test
print("--- Parcours en profondeur (avec hiérachie) ---")
parcours_arbre_profondeur_niveau(racine)

######
## C. Parcours d'arbre en largeur

def parcours_arbre_largeur(noeud):
    """ Parcours de l'arbre de la gauche vers la droite, du haut vers le bas. """
    file = [noeud]
    while file != []:
        noeud = file.pop()
        print(noeud.val)
        for enfant in noeud.enfants:
            file = [enfant] + file

# Test
print("--- Parcours en largeur ---")
parcours_arbre_largeur(racine)

