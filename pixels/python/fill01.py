from math import *

from matplotlib import pyplot as plt
import numpy as np

Nx, Ny = 20, 15
grille = np.zeros((Nx,Ny))
# Couleurs : 
#   0 = blanc (vide)
#   1 = gris  (couleur remplissage)
#   2 = noir  (bord)

# Exemple 1
Nx, Ny = 20, 15
grille1 = np.zeros((Nx,Ny))
for i in range(Nx):
    grille1[i,(i+5) % Ny] = 2
    grille1[i,-(i+6) % Ny] = 2
grille1[9,7] = 2
grille1[10,7] = 2
grille1[9,8] = 2
grille1[9,9] = 2
grille1[10,6] = 2
grille1[10,5] = 2




### Affichage
def affiche(grille, n=-1):

    fig = plt.figure()
    ax = plt.axes(aspect='equal')

    plt.imshow(grille.T, interpolation=None, cmap='Greys', vmin=0, vmax=2)

    plt.axis('off')
    plt.tight_layout()    

    if n>=0:
        plt.savefig('fill02_{:03d}.png'.format(n), dpi=300)

    # plt.show()


# Test
grille[2,3] = 2
# affiche(grille)
# affiche_pixels([(0,1),(1,2),(2,3),(3,4)])
# affiche_pixels([(0,1,0.1),(1,2,0.5),(2,3,0.2),(3,4,0.0)])


def remplissage_recursif(x, y, grille):
    """ Colorie une région délimitée par pixels noirs à partir d'un point source """
    # affiche(grille)
    Nx, Ny = grille.shape 
    if (0 <= x < Nx) and (0 <= y < Ny) and grille[x,y] == 0:  # si pixel blanc
        # print(x,y)
        grille[x,y] = 1   # alors le colorier

        # Appel récursif des 4 pixels voisins
        remplissage_recursif(x-1, y, grille)
        remplissage_recursif(x+1, y, grille)
        remplissage_recursif(x, y+1, grille)
        remplissage_recursif(x, y-1, grille)

    return    


# Test
# affiche(grille1)
# remplissage_recursif(2, 2, grille1)
# affiche(grille1)



def remplissage_file(x0, y0, grille):
    """ Colorie une région délimitée par pixels noirs à partir d'un point source """

    # affiche(grille)
    Nx, Ny = grille.shape 

    file = [ (x0,y0) ]

    # n = 0

    while len(file)>0:
        # print(len(file))

        x, y  = file.pop(0)
        if (0 <= x < Nx) and (0 <= y < Ny) and grille[x,y] == 0:  # si pixel blanc
            # print(x,y)
            grille[x,y] = 1   # alors le colorier

            # Ajout des 4 pixels voisins à la file
            file.append( (x-1, y) )
            file.append( (x, y+1) )
            file.append( (x+1, y) )
            file.append( (x, y-1) )

        # affiche(grille, n)
        # n = n + 1
    return    


# Test
# affiche(grille1)
# remplissage_file(10, 10, grille1)
# affiche(grille1)


def remplissage_balayage(x0, y0, grille):
    """ Colorie une région délimitée par pixels noirs à partir d'un point source """
    
    # affiche(grille)
    Nx, Ny = grille.shape 

    file = [ (x0,y0) ]

    n = 1

    while len(file)>0:
        x, y  = file.pop(0)

        # balayage vers la gauche de (x,y)
        xmin = x-1     
        while xmin >= 0 and grille[xmin,y] == 0:  # si pixel blanc
            grille[xmin,y] = 1   # alors le colorier
            xmin = xmin - 1

        # balayage vers la droite de (x,y)
        xmax = x
        while xmax < Nx  and grille[xmax,y] == 0:  # si pixel blanc
            grille[xmax,y] = 1   # alors le colorier
            xmax = xmax + 1

        for xx in range(xmin+1, xmax):
            if y < Ny-1 and grille[xx,y+1] == 0:
                file.append( (xx, y+1) )
            if y > 0 and grille[xx,y-1] == 0:
                file.append( (xx, y-1) )  

        affiche(grille, n)
        n = n + 1
        # affiche(grille)
    return   


# Test
affiche(grille1)
# remplissage_file(11, 9, grille1)
remplissage_balayage(11, 9, grille1)
# affiche(grille1)