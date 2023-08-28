# Labyrinthe

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Terrain 
# valeur 1 : terrain normal
# valeur 2 : terrain difficile
# valeur 5 : eau
# valeur infini : obstacle infranchissable

infini = 1000 # 

# Données

### Exemple 1 : petit terrain
# Nx, Ny = 10, 5
# terrain = np.ones((Nx, Ny), dtype=int)  
# xdepart, ydepart = 0, 1
# xarrivee, yarrivee = Nx-2, Ny-3

# # Terrain difficile
# terrain[4:6, 2:6] = 2
# terrain[4, 0] = 2

# # Obstacles
# terrain[2, 3] = infini
# terrain[4, 1] = infini
# terrain[9, 1] = infini
# terrain[6, 0] = infini

# # Eau
# terrain[1:3, 0:2] = 5
# terrain[7, 4] = 5
# terrain[8, 4] = 5


### Exemple 2 : grand terrain
Nx, Ny = 40, 20
terrain = np.ones((Nx, Ny), dtype=int)  
xdepart, ydepart = 2, 5
xarrivee, yarrivee = 37, 12

# Terrain difficile
terrain[5:10, 5:15] = 2
terrain[18:23, 8:20] = 2
terrain[13:17, 0:12] = 2

# Obstacles
terrain[11,0:10] = infini
terrain[33,5:15] = infini

# Eau
terrain[26:28, 0:Ny] = 5
terrain[24:26, 5:15] = 5
terrain[28:30, 5:15] = 5

############################
### Affichage du terrain ###

def rgb(value, minimum, maximum):
    """ fonction qui renvoie la couleur +/- chaude selon la valeur """
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2*(value-minimum) / (maximum - minimum)
    b = max(1 - ratio,0)
    r = max(ratio - 1,0)
    g = max(1 - b - r,0)
    return r, g, b


def affichage_terrain(terrain, heatmap=None, gradient = None, withcolor=False, withtext=False, withgrille=True, withgradient=False):
    """ Affichage du terrain """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in range(Nx):
        for j in range(Ny):
            if terrain[i, j] == 1:
                ax.add_patch(Rectangle((i, j), 1, 1, color=[0.95,0.95,0.95],fill = True))
            if terrain[i, j] == 2:
                ax.add_patch(Rectangle((i, j), 1, 1, color=[0.7,0.7,0.7],fill = True))
            elif (terrain[i, j] == 5):
                ax.add_patch(Rectangle((i, j), 1, 1, color="blue",fill = True))
            elif (terrain[i, j] == infini):
                ax.add_patch(Rectangle((i, j), 1, 1, color="black",fill = True))     

    # Départ et arrivée
    ax.add_patch(Rectangle((xdepart, ydepart), 1, 1, color=[0.5,0.8,0.5]))
    ax.add_patch(Rectangle((xarrivee, yarrivee), 1, 1, color=[0.8,0.5,0.5])) 

    if heatmap is not None and withtext:
        for i in range(Nx):
            for j in range(Ny):
                if heatmap[i, j] < infini:
                    plt.text(i+0.5, j+0.5, "{:.1f}".format(heatmap[i, j]), 
                        horizontalalignment='center', verticalalignment='center')
                if heatmap[i, j] == infini:
                    plt.text(i+0.5, j+0.5, "∞", 
                        horizontalalignment='center', verticalalignment='center')
                    
    if heatmap is not None and withcolor:
        secondmax = np.max(heatmap[heatmap < infini])
        for i in range(Nx):
            for j in range(Ny):       
                val = secondmax - np.minimum(heatmap[i, j],secondmax)
                coul = rgb(val, 0, secondmax)
                ax.add_patch(Rectangle((i, j), 1, 1, color=coul,fill = True))   

    if gradient is not None and withgradient:
        gradientx, gradienty = gradient
        for i in range(Nx):
            for j in range(Ny):       
                valx = gradientx[i, j]
                valy = gradienty[i, j]
                # norme = 3
                norme = 2*np.sqrt(valx**2 + valy**2)
                if norme > 0:
                    plt.arrow(i+0.5, j+0.5, valx/norme, valy/norme, head_width=0.1, head_length=0.1, fc='k', ec='k')

    # Grille
    if withgrille:
        for i in range(Nx+1):
            plt.plot([i, i], [0, Ny], color="gray")
        for j in range(Ny+1):
            plt.plot([0, Nx], [j, j], color="gray")                

    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    # plt.savefig("terrain-02-4.png", dpi=300)
    plt.show()

    return

