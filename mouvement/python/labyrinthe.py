# Labyrinthe

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random   

# Labyrinthe 
# valeur positive = distance à la source
# valeur -1 = pas encore visité
# valeur -2 = mur

# Données

### Exemple 1 : petit labyrinthe
Nx, Ny = 10, 5
labyrinthe = -np.ones((Nx, Ny), dtype=int)  
xdepart, ydepart = 0, 0
xarrivee, yarrivee = Nx-1, Ny-1
labyrinthe[xdepart, ydepart] = 0
labyrinthe[xarrivee, yarrivee] = -1

# Murs
# labyrinthe[3, 1] = -2
# labyrinthe[3, 2] = -2
# labyrinthe[3, 3] = -2
# labyrinthe[4, 3] = -2
# labyrinthe[5, 3] = -2
# labyrinthe[4, 1] = -2
# labyrinthe[9, 1] = -2
# labyrinthe[6, 0] = -2
# labyrinthe[1, 4] = -2
# labyrinthe[7, 4] = -2
# labyrinthe[7, 2] = -2

### Exemple 2 : grand labyrinthe
random.seed(314)
Nx, Ny = 50, 40
labyrinthe = -np.ones((Nx, Ny), dtype=int)  
xdepart, ydepart = 1, 1
xarrivee, yarrivee = Nx-2, Ny-2
labyrinthe[xdepart, ydepart] = 0
labyrinthe[xarrivee, yarrivee] = -1

nb_murs = 550
for i in range(nb_murs):
    labyrinthe[random.randint(0, Nx-1), random.randint(0, Ny-1)] = -2

###


def affichage(labyrinthe, valeurs=True, chemin=[]):
    """ Affichage du labyrinthe """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Chemin solution (en option)
    for i, j in chemin:
        ax.add_patch(Rectangle((i, j), 1, 1, color=[0.7,0.7,0.9]))

    for i in range(Nx):
        for j in range(Ny):

            if labyrinthe[i, j] == -2:
                ax.add_patch(Rectangle((i, j), 1, 1, color="gray",fill = True))
            elif (labyrinthe[i, j] >= 0) and valeurs:
                plt.text(i+0.5, j+0.5, str(labyrinthe[i, j]), color="blue",ha='center', va='center')

    # Grille
    for i in range(Nx+1):
       plt.plot([i, i], [0, Ny], color="gray")
    for j in range(Ny+1):
      plt.plot([0, Nx], [j, j], color="gray")                

    # Bordure
    ax.add_patch(Rectangle((-1, -1), Nx+2, 1, color="gray"))
    ax.add_patch(Rectangle((-1, -1), 1, Ny+2, color="gray"))
    ax.add_patch(Rectangle((0, Ny), Nx+1, 1, color="gray"))
    ax.add_patch(Rectangle((Nx, 0), 1, Ny+1, color="gray"))  

    # Départ et arrivée
    ax.add_patch(Rectangle((xdepart, ydepart), 1, 1, color=[0.5,0.8,0.5]))
    ax.add_patch(Rectangle((xarrivee, yarrivee), 1, 1, color=[0.8,0.5,0.5])) 

    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("labyrinthe-02-2.png", dpi=300)
    plt.show()

    return

# affichage(labyrinthe)


def nouveaux_voisins(i, j):
    """ Liste des voisins non visités de la case (i, j) """
    voisins = []
    if i > 0 and labyrinthe[i-1, j] == -1:
        voisins.append((i-1, j))
    if i < Nx-1 and labyrinthe[i+1, j] == -1:
        voisins.append((i+1, j))
    if j > 0 and labyrinthe[i, j-1] == -1:
        voisins.append((i, j-1))
    if j < Ny-1 and labyrinthe[i, j+1] == -1:
        voisins.append((i, j+1))
    return voisins

# Test
# print(nouveaux_voisins(0, 0))


def remplissage(labyrinthe, etapes=1000):
    """ Remplissage du labyrinthe """
    # Liste des cases à visiter
    file = [(xdepart, ydepart)]

    while file != []:
        # Choix d'une case à visiter qui a la plus petite valeur 
        i, j = file.pop(0)   # On dépile la première case 

        if labyrinthe[i, j] >= etapes:  # Optionnel : pour s'arrêter en court de route
            return

        # Mise à jour des voisins
        voisins = nouveaux_voisins(i, j)
        for v in voisins:
            labyrinthe[v] = labyrinthe[i, j] + 1
            file.append(v)
    return



# remplissage(labyrinthe,2)
# affichage(labyrinthe)


def tous_voisins(i, j):
    """ Liste des voisins de la case (i, j) """
    voisins = []
    if i > 0 and labyrinthe[i-1, j] >= 0:
        voisins.append((i-1, j))
    if i < Nx-1 and labyrinthe[i+1, j] >= 0:
        voisins.append((i+1, j))
    if j > 0 and labyrinthe[i, j-1] >= 0:
        voisins.append((i, j-1))
    if j < Ny-1 and labyrinthe[i, j+1] >= 0:
        voisins.append((i, j+1))
    return voisins


def chemin(labyrinthe):
    """ Chemin le plus court """
    i, j = xarrivee, yarrivee
    chemin = [(i, j)]
    while (i,j) != (xdepart, ydepart):
        voisins = tous_voisins(i, j)
        random.shuffle(voisins)  # mélange juste pour le fun
        for v in voisins:
            if labyrinthe[v] < labyrinthe[i, j]:
                i, j = v
                chemin.append((i, j))
                break
    return chemin


# Avant
# affichage(labyrinthe)

# Remplissage
remplissage(labyrinthe)
# affichage(labyrinthe)

# Solution
solution = chemin(labyrinthe)
affichage(labyrinthe, False, solution)

# solution = chemin(labyrinthe)
# affichage(labyrinthe, False, solution)

