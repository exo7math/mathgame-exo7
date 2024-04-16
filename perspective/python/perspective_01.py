##### Mathgame #####
### Perspective ###

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



##### Objets à afficher ######

### Cube ###
# Un objet est une liste d'arêtes
P1, P2, P3, P4 = (0,0,0), (1,0,0), (1,1,0), (0,1,0)
P5, P6, P7, P8 = (0,0,1), (1,0,1), (1,1,1), (0,1,1)

cube = [ [P1,P2], [P2,P3], [P3,P4], [P4,P1], [P5,P6], [P6,P7], [P7,P8], [P8,P5], [P1,P5], [P2,P6], [P3,P7], [P4,P8] ]


### Grille horizontale sur (z=0)
N = 5
grille_horizontale = []
for i in range(-N,N+1):
    grille_horizontale.append([(i,-N,0),(i,N,0)])
    grille_horizontale.append([(-N,i,0),(N,i,0)])


### Grille verticale sur (x=3)
N = 5
grille_verticale = []
for i in range(-N,N+1):
    grille_verticale.append([(3,i,-N),(3,i,N)])
    grille_verticale.append([(3,-N,i),(3,N,i)])



##### Outils standards ######

def affichage_3d_standard(objet):
    """ Affichage de l'objet 3D par matplotlib """

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # ax = plt.axes(projection='3d', proj_type = 'ortho')
    ax.set_xlabel('axe x')
    ax.set_ylabel('axe y')
    ax.set_zlabel('axe z')
    ax.view_init(15, -120)

    for P, Q in objet:
        ax.plot([P[0],Q[0]],[P[1],Q[1]],[P[2],Q[2]], color='red')
    plt.tight_layout()
    # plt.savefig('nomfichier.png')
    plt.show()

    return

# Test
# affichage_3d_standard(cube)
# affichage_3d_standard(grille_horizontale)
# affichage_3d_standard(grille_verticale)

def translation_objet(objet,vecteur):
    """ Translation """
    vx, vy, vz = vecteur
    new_objet = []
    for P, Q in objet:
        PP = (P[0]+vx, P[1]+vy, P[2]+vz)
        QQ = (Q[0]+vx, Q[1]+vy, Q[2]+vz)
        new_objet.append([PP,QQ])

    return new_objet

new_cube = translation_objet(cube,(2,2,3))
test_objets = grille_horizontale + grille_verticale + translation_objet(cube,(0,1,2))
# affichage_3d_standard(test_objets)  


def rotation(x,y,z,axe,angle):
    """ Rotation selon un des axes """

    if axe == 'x':
        X = x
        Y = np.cos(angle)*y - np.sin(angle)*z
        Z = np.sin(angle)*y + np.cos(angle)*z

    if axe == 'y':
        X = np.cos(angle)*x + np.sin(angle)*z
        Y = y
        Z = -np.sin(angle)*x + np.cos(angle)*z

    if axe == 'z':
        X = np.cos(angle)*x - np.sin(angle)*y
        Y = np.sin(angle)*x + np.cos(angle)*y
        Z = z

    return (X,Y,Z)


def rotation_objet(objet,axe,angle):
    """ Rotation selon un des axes """

    new_objet = []
    for P, Q in objet:
        PP = rotation(*P,axe,angle)
        QQ = rotation(*Q,axe,angle)
        new_objet.append([PP,QQ])
    return new_objet

cube2 = translation_objet(cube,(2,2,3))
cube3 = rotation_objet(cube2,'z',np.pi/4)

cube_cours = rotation_objet(cube,'z',np.pi/5)
cube_cours = rotation_objet(cube_cours,'y',-np.pi/6)
cube_cours = translation_objet(cube_cours,(3,0,0))

# affichage_3d_standard(cube_cours)

# Farandoles de cubes
cube_init = translation_objet(cube,(3,-0.5,-0.5))
des_cubes = []
for i in range(10):
    my_cube = rotation_objet(cube_init,'x',i*np.pi/10)
    my_cube = rotation_objet(my_cube,'z',i*np.pi/8)
    des_cubes += my_cube

# affichage_3d_standard(des_cubes)  


test_objets = grille_horizontale + grille_verticale + translation_objet(cube,(0,1,2))
# affichage_3d_standard(test_objets)  
##### Perspective linéaire #####

def perspective_lineaire(P,C):
    """ Calcule l'image du point P sur le plan (Oxz) c-à-d (y=0), par la persepective linéaire centrée en C """
    x, y, z = P
    xc, yc, zc = C

    if x == xc:
        return (+inf,+inf,0)

    k = -xc/(x-xc)
    X = k*(y-yc) + yc
    Y = k*(z-zc) + zc

    return (X,Y)