# affichage_terrain(terrain)   # Exemple 1
# affichage_terrain(terrain, withtext=False, withgrille=False)   # Exemple 2

##############
### Outils ###


def tous_voisins(i, j, terrain):
    """ Liste des 8 voisins de la case (i, j) """
    voisins = []
    if i>0:
        voisins.append((i-1, j))
    if i>0 and j>0:
        voisins.append((i-1, j-1))
    if i>0 and j<Ny-1:
        voisins.append((i-1, j+1))    
    if i<Nx-1:
        voisins.append((i+1, j))
    if i<Nx-1 and j>0:
        voisins.append((i+1, j-1))
    if i<Nx-1 and j<Ny-1:
        voisins.append((i+1, j+1))
    if j>0:
        voisins.append((i, j-1))
    if j<Ny-1:
        voisins.append((i, j+1))

    return voisins

#################
### Distances ###


def distance1(i,j,ii,jj):
    """ Distance de Manhattan entre (i, j) et (ii, jj) (norme 1)"""
    return abs(ii-i) + abs(jj-j)

def distance2(i,j,ii,jj):
    """ Distance euclidienne entre (i, j) et (ii, jj) (norme 2)"""
    return np.sqrt((ii-i)**2 + (jj-j)**2)

def distance3(i,j,ii,jj):
    """ Distance de Chebychev entre (i, j) et (ii, jj) (norme infinie)"""
    return max(abs(ii-i), abs(jj-j))


###############
### Heatmap ###

def calcule_heatmap(terrain, dist=distance2, etapes=1e5):
    """ Remplissage du terrain """
    # Liste des cases à visiter

    heatmap = infini*np.ones((Nx, Ny), dtype=float)  # Valeurs de la heatmap

    heatmap[xarrivee, yarrivee] = 0
    file = [(xarrivee, yarrivee)]

    k = 0  # nb d'étapes  (juste pour info)

    while file != []:
        # Choix d'une case à visiter qui a la plus petite valeur 
        i, j = file.pop(0)   # On défile

        # Mise à jour des voisins
        voisins = tous_voisins(i, j, terrain)
        for ii,jj in voisins:
            distance = heatmap[i,j] + dist(i,j,ii,jj)*terrain[ii,jj]
            if distance < heatmap[ii, jj]:
                heatmap[ii, jj] = distance

                file.append((ii, jj))

        if k > etapes:  # Optionnel : pour s'arrêter en court de route
            return heatmap
        k += 1
    
    return heatmap


# heatmap = calcule_heatmap(terrain, dist=distance2)

# # affichage_terrain(terrain, heatmap=heatmap, withcolor=True, withtext=True, withgrille=True)  # Exemple 1
# affichage_terrain(terrain, heatmap=heatmap, withcolor=True, withtext=False, withgrille=False)  # Exemple 2

###############################
### Convolution vectorielle ###

def fonction_decroissante(x):
    if x == 0:
        return 0
    else:
        return -0.5*1/x
    

def calcule_gradient(heatmap, f = lambda x:-x):
    gradientx = np.zeros((Nx, Ny), dtype=float)
    gradienty = np.zeros((Nx, Ny), dtype=float)
    for i in range(Nx):
        for j in range(Ny):
            hij = heatmap[i,j]
            if i>0:
                gradientx[i,j] += -f(heatmap[i-1,j] - hij)
                # pas de contrib en y

            if i>0 and j>0:
                gradientx[i,j] += -f(heatmap[i-1,j-1] - hij)
                gradienty[i,j] += -f(heatmap[i-1,j-1] - hij)

            if i>0 and j<Ny-1:
                gradientx[i,j] += -f(heatmap[i-1,j+1] - hij)
                gradienty[i,j] += +f(heatmap[i-1,j+1] - hij) 
 
            if i<Nx-1:
                gradientx[i,j] += +f(heatmap[i+1,j] - hij)
                # pas de contrib en y

            if i<Nx-1 and j>0:
                gradientx[i,j] += +f(heatmap[i+1,j-1] - hij)
                gradienty[i,j] += -f(heatmap[i+1,j-1] - hij)                 

            if i<Nx-1 and j<Ny-1:
                gradientx[i,j] += +f(heatmap[i+1,j+1] - hij)
                gradienty[i,j] += +f(heatmap[i+1,j+1] - hij)                   

            if j>0:
                # pas de contrib en x
                gradienty[i,j] += -f(heatmap[i,j-1] - hij)

            if j<Ny-1:
                # pas de contrib en x
                gradienty[i,j] += +f(heatmap[i,j+1] - hij)

    return gradientx, gradienty


