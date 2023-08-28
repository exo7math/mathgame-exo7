# Passage d'un carré à un cercle
# From Analytical Methods for Squaring the Disc
# Chamberlain Fong https://arxiv.org/pdf/1509.06344.pdf



import numpy as np
import matplotlib.pyplot as plt



# Carré [-1,1]x[-1,1] coordonnées (x,y)
# Disque de centre (0,0) et de rayon 1, coordonnées (u,v)

################################################
# Partie A : par les rayons

# Du carré vers le disque
def carre_vers_disque1(x,y):
    invr = 1/np.sqrt(x**2+y**2)
    if x**2 >= y**2:
        u = np.sign(x) * x**2 * invr
        v = np.sign(x) * x*y * invr
    else:
        u = np.sign(y) * x*y * invr
        v = np.sign(y) * y**2 * invr
    return u,v


# Du disque vers le carré
def disque_vers_carre1(u,v):
    r = np.sqrt(u**2+v**2)
    if u**2 >= v**2:
        x = np.sign(u) * r
        y = np.sign(u) * v/u * r
    else:
        x = np.sign(v) * u/v * r
        y = np.sign(v) * r
    return x,y



################################################
# Partie B : par la grille elliptique


def carre_vers_disque2(x,y):
    u = x * np.sqrt(1-y**2/2)
    v = y * np.sqrt(1-x**2/2)
    return u, v

def disque_vers_carre2(u,v):
    x = 1/2 * np.sqrt(2+u**2-v**2 +2*np.sqrt(2)*u) - 1/2 * np.sqrt(2+u**2-v**2 -2*np.sqrt(2)*u)
    y = 1/2 * np.sqrt(2-u**2+v**2 +2*np.sqrt(2)*v) - 1/2 * np.sqrt(2-u**2+v**2 -2*np.sqrt(2)*v)
    return x, y



################################################
# Partie C : affichage des grilles

def affichage1():
    N = 100    # résolution graphique
    n = 10      # nombre de lignes affichées
    X = np.linspace(-1,1,N)
    Y = np.linspace(-1,1,N)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    for y in np.linspace(-1,1,n):
        ax1.plot(X,[y]*N, color='orange')  # lignes horizontales
        U = [carre_vers_disque1(x,y)[0] for x in X]
        V = [carre_vers_disque1(x,y)[1] for x in X]
        ax2.plot(U,V, color='orange')

    for x in np.linspace(-1,1,n):
        ax1.plot([x]*N,Y, color='green')  # lignes verticales
        U = [carre_vers_disque1(x,y)[0] for y in Y]
        V = [carre_vers_disque1(x,y)[1] for y in Y]
        ax2.plot(U,V, color='green')

    ax1.axis('equal')
    ax1.axis([-1.1,1.1,-1.1,1.1])
    ax1.axis('off')
    ax2.axis('equal')
    ax2.axis([-1.1,1.1,-1.1,1.1])
    ax2.axis('off')
    plt.tight_layout()
    # plt.savefig('carre-cercle-01.png', dpi=300)
    plt.show()
    return

# affichage1()


def affichage2():
    N = 400    # résolution graphique
    n = 10      # nombre de lignes affichées
    Theta = np.linspace(0,2*np.pi,N)
    R = np.linspace(0,1,N)


    fig, (ax1, ax2) = plt.subplots(1, 2)
    for theta in np.linspace(0,2*np.pi,n):
        ax1.plot(R*np.cos(theta),R*np.sin(theta), color='purple')  # rayons
        X = [disque_vers_carre1(r*np.cos(theta), r*np.sin(theta))[0] for r in R]
        Y = [disque_vers_carre1(r*np.cos(theta), r*np.sin(theta))[1] for r in R]
        ax2.plot(X,Y, color='purple')

    for r in np.linspace(0,1,n):
        ax1.plot(r*np.cos(Theta),r*np.sin(Theta), color='olive')  # cercles
        X = [disque_vers_carre1(r*np.cos(theta), r*np.sin(theta))[0] for theta in Theta]
        Y = [disque_vers_carre1(r*np.cos(theta), r*np.sin(theta))[1] for theta in Theta]
        ax2.plot(X,Y, color='olive')

    ax1.axis('equal')
    ax1.axis([-1.1,1.1,-1.1,1.1])
    ax1.axis('off')
    ax2.axis('equal')
    ax2.axis([-1.1,1.1,-1.1,1.1])
    ax2.axis('off')
    plt.tight_layout()
    # plt.savefig('carre-cercle-02.png', dpi=300)    
    plt.show()
    return

# affichage2()


