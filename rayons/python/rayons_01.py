##### Mathgame #####
### Lancer de rayons ###

import numpy as np

# import sys
# sys.path.append('...')
from outils_mathgame import *

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

#######################################
## Lancer de rayon sur un plan/triangle

def intersection_plan(S, v, A, B, C):
    """ Calcule l'intersection du rayon S + tv avec le plan (ABC). Renvoie t et coord. alpha, beta """
    u = vecteur(A, B)
    uu = vecteur(A, C)
    n = produit_vectoriel(u, uu)  # vecteur orthogonal au plan

    p = produit_scalaire(v, n)
    if p == 0:  # pas d'intersection
        return None
    else:
        t = produit_scalaire(vecteur(S, A), n) / p
        alpha = - produit_mixte(vecteur(S, A), vecteur(A, C), v) / p
        beta = - produit_mixte(vecteur(A, B), vecteur(S, A), n) / p
        return t, alpha, beta


def intersection_triangle(S, v, A, B, C):
    """ Calcule l'intersection du rayon S + tv avec le triangle (ABC). Renvoie t et coord. alpha, beta """
    
    inter = intersection_plan(S, v, A, B, C)
    if not inter:     # Pas d'intersection avec le plan
        return None
    else:               
        t, alpha, beta = inter
        if (t >= 0) and (alpha >= 0) and (beta >=0) and (alpha+beta <= 1):
            return inter   # intersection dans le triangle
        else:              # intersection en dehors du triangle
            return None 



def affichage_triangle(S, v, A, B, C):
    """ Affichage de l'intersection rayon avec triangle """

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # ax = plt.axes(projection='3d', proj_type = 'ortho')
    ax.set_xlabel('axe x')
    ax.set_ylabel('axe y')
    ax.set_zlabel('axe z')
    ax.view_init(15, -120)


    ax.scatter(*S, color = 'green')     # origine du rayon
    ax.text(*S, "S")    

    ax.quiver(*S, *v, color = 'green')  # vecteur 
    ax.scatter(*A, color = 'blue')    # sommets du triangle
    ax.scatter(*B, color = 'blue')
    ax.scatter(*C, color = 'blue') 
    ax.text(*A, "A")
    ax.text(*B, "B")    
    ax.text(*C, "C")    

    ax.plot([A[0],B[0],C[0],A[0]], [A[1],B[1],C[1],A[1]],  [A[2],B[2],C[2],A[2]], color = 'blue')


    lx, ly, lz = [A[0],B[0],C[0]], [A[1],B[1],C[1]], [A[2],B[2],C[2]]
    verts = [list(zip(lx,ly,lz))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.2, color='blue'))
 
    inter = intersection_plan(S, v, A, B, C)
    if inter:
        t, alpha, beta = inter 
        P = addition(S, multiplication_scalaire(t, v))  # P = S + t*v

        if (t >= 0) and (alpha >= 0) and (beta >=0) and (alpha+beta <= 1):
          ax.scatter(*P, color = 'red')
          ax.text(*P, "P in")
        else:
          ax.scatter(*P, color = 'red')
          ax.text(*P, "P out")              

        ax.plot([S[0],P[0]], [S[1],P[1]], [S[2],P[2]], color = 'red', lw=0.5)  # vecteur 


        print(inter) 

    plt.tight_layout()
    # plt.savefig('nomfichier.png')
    plt.show()

    return


# Test
S = (0, 0, 0)
v = (1, 1/2, 1)
A = (1, 2, 3)
B = (1, 0, 2)
C = (3, 1, 1)

# affichage_triangle(S, v, A, B, C)


#######################################
## Lancer de rayon sur une sphère



def intersection_sphere(S, v, O, R):
    """ Calcule l'intersection du rayon S + tv avec une sphère centrée en O de rayon R """

    vecSO = vecteur(S,O)
    d2 = norme2(vecSO) - produit_scalaire(vecSO, v)**2 / norme2(v)

    if R**2 - d2 >= 0:  # intersection existe
        tH = produit_scalaire(vecSO, v) / norme2(v)
        h = np.sqrt(R**2 - d2)
        n = norme(v)
        t1 = tH - h/n
        t2 = tH + h/n
        return t1, t2, tH
    else:
        return None