def calcule_gradient_min(heatmap):
    """ Renvoie le vecteur (vx,vy) vers une des cases voisines qui a la plus petite valeur """
    gradientx = np.zeros((Nx, Ny), dtype=float)
    gradienty = np.zeros((Nx, Ny), dtype=float)
    for i in range(Nx):
        for j in range(Ny):
            hij = heatmap[i,j]
            hmin = infini
            gradientx[i,j] = 0
            gradienty[i,j] = 0

            if i>0 and heatmap[i-1,j] < hmin:
                hmin = heatmap[i-1,j]
                gradientx[i,j] = -1
                gradienty[i,j] = 0           

            if i>0 and j>0 and heatmap[i-1,j-1] < hmin:
                hmin = heatmap[i-1,j-1]
                gradientx[i,j] = -1
                gradienty[i,j] = -1
                

            if i>0 and j<Ny-1 and heatmap[i-1,j+1] < hmin:
                hmin = heatmap[i-1,j+1]
                gradientx[i,j] = -1
                gradienty[i,j] = +1
 
            if i<Nx-1 and heatmap[i+1,j] < hmin:
                hmin = heatmap[i+1,j]
                gradientx[i,j] = +1
                gradienty[i,j] = 0

            if i<Nx-1 and j>0 and heatmap[i+1,j-1] < hmin:
                hmin = heatmap[i+1,j-1]
                gradientx[i,j] = +1
                gradienty[i,j] = -1

            if i<Nx-1 and j<Ny-1 and heatmap[i+1,j+1] < hmin:
                hmin = heatmap[i+1,j+1]
                gradientx[i,j] = +1
                gradienty[i,j] = +1            

            if j>0 and heatmap[i,j-1] < hmin:
                hmin = heatmap[i,j-1]
                gradientx[i,j] = 0
                gradienty[i,j] = -1

            if j<Ny-1 and heatmap[i,j+1] < hmin:
                hmin = heatmap[i,j+1]
                gradientx[i,j] = 0
                gradienty[i,j] = +1

    return gradientx, gradienty

# gradient = calcule_gradient(heatmap, f=fonction_decroissante)
# gradient = calcule_gradient(heatmap)
# gradient = calcule_gradient_min(heatmap)
# gradientx, gradienty = gradient

# affichage_terrain(terrain, heatmap=heatmap, gradient=gradient, withcolor=False, withtext=True, withgrille=True, withgradient=True)  # Exemple 1
# affichage_terrain(terrain, heatmap=heatmap, gradient=gradient, withcolor=False, withtext=False, withgrille=False, withgradient=True)  # Exemple 2

#################
### Exemple 1 ###


# affichage_terrain(terrain)

# heatmap = calcule_heatmap(terrain, dist=distance1)
# affichage_terrain(terrain, heatmap=heatmap, withcolor=False, withtext=True, withgrille=True) 

# gradient = calcule_gradient_min(heatmap)
# gradient = calcule_gradient(heatmap, f=fonction_decroissante)
# gradient = calcule_gradient(heatmap)
# affichage_terrain(terrain, heatmap=heatmap, gradient=gradient, withcolor=False, withtext=True, withgrille=True, withgradient=True)  # Exemple 1

#################
### Exemple 2 ###

# affichage_terrain(terrain, withtext=False, withgrille=False)

heatmap = calcule_heatmap(terrain, dist=distance1)
# affichage_terrain(terrain, heatmap=heatmap, withcolor=True, withtext=False, withgrille=False)

# gradient = calcule_gradient_min(heatmap)
# # gradient = calcule_gradient(heatmap, f=fonction_decroissante)
gradient = calcule_gradient(heatmap)
affichage_terrain(terrain, heatmap=heatmap, gradient=gradient, withcolor=False, withtext=False, withgrille=False, withgradient=True)


