# Solutions numérique des équations différentielles
# Intégration des champs de vecteurs ou d'un système différentiel


import numpy as np
import matplotlib.pyplot as plt



# Méthode d'Euler champ de vecteurs
def euler_systeme(f, g, x0, y0, t1, h=0.01):
    liste_x = [x0]
    liste_y = [y0]
    x = x0
    y = y0

    t = 0

    while t < t1:
        x = x + h * f(x,y)
        y = y + h * g(x,y)
        t = t + h

        liste_x.append(x)
        liste_y.append(y)

    return liste_x, liste_y


# Méthode Runge-Kutta d'ordre 2
def rungekutta2_systeme(f, g, x0, y0, t1, h=0.01):
    liste_x = [x0]
    liste_y = [y0]   
    x = x0
    y = y0

    t = 0

    while t < t1:
        k1 = f(x, y)
        l1 = g(x, y)
        k2 = f(x + h*k1, y + h*l1)
        l2 = g(x + h*k1, y + h*l1)

        x = x + h/2*(k1 + k2)
        y = y + h/2*(l1 + l2)

        t = t + h

        liste_x.append(x)
        liste_y.append(y)  

    return liste_x, liste_y



# Exemple 1 : 
def exemple1(t=1, h=0.01, Ny=10):

    f = lambda x,y: y
    g = lambda x,y: -x

    x0 = 0
    t = t
    # y0 = 0.8
    for y0 in np.linspace(0.2, 1, Ny):
        plt.plot(x0, y0, 'ro')
        # liste_x, liste_y = euler_systeme(f, g, x0, y0, t, h)
        # plt.plot(liste_x, liste_y, 'b-', linewidth=3)
        liste_x, liste_y = rungekutta2_systeme(f, g, x0, y0, t, h)
        plt.plot(liste_x, liste_y, 'r-', linewidth=3)

    for x in np.linspace(-1, 1, 20):
        for y in np.linspace(-1, 1, 20):
            vx, vy = f(x, y), g(x,y)
            plt.arrow(x, y, 0.2*vx, 0.2*vy, head_width=0.02, head_length=0.05, fc='gray', ec='gray')

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('equadiff-sys-01.png',dpi=600) 
    plt.show()

exemple1(t = 2, h=0.01, Ny = 5)


# Exemple 2 : 
def exemple2(t=1, h=0.01):

    f = lambda x,y: x - y
    g = lambda x,y: x*y

    x0 = 0.5
    y0 = 0.5

    liste_x, liste_y = rungekutta2_systeme(f, g, x0, y0, t, h)

    plt.plot(x0, y0, 'ro')
    plt.plot(liste_x, liste_y, 'r-', linewidth=3)
    # plt.plot(liste_x, liste_y, 'bo')   

    for x in np.linspace(-1, 1, 20):
        for y in np.linspace(-1, 1, 20):
            vx, vy = f(x, y), g(x,y)
            plt.arrow(x, y, 0.2*vx, 0.2*vy, head_width=0.02, head_length=0.05, fc='gray', ec='gray')

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('equadiff-sys-04.png',dpi=600)
    plt.show()

# exemple2(t = 2.5, h=0.01)