def affichage3():
    N = 100    # résolution graphique
    n = 10      # nombre de lignes affichées
    X = np.linspace(-1,1,N)
    Y = np.linspace(-1,1,N)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    for y in np.linspace(-1,1,n):
        ax1.plot(X,[y]*N, color='orange')  # lignes horizontales
        U = [carre_vers_disque2(x,y)[0] for x in X]
        V = [carre_vers_disque2(x,y)[1] for x in X]
        ax2.plot(U,V, color='orange')

    for x in np.linspace(-1,1,n):
        ax1.plot([x]*N,Y, color='green')  # lignes verticales
        U = [carre_vers_disque2(x,y)[0] for y in Y]
        V = [carre_vers_disque2(x,y)[1] for y in Y]
        ax2.plot(U,V, color='green')

    ax1.axis('equal')
    ax1.axis([-1.1,1.1,-1.1,1.1])
    ax1.axis('off')
    ax2.axis('equal')
    ax2.axis([-1.1,1.1,-1.1,1.1])
    ax2.axis('off')
    plt.tight_layout()
    # plt.savefig('carre-cercle-03.png', dpi=300)
    plt.show()
    return

# affichage3()


def affichage4():
    N = 200    # résolution graphique
    n = 10      # nombre de lignes affichées
    Theta = np.linspace(0,2*np.pi,N)
    R = np.linspace(0,1,N)


    fig, (ax1, ax2) = plt.subplots(1, 2)
    for theta in np.linspace(0,2*np.pi,n):
        ax1.plot(R*np.cos(theta),R*np.sin(theta), color='purple')  # rayons
        X = [disque_vers_carre2(r*np.cos(theta), r*np.sin(theta))[0] for r in R]
        Y = [disque_vers_carre2(r*np.cos(theta), r*np.sin(theta))[1] for r in R]
        ax2.plot(X,Y, color='purple')

    for r in np.linspace(0,1,n):
        ax1.plot(r*np.cos(Theta),r*np.sin(Theta), color='olive')  # cercles
        X = [disque_vers_carre2(r*np.cos(theta), r*np.sin(theta))[0] for theta in Theta]
        Y = [disque_vers_carre2(r*np.cos(theta), r*np.sin(theta))[1] for theta in Theta]
        ax2.plot(X,Y, color='olive')

    ax1.axis('equal')
    ax1.axis([-1.1,1.1,-1.1,1.1])
    ax1.axis('off')
    ax2.axis('equal')
    ax2.axis([-1.1,1.1,-1.1,1.1])
    ax2.axis('off')
    plt.tight_layout()
    # plt.savefig('carre-cercle-04.png', dpi=300)
    plt.show()
    return

# affichage4()


# Partie D : affichage des images

import imageio.v3 as imageio

## Fonction qui lit une image, la transforme en un tableau numpy, lui applique une fonction F(x,y) et renvoie l'image transformée.

def transformer_image(F, nom_image):
    f = imageio.imread(nom_image)
    Nx, Ny, Nc = f.shape
    g = 255*np.ones( (Nx,Ny,Nc) )
    # C'est mieux de parcourir sur l'image de sortie
    # pour éviter les pb de pixellisation
    for i in range(Nx):     
        for j in range(Ny):
            x, y = 2*i/Nx-1, 2*j/Ny-1            
            u, v = F(x,y)
            ii, jj = Nx*(u+1)/2, Ny*(v+1)/2
            if (not np.isnan(ii)) and (not np.isnan(jj)):
                ii, jj = int(ii), int(jj)
            if ii >= 0 and ii < f.shape[0] and jj >= 0 and jj < f.shape[1]:
                g[i,j] = f[ii,jj]
    g = np.clip(g,0,255)   # limite les valeurs entre 0 et 255
    g = g.astype(np.uint8)  # conversion en entier

    # Affichage de l'image
    fig = plt.figure(figsize = (10,5))
    ax = plt.subplot(1,2,1)
    ax.set_title("Image originale")
    # fig, ax = subplots(figsize=(18, 2))
    ax.axis("off")
    ax.imshow(f, cmap='gray')

    ax = plt.subplot(1,2,2)
    ax.set_title("Image transformée")
    ax.axis("off")
    plt.imshow(g, cmap='gray')

    plt.tight_layout()
    plt.show()

    # Sauvegarde de l'image   
    # imageio.imwrite('image_disque_apres_1.png', g)

    return g

# Il faut en fait appliquer la transformation inverse de ce qu'on veut faire
# car c'est du texturage inverse qu'on effectue ici.

# transformer_image(disque_vers_carre1, 'image_carre_avant.png')
# transformer_image(carre_vers_disque1, 'image_disque_avant.png')