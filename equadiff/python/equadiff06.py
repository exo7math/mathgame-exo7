# Solutions numérique des équations différentielles
# Mouvement d'un satellite


import numpy as np
import matplotlib.pyplot as plt



# Méthode d'Euler système différentiel x'' = f(x,y) et y'' = g(x,y)
# Système de 2 équations différentielles du 2ème ordre
# Equivalence avec un système de 4 équations du 1er ordre
# x' = xx, xx' = f(x,y), y' = yy, yy' = g(x,y)
# x, y position, xx, yy vitesse, xx', yy' accélération

def euler_systeme_ordre2(f, g, x0, y0, xx0, yy0, t0=0, t1=1, h=0.01):
    liste_x = [x0]
    liste_y = [y0]
    liste_xx = [xx0]
    liste_yy = [yy0]
    x = x0
    y = y0
    xx = xx0
    yy = yy0

    t = t0

    while t < t1:
        newx = x + h * xx
        xx = xx + h * f(x,y)
        x = newx

        newy = y + h * yy
        yy = yy + h * g(x,y)
        y = newy

        t = t + h

        liste_x.append(x)
        liste_y.append(y)
        liste_xx.append(xx)
        liste_yy.append(yy)

    return liste_x, liste_y




# Exemple 1
def exemple1(h=0.01):
    def f(x, y):
        return 0

    def g(x, y):
        return -1

    x0 = 1
    y0 = 1
    xx0 = 0
    yy0 = 0
    t0 = 0
    t1 = 1

    liste_x, liste_y = euler_systeme_ordre2(f, g, x0, y0, xx0, yy0, t0, t1, h)

    plt.plot(liste_x, liste_y, 'r-')
    plt.plot(liste_x, liste_y, 'ro')

    plt.show()

# exemple1(h=0.1)


# Trajectoire d'un satellite
def satellite(t0=0, t1=1, h=0.01):
    MS = 2  # Masse Soleil
    MT = 0.1  # Masses Terre
    # MT = 1
    G = 10  # Constante gravitationnelle
    (xS, yS) = (0, 0)  # Position Soleil
    (xT, yT) = (1, 0)  # Position Terre

    (x0, y0) = (1, 1)  # Position initiale satellite

    (xx0, yy0) = (0, -4)  # Vitesse initiale satellite
    # (xx0, yy0) = (0, 0)  # Vitesse initiale satellite
  
    # Action de la gravité :  force gravité de S + force gravité de T = m * accélération
    # Sur l'axe des x
    def f(x, y):
        return -G*MS*(x-xS)/((x-xS)**2 + (y-yS)**2)**(3/2) - G*MT*(x-xT)/((x-xT)**2 + (y-yT)**2)**(3/2)

    # Sur l'axe des y
    def g(x, y):
        return -G*MS*(y-yS)/((x-xS)**2 + (y-yS)**2)**(3/2) - G*MT*(y-yT)/((x-xT)**2 + (y-yT)**2)**(3/2)

    x0 = 0.644

    for __ in np.arange(0.4, 1, 0.1):

        liste_x, liste_y = euler_systeme_ordre2(f, g, x0, y0, xx0, yy0, t0, t1, h)

        plt.plot(xS, yS, color='orange', marker='o', markersize=10)
        plt.plot(xT, yT, color='blue', marker='o', markersize=10)
        plt.plot(x0, y0, color='red', marker='o', markersize=5)
        plt.plot(liste_x, liste_y, 'r-')

        # plt.plot(liste_x, liste_y, 'ro')


    plt.axis('off')
    plt.xlim(-2, 3)
    plt.ylim(-2, 2)
    plt.tight_layout()
    # plt.savefig('satell6ite-01.png', dpi=600)
    plt.show()

satellite(t1=5, h=0.0001)


