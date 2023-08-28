"""Mathgame 

Librairie outils
"""


import numpy as np



###############################
## Opérations sur les vecteurs du plan ##



def produit_scalaire_2d(u, v):
    """ Produit scalaire de deux vecteurs u, v du plan """
    x, y = u
    xx, yy = v
    p = x*xx + y*yy
    return p

def norme_2d(u):
    """ Norme d'un vecteur u du plan """
    x, y = u
    n = np.sqrt(x**2 + y**2)
    return n


###############################
## Opérations sur les vecteurs de l'espace ##


def addition(u, v):
    """ Addition de deux vecteur : u + v  """
    x, y, z = u
    xx, yy, zz = v
    w = x+xx, y+yy, z+zz
    return w 


def oppose(u):
    """ Vecteur -u """
    x, y, z = u
    w = -x, -y, -z
    return v


def multiplication_scalaire(t, u):
    """ Multiplication d'un vecteur u par un scalaire t """
    x, y, z = u
    v = t*x, t*y, t*z
    return v


def vecteur(A, B):
    """ Vecteur vec(AB) défini par deux points c-a-d différence B-A  """
    x, y, z = A
    xx, yy, zz = B
    v = xx-x, yy-y, zz-z
    return v   


def produit_scalaire(u, v):
    """ Produit scalaire de deux vecteurs u, v de l'espace """
    x, y, z = u
    xx, yy, zz = v
    p = x*xx + y*yy + z*zz
    return p


def norme(u):
    """ Norme d'un vecteur u de l'espace """
    x, y, z = u
    n = np.sqrt(x**2 + y**2 + z**2)
    return n

def norme2(u):
    """ Norme au carré d'un vecteur u de l'espace """
    x, y, z = u
    n2 = x**2 + y**2 + z**2
    return n2    


def produit_vectoriel(u, v):
    """ Produit vectoriel de deux vecteur (de l'espace) """
    x, y, z = u
    xx, yy, zz = v
    w = y*zz - yy*z, z*xx - zz*x, x*yy - xx*y
    return w


def produit_mixte(u, v, w):
    """ Produit mixte de trois vecteurs (de l'espace) """
    return produit_scalaire(produit_vectoriel(u,v), w)





###############################
## Changement de coordonnées ##


##### Coordonnées plaires #####

def coordonnees_polaires(x, y):
    """ Coord. cartésiennes vers polaires """

    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)

    return (r, theta)


##### Coordonnées cylindrique #####

def coordonnees_cylindrique(x, y, z):
    """ Coord. cartésiennes vers cylindrique """

    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)

    return (r, theta, z)


##### Coordonnées sphériques #####

# note: nom 'lambda' reservé par Python

def coordonnees_spheriques(x, y, z):
    """ Coord. cartésiennes vers spheriques (rayon,latitude,longitude) """

    r = np.sqrt(x**2 + y**2 + z**2)   # rayon
    phi = np.arcsin(z/r)              # latitude
    mylambda = np.arctan2(y, x)       # longitude (note: 'lambda' reservé par Python) 

    return (r, phi, mylambda)