# Test
# f = 5.5        # focale
# C = (0,f,0) # centre
# P = (1,1,1)  # point
# print(perspective_lineaire(P,C))    



def affichage_3d_lineaire(objet,C):
    """ Affichage de l'objet par perspecive linéaire de centre C sur (Oxz) """

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    ax.set_xlabel('axe x')
    ax.set_ylabel('axe y')

    # Surface
    for P, Q in objet:
        PP = perspective_lineaire(P,C)
        QQ = perspective_lineaire(Q,C)

        ax.plot([PP[0],QQ[0]], [PP[1], QQ[1]], color='blue')
    plt.tight_layout()
    # plt.savefig('nomfichier.png')
    plt.show()

    return

# C = (5,-5.5,2)
# affichage_3d_lineaire(cube,C)
# affichage_3d_lineaire(grille_horizontale,C)
# affichage_3d_lineaire(grille_verticale,C)
# affichage_3d_lineaire(test_objets,C)

# Pour tikz cours
mycube = translation_objet(cube,(3,2.5,1.5))
# print(mycube)
# C = (7,3,3)
# affichage_3d_lineaire(mycube,C)
# for P in [P1,P2,P3,P4,P5,P6,P7,P8]:
#     PP = (P[0]+3, P[1]+2.5, P[2]+1.5)
#     print(perspective_lineaire(PP,C))



##### Projection orthogonale #####

def projection_orthogonale(x,y,z,phi,mylambda):
    """ Projection orthogonale de (x,y,z) sur le plan orthogonal au vecteur dirigé 
    par latitude phi et longitude lambda """

    M1 = np.matrix([[0, 0, 0], [0, 1, 0], [0, 0, 1]])  # projection sur (Oyz) (donc (x=0))
    M2 = np.matrix([[np.cos(-phi), 0, np.sin(-phi)], [0, 1, 0], [-np.sin(-phi),0,np.cos(-phi)]])  # rotation axe y du plan d'angle -phi
    M3 = np.matrix([[np.cos(-mylambda), -np.sin(-mylambda), 0], [np.sin(-mylambda), np.cos(-mylambda), 0], [0, 0, 1]])  # rotation axe z du plan d'angle -lambda

    M = M1 * M2 * M3

    # print(M)

    vX = np.array([[x],[y],[z]])
    vY = M * vX
    X, Y, Z = vY.item(0), vY.item(1), vY.item(2), 
    return (X,Y,Z)


# Test
myphi = np.pi/4
mylambda = 0
P = (1,1,1)  # point
# print(projection_orthogonale(*P,myphi,mylambda))   


def affichage_3d_orthogonale(objet,phi,mylambda):
    """ Affichage de l'objet par projection orthogonale """

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    ax.set_xlabel('axe x')
    ax.set_ylabel('axe y')

    # Surface
    for P, Q in objet:
        PP = projection_orthogonale(*P,phi,mylambda)
        QQ = projection_orthogonale(*Q,phi,mylambda)

        ax.plot([PP[1],QQ[1]], [PP[2], QQ[2]], color='blue')
    plt.tight_layout()
    # plt.savefig('nomfichier.png')
    plt.show()

    return

# phi, mylambda = np.pi/3, np.pi/4
# affichage_3d_orthogonale(cube,phi,mylambda)
# affichage_3d_orthogonale(grille_horizontale,phi,mylambda)
# affichage_3d_orthogonale(grille_verticale,phi,mylambda)
# affichage_3d_orthogonale(test_objets,phi,mylambda)

# Pour tikz cours
# myphi = np.pi/7
# mylambda = np.pi/6
# mycube = translation_objet(cube,(4,3,2))

myphi = np.pi/10
mylambda = np.pi/10
mycube = translation_objet(cube,(0,0,0))
mycube = rotation_objet(mycube,'x',myphi)
mycube = rotation_objet(mycube,'z',mylambda)
print(mycube)

# affichage_3d_orthogonale(mycube,0,0)

# Un objet est une liste d'arêtes
P1, P2, P3, P4 = (0,0,0), (1,0,0), (1,1,0), (0,1,0)
P5, P6, P7, P8 = (0,0,1), (1,0,1), (1,1,1), (0,1,1)
for P in [P1,P2,P3,P4,P5,P6,P7,P8]:
    PP = (P[0]+1, P[1]+2, P[2]+3)
    PP = rotation(*PP,'x',myphi)
    PP = rotation(*PP,'z',mylambda)
    # PP = projection_orthogonale(*PP,0,0)
    print("  ", PP)



