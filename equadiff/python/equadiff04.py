# Solutions numérique des équations différentielles
# Comparaison graphique des méthodes d'Euler et de Runge-Kutta


import numpy as np
import matplotlib.pyplot as plt

# Méthode d'Euler
def euler(f, x0, y0, x1, h):
    liste_x = [x0]
    liste_y = [y0]   
    x = x0
    y = y0

    while x < x1:
        y = y + h * f(x, y)
        x = x + h
        liste_x.append(x)
        liste_y.append(y)  

    return liste_x, liste_y


# Méthode Runge-Kutta d'ordre 2
def rungekutta2(f, x0, y0, x1, h):
    liste_x = [x0]
    liste_y = [y0]   
    x = x0
    y = y0

    while x < x1:
        k1 = f(x, y)
        k2 = f(x + h, y + k1*h)
        y = y + h/2 * (k1 + k2)   
        x = x + h
        liste_x.append(x)
        liste_y.append(y)  

    return liste_x, liste_y


# Méthode de Runge-Kutta d'ordre 4
def rungekutta4(f, x0, y0, x1, h):
    liste_x = [x0]
    liste_y = [y0]     
    x = x0
    y = y0
    while x < x1:
        k1 = f(x, y)
        k2 = f(x + h/2, y + k1*h/2)
        k3 = f(x + h/2, y + k2*h/2)
        k4 = f(x + h, y + k3*h)
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        liste_x.append(x)
        liste_y.append(y)
    return liste_x, liste_y
    

# Exemple 1 : y'= 1/2y, y(1) = 1, solution y(x) = sqrt(x)
def exemple1():
    f = lambda x, y: 1/(2*y)    

    x0 = 1
    x1 = 2
    y0 = 1

    h = 0.1
    liste_x1, liste_y1 = euler(f, x0, y0, x1, h)
    plt.plot(liste_x1, liste_y1, 'b', label='Euler n =10')

    # h = 0.05
    # liste_x1bis, liste_y1bis = euler(f, x0, y0, x1+0.1, h)
    # plt.plot(liste_x1bis, liste_y1bis, 'g', label='Euler n=20')

    liste_x2, liste_y2 = rungekutta2(f, x0, y0, x1, h)
    liste_x4, liste_y4 = rungekutta4(f, x0, y0, x1, h)

    # plt.plot(liste_x2, liste_y2 , 'g')
    # plt.plot(liste_x4, liste_y4, 'b')
    # plt.plot(liste_x1, y0*np.exp(liste_x1), 'r' )

    # Vraie solution
    X = np.linspace(1, 2, 100)
    Y = np.sqrt(X)
    plt.plot(X, Y, 'r', label='sqrt(x)')

    plt.tight_layout()
    plt.legend()
    # plt.savefig('equadiff-euler-01.png',dpi=600) 
    plt.show()

# exemple1()


# Exemple 2 : y' = y,  : solution y(x) =exp(x)
def exemple2():
    f = lambda x, y: y   

    x0 = 0
    x1 = 1
    y0 = 1

    h = 0.1
    liste_x1, liste_y1 = euler(f, x0, y0, x1, h)

    liste_x2, liste_y2 = rungekutta2(f, x0, y0, x1, h)
    liste_x4, liste_y4 = rungekutta4(f, x0, y0, x1, h)

    plt.plot(liste_x1, liste_y1, 'b', label='Euler')
    plt.plot(liste_x2, liste_y2 , 'g', label='RK2')
    plt.plot(liste_x4, liste_y4, 'black', label='RK4')

    # Vraie solution
    X = np.linspace(0, 1.1, 100)
    Y = np.exp(X)
    plt.plot(X, Y, 'r', label='exp(x)')

    plt.tight_layout()
    plt.legend()
    plt.savefig('equadiff-euler-05.png',dpi=600) 
    plt.show()

exemple2()


