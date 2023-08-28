# Ondes

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

### Partie A
### Ondes 1D



def ondes1D(x, t, A, mylambda, T):
    """Renvoie la valeur de la fonction de la forme
    A * sin(2*pi*x/mylambda - 2*pi/T *t) à l'instant t
    pour une onde de longueur d'onde mylambda et d'une période T
    """
    return A * np.sin(2*np.pi/mylambda * x - 2*np.pi/T * t)

def affiche_ondes1D():
    """Affiche les ondes 1D pour différentes valeurs de t"""
    mylambda = 2*np.pi
    T = 1

    for t in np.linspace(0, 0.3, 3):
        X = np.linspace(0, 6*np.pi, 200)
        Y = ondes1D(X, t, 5, mylambda, T)
        plt.plot(X, Y, color='blue')

    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('ondes1D-1.png', dpi=300)
    plt.show()
    return

# affiche_ondes1D()



def film_ondes1D(Tmax=2, dt=0.01, A=1, mylambda=2*np.pi, T=1):
    """Affiche les ondes 1D pour différentes valeurs de t"""

    for t in np.arange(0, Tmax, dt):
        plt.cla()
        X = np.linspace(0, 6*np.pi, 100)
        Y = ondes1D(X, t, 1, mylambda, T)
        plt.plot(X, Y, color='blue')
        plt.pause(0.01)


    # plt.axis('equal')
    plt.tight_layout()
    plt.show()
    return

# film_ondes1D()

def superposition_ondes1D():
    """Affiche les ondes 1D pour différentes valeurs de t"""
    mylambda1 = 2*np.pi
    T1 = 3
    t1 = 0
    A1 = 5

    mylambda2 = 2*np.pi/3
    T2 = 2
    t2 = 0.3
    A2 = 3

    fig, (ax1, ax2) = plt.subplots(2)



    X = np.linspace(0, 6*np.pi, 200)
    Y1 = ondes1D(X, t1, A1, mylambda1, T1)
    ax1.plot(X, Y1, color='blue')

    Y2 = ondes1D(X, t2, A2, mylambda2, T2)
    ax1.plot(X, Y2, color='green')

    Y3 = Y1 + Y2
    ax2.plot(X, Y3, color='red')

    # ax2.set_ylim(-5,5)
    # plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('ondes_superposition.png', dpi=300)
    plt.show()
    return

# superposition_ondes1D()




### Partie B
### Ondes 2D

def ondes2Dradial(r, t, A, mylambda, T):
    return A * np.sin(2*np.pi/mylambda*r - 2*np.pi/T*t)


def ondes2D(x, y, x0, y0, t=0, A=5, mylambda=np.pi, T=1):
    """Renvoie la valeur de la fonction de la forme
    1/r * A * sin(2*pi*x/mylambda - T*t) à l'instant t
    pour une onde radiale de longueur d'onde mylambda et d'une période T
    """
    r = np.sqrt((x-x0)**2 + (y-y0)**2)
    invr = np.minimum(1,1/r)  # Pour éviter les divisions par 0

    return invr*ondes2Dradial(r, t, A, mylambda, T)


def affiche_ondes2D():
    """Affiche les ondes 2D pour différentes valeurs de t"""
    mylambda = 2*np.pi
    T = 1

    X = np.linspace(-20, 20, 200)
    Y = np.linspace(-20, 20, 200)
    X, Y = np.meshgrid(X, Y)
    # Z = ondes2D(X, Y, 0, 0)  # une seule onde 
    Z = ondes2D(X, Y, -5, 0) + ondes2D(X, Y, 5, 0) # superposition deux ondes

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    surface = ax.plot_surface(X, Y, Z,cmap=cm.inferno,linewidth=0, antialiased=False, rstride=1, cstride=1)

    ax.axis('off')
    ax.set_box_aspect((np.ptp(X), np.ptp(Y), np.ptp(Z)))
    ax.view_init( azim=50., elev=30.)
    # ax.set_box_aspect((1, 1, 1))
    plt.tight_layout()

    # plt.savefig('ondes2D-3.png', dpi=600)
    plt.show()

    return

affiche_ondes2D()


def affiche_tranche_ondes2D():
    """Affiche une tranche d'une onde 2D"""
    # mylambda = 2*np.pi
    # T = 1

    
    X = np.linspace(-3*np.pi, 3*np.pi, 200)
    Y = ondes2D(X, 0, 0, 0, t=0.2)
    plt.plot(X, Y, color='blue')

    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('ondes2D-1.png', dpi=300)
    plt.show()
    return

# affiche_tranche_ondes2D()


def film_ondes2D(Tmax=10, dt=0.05, A=1, mylambda=2*np.pi, T=1):
    """Affiche les ondes 2D pour différentes valeurs de t"""

    X = np.linspace(-20, 20, 100)
    Y = np.linspace(-20, 20, 100)
    X, Y = np.meshgrid(X, Y)

    fig = plt.figure()
    ax = fig.gca(projection='3d')


    for t in np.arange(0, T, dt):
        ax.cla()
        ax.set_xlim(-20, 20)        
        ax.set_ylim(-20, 20)
        ax.set_zlim(-10,10)
        Z = ondes2D(X, Y, -5, 0, t) + ondes2D(X, Y, 5, 0, t)
        ax.set_box_aspect((np.ptp(X), np.ptp(Y), np.ptp(Z)))
        ax.axis('off')
        surface = ax.plot_surface(X, Y, Z,cmap=cm.inferno,linewidth=0, antialiased=False, rstride=2, cstride=2)
        plt.pause(0.01)

    
    
    plt.tight_layout()
    plt.show()
    return

# film_ondes2D()