##### Projection parallèle #####

def projection_parallele(x,y,z,alpha,beta,kx,ky,kz):
    """ Projection parallèle de (x,y,z) """

    X = -x*kx*np.sin(alpha) + y*ky*np.sin(beta) + 0
    Y = x*kx*np.cos(alpha) + y*ky*np.cos(beta) + z*kz

    return (X,Y)



def affichage_3d_parallele(objet,alpha,beta,kx,ky,kz):
    """ Affichage de l'objet par projection parallèle """

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    ax.set_xlabel('axe x')
    ax.set_ylabel('axe y')

    # Surface
    for P, Q in objet:
        PP = projection_parallele(*P,alpha,beta,kx,ky,kz)
        QQ = projection_parallele(*Q,alpha,beta,kx,ky,kz)

        ax.plot([PP[0],QQ[0]], [PP[1], QQ[1]], color='blue')
    plt.tight_layout()
    # plt.savefig('nomfichier.png')
    plt.show()

    return

alpha, beta = 3*np.pi/4, 2*np.pi/4
kx, ky, kz = 1, 1, 1
# affichage_3d_parallele(cube,alpha,beta,kx,ky,kz)
# affichage_3d_parallele(grille_horizontale,alpha,beta,kx,ky,kz)
# affichage_3d_parallele(grille_verticale,alpha,beta,kx,ky,kz)
# affichage_3d_parallele(test_objets,alpha,beta,kx,ky,kz)


# Pour tikz cours
# myphi = np.pi/7
# mylambda = np.pi/6
# mycube = translation_objet(cube,(-2,2,-1))
# mycube = rotation_objet(mycube,'x',myphi)
# mycube = rotation_objet(mycube,'z',mylambda)
# print(mycube)

# alpha, beta = 3*np.pi/4, 2*np.pi/4
# kx, ky, kz = 1, 1, 1
# affichage_3d_parallele(mycube,alpha,beta, kx, ky, kz)

# for P in [P1,P2,P3,P4,P5,P6,P7,P8]:
#     PP = (P[0]-2, P[1]+2, P[2]-1)
#     PP = rotation(*PP,'x',myphi)
#     PP = rotation(*PP,'z',mylambda)
#     # print(PP)
#     Q = projection_parallele(*PP,alpha,beta, kx, ky, kz)
#     print(Q)
#     print(PP[0]-Q[0], PP[1]-0, PP[2]-Q[1])



##### Coordonnées cylindrique #####

def coordonnees_cylindrique(x,y,z):
    """ Coord. cartésiennes vers cylindrique """

    r = np.sqrt(x**2+y**2)
    theta = np.arctan2(y,x)

    return (r,theta,z)


def affichage_3d_coordonnees_cylindrique(objet, numpoints=20):
    """ Affichage de l'objet par coordonnées cylindrique (theta,z) """

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    ax.set_xlabel('axe X')
    ax.set_ylabel('axe Y')

    # Surface
    for P,Q in objet:
        x, y, z = P
        xx, yy, zz = Q
        vx = np.linspace(x,xx,numpoints)
        vy = np.linspace(y,yy,numpoints)
        vz = np.linspace(z,zz,numpoints)
        for i in range(numpoints-1):
            PP = coordonnees_cylindrique(vx[i],vy[i],vz[i])
            QQ = coordonnees_cylindrique(vx[i+1],vy[i+1],vz[i+1])
            ax.plot([-PP[1],-QQ[1]], [PP[2], QQ[2]], color='blue')        

    plt.tight_layout()
    # plt.savefig('cube_coordonnees_cylindriques.png', dpi=600)
    plt.show()

    return

affichage_3d_coordonnees_cylindrique(cube_cours,numpoints=100)
# affichage_3d_coordonnees_cylindrique(grille_verticale, numpoints=100)
# affichage_3d_coordonnees_cylindrique(test_objets)
# affichage_3d_coordonnees_cylindrique(des_cubes)



##### Coordonnées sphériques #####

def coordonnees_spheriques(x,y,z):
    """ Coord. cartésiennes vers spheriques (rayon,latitude,longitude) = (r, phi, mylambda)"""

    r = np.sqrt(x**2 + y**2 + z**2)   # rayon
    phi = np.arcsin(z/r)              # latitude
    mylambda = np.arctan2(y,x)        # longitude (note: 'lambda' reservé par Python) 

    return (r,phi,mylambda)


