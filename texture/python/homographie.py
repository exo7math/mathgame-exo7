# Transformer un carré en un quadrilatère : les homographies

import numpy as np
import matplotlib.pyplot as plt

# Partie A : calcul de l'homographie

carre = np.array([[0,0],[1,0],[1,1],[0,1]])
quad = np.array([[2,-1],[4,-1/2],[5,1],[3,2]])

def matrice(quad):
    """ Matrice de transformation de carré en quadrilatère """
    xA, yA, xB, yB, xC, yC, xD, yD = quad.flatten()
    A = np.zeros((8,8))
    A[0,0] = 1
    A[1,3] = 1
    A[2,0] = 1
    A[2,1] = 1
    A[2,6] = -xB
    A[3,3] = 1
    A[3,4] = 1
    A[3,6] = -yB
    A[4,0] = 1
    A[4,1] = 1
    A[4,2] = 1
    A[4,6] = -xC
    A[4,7] = -xC
    A[5,3] = 1
    A[5,4] = 1
    A[5,5] = 1
    A[5,6] = -yC
    A[5,7] = -yC
    A[6,0] = 1
    A[6,2] = 1
    A[6,7] = -xD
    A[7,3] = 1
    A[7,5] = 1
    A[7,7] = -yD
    return A



def homographie(quad):
    """ Renvoie une fonction : l'homographie qui transforme un carré en un quadrilatère """
    A = matrice(quad)
    Ainv = np.linalg.inv(A)                       # inverse de la matrice
    B = quad.flatten()                            # coordonnées du quadrilatère 
    C = np.dot(Ainv, B)                           # coeff de l'homographie
    a0, a1, a2, b0, b1, b2, c1, c2 = C.flatten()  # coeff de l'homographie
    print(C.flatten())
    def Phi(X):
        """ Homographie de carré en quadrilatère """
        x, y = X
        return np.array([(a0 + a1*x + a2*y)/(1 + c1*x + c2*y), (b0 + b1*x + b2*y)/(1 + c1*x + c2*y)])   
    
    return Phi


def homographie_inverse(quad):
    """ Renvoie une fonction : l'homographie qui transforme un quadrilatère en un carré """
    A = matrice(quad)
    Ainv = np.linalg.inv(A)                       # inverse de la matrice
    B = quad.flatten()                           # coordonnées du carré
    C = np.dot(Ainv, B)                           # coeff de l'homographie
    a0, a1, a2, b0, b1, b2, c1, c2 = C.flatten()  # coeff de l'homographie

    def Phiinv(X):
        """ Homographie de quadrilatère en carré """
        u, v = X
        x = (-a0*b2 + a0*c2*v + a2*b0 - a2*v - b0*c2*u + b2*u)/(a1*b2 - a1*c2*v - a2*b1 + a2*c1*v + b1*c2*u - b2*c1*u)
        y = (-a0*b1 + a0*c1*v + a1*b0 - a1*v - b0*c1*u + b1*u)/(-a1*b2 + a1*c2*v + a2*b1 - a2*c1*v - b1*c2*u + b2*c1*u)
        return np.array([x, y])   
    
    return Phiinv

# Test
# Phiinv = homographie_inverse(quad)
# for i in range(4):
    #  print(Phiinv(quad[i]))

# Partie B : affichage du carré et de son image

def affiche(quad):
    """ Affiche le carré et le quadrilatère """
    plt.plot(carre[:,0], carre[:,1], 'o', color = 'r', markersize = 6)
    plt.fill(carre[:,0], carre[:,1], edgecolor = 'r', fill=False, lw=2)


    Phi = homographie(quad)


    for X in carre:
        Y = Phi(X)
        plt.scatter(Y[0], Y[1], color = 'b', s = 40)

    # plt.plot(quad[:,0], quad[:,1], 'o', color = 'b', markersize = 10)
    plt.fill(quad[:,0], quad[:,1], edgecolor = 'b', fill=False, lw=2)

    # Segments verticaux
    cT = np.linspace(0, 1, 8)
    cX = []
    cY = []
    for t in cT:
        X1 = np.array([t, 0])
        Y1 = Phi(X1)
        X2 = np.array([t, 1])
        Y2 = Phi(X2)
        plt.plot([X1[0], X2[0]], [X1[1], X2[1]], color = 'gray', lw=1)
        plt.plot([Y1[0], Y2[0]], [Y1[1], Y2[1]], color = 'gray', lw=1)

    # Segments horizontaux
    cT = np.linspace(0, 1, 8)
    cX = []
    cY = []
    for t in cT:
        X1 = np.array([0, t])
        Y1 = Phi(X1)
        X2 = np.array([1, t])
        Y2 = Phi(X2)
        plt.plot([X1[0], X2[0]], [X1[1], X2[1]], color = 'gray', lw=1)
        plt.plot([Y1[0], Y2[0]], [Y1[1], Y2[1]], color = 'gray', lw=1)
        

    # Cercle
    cT = np.linspace(0, 2*np.pi, 100)
    cX = []
    cY = []
    for t in cT:
        X = np.array([0.5+0.5*np.cos(t), 0.5+0.5*np.sin(t)])
        Y = Phi(X)
        cX.append(X)
        cY.append(Y)
    cX = np.array(cX)
    cY = np.array(cY)
    plt.fill(cX[:,0], cX[:,1], edgecolor = 'r', fill=False, lw=1)
    plt.fill(cY[:,0], cY[:,1], edgecolor = 'b', fill=False, lw=1)

    plt.axis('equal')
    # plt.axis('off')
    plt.tight_layout()
    # plt.savefig('carre-quadrilatere.png', dpi=300)
    plt.show()

quad = np.array([[2,-1],[4,-1/2],[5,1],[3,2]])
affiche(quad)




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
    # imageio.imwrite('image-mur-apres.png', g)

    return g


quad = np.array([[0,0],[1-0.1,0],[1+0.8,1.5],[0+0.05,1.5]])
# affiche(quad)
Phiinv = homographie_inverse(quad)
def Psi(x,y):
    xx, yy = Phiinv([x,y])
    return xx, yy

# transformer_image(Psi, 'image_mur.png')





