# Interpolation bilineaire


import numpy as np
import matplotlib.pyplot as plt

# Une fonction valeur (par exemple une couleur)
def F(x,y):
    val = x**2+y**2
    return val

# Interpolation bilinéaire
def interpolation_bilineaire(x, y, F):
    """ Interpolation bilineaire de la fonction F en (x,y) """
    x1 = np.floor(x)
    x2 = x1+1
    y1 = np.floor(y)
    y2 = y1+1

    v11 = F(x1,y1)
    v12 = F(x1,y2)
    v21 = F(x2,y1)
    v22 = F(x2,y2)

    xx = x-x1
    yy = y-y1
    
    val = (1-xx)*(1-yy)*v11 + (1-xx)*yy*v12 + xx*(1-yy)*v21 + xx*yy*v22
    return val

# Interpolation linéaire
def interpolation_lineaire(t, f):
    """ Interpolation linéaire de la fonction f en t """
    t1 = np.floor(t)
    t2 = t1+1
    tt = t-t1
    val = (1-tt)*f(t1) + tt*f(t2)
    return val


def agrandissement(tab):
    """ Agrandissement x2 d'une image (Nx,Ny) par interpolation bilineaire """
    
    print(tab.shape)
    Nx, Ny = tab.shape


    # Fonction qui correspond à la valeur d'un tableau après homothétie de rapport 2
    def F(x,y):
        return tab[int(x),int(y)]
    
    bitab = np.zeros((2*Nx,2*Ny))
    for i in range(2*Nx-1):
        for j in range(2*Ny-1):
            x = i/2-1/4
            y = j/2-1/4
            x = max(0, x)
            y = max(0, y)
            bitab[i,j] = interpolation_bilineaire(x, y, F)

    # Problèmes de bords
    i = 2*Nx-1
    x = i/2-1/4
    for j in range(2*Ny-1):
        y = j/2-1/4
        y = max(0, y)
        bitab[i,j] = interpolation_lineaire(y, lambda t: F(x,t))

    j = 2*Ny-1
    y = j/2-1/4
    for i in range(2*Nx-1):
        x = i/2-1/4
        x = max(0, x)
        bitab[i,j] = interpolation_lineaire(x, lambda t: F(t,y))


    # Coin en haut à droite
    bitab[2*Nx-1,2*Ny-1] = tab[Nx-1,Ny-1]

    return bitab


def exemple1():
    tab = np.array([[0.0,0.25],[0.50,0.75]])
    print(tab)
    bitab = agrandissement(tab)

    # Affichage sous forme d'image noir et blanc
    # Affichage une ligne 2 colonnes
    ax = plt.subplot(1,2,1)
    ax.imshow(1-tab, cmap='gray', interpolation='none', origin='lower')
    ax.axis('off')
    ax.set_title("Image originale")
    ax = plt.subplot(1,2,2)
    ax.imshow(1-bitab, cmap='gray', interpolation='none', origin='lower')
    ax.axis('off')
    ax.set_title("Image interpolée")
    plt.tight_layout(pad=5.0)
    plt.savefig('interpolation_bilineaire_1.png', dpi=300)
    plt.show()
    return

# exemple1()

import imageio.v3 as imageio

def exemple2(nom_image):

    tab = imageio.imread(nom_image)
    # Conversion en niveau de gris
    tab = np.dot(tab[...,:3], [0.299, 0.587, 0.114])
    # Selection d'un zone carrée
    tab = tab[275:325,300:350]

    bitab = agrandissement(tab)
    bitab = np.clip(bitab,0,255)   # limite les valeurs entre 0 et 255
    bitab = bitab.astype(np.uint8)  # conversion en entier

    # Affichage sous forme d'image noir et blanc
    # Affichage une ligne 2 colonnes
    ax = plt.subplot(1,2,1)
    ax.imshow(tab, cmap='gray', interpolation='none', origin='upper')
    ax.axis('off')
    ax.set_title("Image originale")
    ax = plt.subplot(1,2,2)
    ax.imshow(bitab, cmap='gray', interpolation='none', origin='upper')
    ax.axis('off')
    ax.set_title("Image interpolée")
    plt.tight_layout(pad=5.0)
    # plt.savefig('interpolation_bilineaire_2.png', dpi=300)
    plt.show()
    return

# exemple2("image_maison.jpg")