def affichage_3d_coordonnees_spheriques(objet, numpoints=20):
    """ Affichage de l'objet par coordonnées cylindrique (mylambda, phi) """

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    ax.set_xlabel('axe X')
    ax.set_ylabel('axe Y')

    # Surface
    for P,Q in objet:
        x, y, z = P
        xx, yy, zz = Q
        vx = np.linspace(x,xx,numpoints)
        vy = np.linspace(y,yy,numpoints)
        vz = np.linspace(z,zz,numpoints)
        for i in range(numpoints-1):
            PP = coordonnees_spheriques(vx[i],vy[i],vz[i])
            QQ = coordonnees_spheriques(vx[i+1],vy[i+1],vz[i+1])
            ax.plot([-PP[2],-QQ[2]], [PP[1], QQ[1]], color='blue')

    plt.tight_layout()
    # plt.savefig('cube_coordonnees_spheriques.png', dpi=600)
    plt.show()

    return

# affichage_3d_coordonnees_spheriques(cube_cours,numpoints=100)
# affichage_3d_coordonnees_spheriques(grille_verticale,numpoints=100)
# affichage_3d_coordonnees_spheriques(test_objets)
# affichage_3d_coordonnees_spheriques(des_cubes)



##### Projection curviligne cylindrique #####

def projection_curviligne_cylindrique(x,y,z, R=1):
    """ Projection sur un cylindre vertical de rayon R puis sur plan vertical (y=0) """

    r = np.sqrt(x**2+y**2)

    if r == 0:
        X, Y, Z = 0, inf, z
    else:
        X, Y, Z = 0, y*R/r, z
    return X, Y, Z


# # Test
# P = (1,2,1)  # point
# print(projection_curviligne_cylindrique(*P))   

def affichage_3d_projection_curviligne_cylindrique(objet, R=1, numpoints=20):
    """ Affichage de l'objet par projection curviligne cylindrique """

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    ax.set_xlabel('axe X')
    ax.set_ylabel('axe Y')

    # Surface
    for P,Q in objet:
        x, y, z = P
        xx, yy, zz = Q
        vx = np.linspace(x,xx,numpoints)
        vy = np.linspace(y,yy,numpoints)
        vz = np.linspace(z,zz,numpoints)
        for i in range(numpoints-1):
            PP = projection_curviligne_cylindrique(vx[i],vy[i],vz[i],R=R)
            QQ = projection_curviligne_cylindrique(vx[i+1],vy[i+1],vz[i+1],R=R)
            ax.plot([PP[1],QQ[1]], [PP[2], QQ[2]], color='blue')        

    plt.tight_layout()
    # plt.savefig('cube_curviligne_cylindrique.png', dpi=600)   
    plt.show()

    return

# affichage_3d_projection_curviligne_cylindrique(cube_cours,R=2,numpoints=100)
# affichage_3d_projection_curviligne_cylindrique(grille_verticale,R=2,numpoints=100)
# affichage_3d_projection_curviligne_cylindrique(test_objets,R=10)
# affichage_3d_projection_curviligne_cylindrique(des_cubes)


##### Projection curviligne spherique #####

def projection_curviligne_spherique(x,y,z, R=1):
    """ Projection sur un sphere de rayon R puis sur plan vertical (y=0) """

    r = np.sqrt(x**2+y**2+z**2)

    if r == 0:
        X, Y, Z = inf, 0, z
    else:
        X, Y, Z = 0, y*R/r, z*R/r
    return X, Y, Z


# # Test
# P = (1,2,1)  # point
# print(projection_curviligne_spherique(*P))   

def affichage_3d_projection_curviligne_spherique(objet, R=2, numpoints=20):
    """ Affichage de l'objet par projection curviligne spherique"""

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    ax.set_xlabel('axe X')
    ax.set_ylabel('axe Y')

    # Surface
    for P,Q in objet:
        x, y, z = P
        xx, yy, zz = Q
        vx = np.linspace(x,xx,numpoints)
        vy = np.linspace(y,yy,numpoints)
        vz = np.linspace(z,zz,numpoints)
        for i in range(numpoints-1):
            PP = projection_curviligne_spherique(vx[i],vy[i],vz[i],R=R)
            QQ = projection_curviligne_spherique(vx[i+1],vy[i+1],vz[i+1],R=R)
            ax.plot([PP[1],QQ[1]], [PP[2], QQ[2]], color='blue')        

    plt.tight_layout()
    # plt.savefig('cube_curviligne_spherique.png', dpi=600)   
    plt.show()

    return

# affichage_3d_projection_curviligne_spherique(cube_cours,R=2,numpoints=100)
# affichage_3d_projection_curviligne_spherique(grille_verticale,R=2,numpoints=100)
# affichage_3d_projection_curviligne_spherique(test_objets,R=10)
# affichage_3d_projection_curviligne_spherique(des_cubes)