def affichage_sphere(S, v, O, R):
    """ Affichage de l'intersection rayon avec sphère """

    fig = plt.figure()
    # ax = plt.axes(projection='3d')
    ax = plt.axes(projection='3d', proj_type = 'ortho')
    ax.set_xlabel('axe x')
    ax.set_ylabel('axe y')
    ax.set_zlabel('axe z')
    ax.view_init(15, -120)


    ax.scatter(*S, color = 'green')     # origine du rayon
    ax.text(*S, "S")    
    ax.quiver(*S, *v, color = 'green')  # vecteur 
    ax.scatter(*O, color = 'blue')    # centre de la sphère
    ax.text(*O, "O")

    # Sphere
    uu, vv = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
    x = O[0] + R*np.cos(uu)*np.sin(vv)
    y = O[1] + R*np.sin(uu)*np.sin(vv)
    z = O[2] + R*np.cos(vv)
    # ax.plot_wireframe(x, y, z, color="r")
    ax.plot_surface(x, y, z, linewidth=0.0, cstride=1, rstride=1, alpha=0.5)
 
    inter = intersection_sphere(S, v, O, R)

    if inter:
        t1, t2, tH = inter 
        P1 = addition(S, multiplication_scalaire(t1, v))  # P = S + t*v
        P2 = addition(S, multiplication_scalaire(t2, v))
        H = addition(S, multiplication_scalaire(tH, v))

        ax.scatter(*P1, color = 'red')
        ax.text(*P1, "P1")

        ax.scatter(*P2, color = 'red')
        ax.text(*P2, "P2")

        ax.scatter(*H, color = 'blue')
        ax.text(*H, "H")
           
        ax.plot([S[0],P1[0]], [S[1],P1[1]], [S[2],P1[2]], color = 'red', lw=0.5)
        ax.plot([S[0],P2[0]], [S[1],P2[1]], [S[2],P2[2]], color = 'red', lw=0.5)
        ax.plot([O[0],H[0]], [O[1],H[1]], [O[2],H[2]], color = 'blue', lw=0.5)

        print(inter) 

    plt.tight_layout()
    # plt.savefig('nomfichier.png')
    plt.show()

    return


# Test
S = (0, 0, 0)
v = (1, 1, 1)
O = (1, 2, 3)
R = 2

# affichage_sphere(S, v, O, R)




#######################################
## Lancer de rayon sur une boite

def intersection_boite(S, v, A, B):
    """ Calcule l'intersection du rayon S + tv avec une boite délmitée par deux sommets opposés A et B """

    tin = -np.inf
    tout = +np.inf

    xS, yS, zS = S
    xv, yv, zv = v
    xA, yA, zA = A
    xB, yB, zB = B

    if xv != 0:
        txA = (xA - xS)/xv
        txB = (xB - xS)/xv

        tin = max(tin, min(txA, txB))
        tout = min(tout, max(txA, txB))

    if yv != 0:
        tyA = (yA - yS)/yv
        tyB = (yB - yS)/yv

        tin = max(tin, min(tyA, tyB))
        tout = min(tout, max(tyA, tyB))

    if zv != 0:
        tzA = (zA - zS)/zv
        tzB = (zB - zS)/zv

        tin = max(tin, min(tzA, tzB))
        tout = min(tout, max(tzA, tzB))  

    if tin <= tout:
        return tin, tout
    else:
        return None           



def affichage_boite(S, v, A, B):
    """ Affichage de l'intersection rayon avec boite """

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # ax = plt.axes(projection='3d', proj_type = 'ortho')
    ax.set_xlabel('axe x')
    ax.set_ylabel('axe y')
    ax.set_zlabel('axe z')
    ax.view_init(15, -120)


    ax.scatter(*S, color = 'green')     # origine du rayon
    ax.text(*S, "S")    
    ax.quiver(*S, *v, color = 'green')  # vecteur 

    # Boite
    xA, yA, zA = A
    xB, yB, zB = B   

    ax.scatter(*A, color = 'blue')    # sommets du triangle
    ax.scatter(*B, color = 'blue')
    ax.text(*A, "A")
    ax.text(*B, "B") 

    # Les 6 faces à la main !!! What a shame!
    lx, ly, lz = [xA,xB,xB,xA], [yA,yA,yB,yB], [zA,zA,zA,zA]
    verts = [list(zip(lx,ly,lz))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.2, color='red'))

    lx, ly, lz = [xA,xB,xB,xA], [yA,yA,yB,yB], [zB,zB,zB,zB]
    verts = [list(zip(lx,ly,lz))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.2, color='red'))

    lx, ly, lz = [xA,xB,xB,xA], [yA,yA,yA,yA], [zA,zA,zB,zB]
    verts = [list(zip(lx,ly,lz))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.2, color='green'))

    lx, ly, lz = [xA,xB,xB,xA], [yB,yB,yB,yB], [zA,zA,zB,zB]
    verts = [list(zip(lx,ly,lz))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.2, color='green'))

    lx, ly, lz = [xA,xA,xA,xA], [yA,yB,yB,yA], [zA,zA,zB,zB]
    verts = [list(zip(lx,ly,lz))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.2, color='blue'))

    lx, ly, lz = [xB,xB,xB,xB], [yA,yB,yB,yA], [zA,zA,zB,zB]
    verts = [list(zip(lx,ly,lz))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.2, color='blue'))
 
    inter = intersection_boite(S, v, A, B)

    if inter:
        t1, t2 = inter 
        P1 = addition(S, multiplication_scalaire(t1, v))  # P = S + t*v
        P2 = addition(S, multiplication_scalaire(t2, v))

        ax.scatter(*P1, color = 'red')
        ax.text(*P1, "Pin")

        ax.scatter(*P2, color = 'red')
        ax.text(*P2, "Pout")

           
        ax.plot([S[0],P1[0]], [S[1],P1[1]], [S[2],P1[2]], color = 'red', lw=0.5)
        ax.plot([S[0],P2[0]], [S[1],P2[1]], [S[2],P2[2]], color = 'red', lw=0.5)

        print(inter) 

    plt.tight_layout()
    # plt.savefig('nomfichier.png')
    plt.show()

    return


# Test
S = (0, 0, 0)
v = (1, 1, 2)
A = (1, 2, 1)
B = (4, 5, 6)
affichage_boite(S, v, A, B)