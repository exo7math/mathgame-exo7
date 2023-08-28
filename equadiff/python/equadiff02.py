# Solutions numérique des équations différentielles
# Méthode d'Euler - visualisation


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


# Exemple 1 : y'= 1/2y, y(1) = 1, solution y(x) = sqrt(x)
def exemple1():
    f = lambda x, y: 1/(2*y)    

    x0 = 1
    x1 = 2
    y0 = 1

    h = 0.1
    liste_x1, liste_y1 = euler(f, x0, y0, x1, h)
    plt.plot(liste_x1, liste_y1, 'b', label='Euler n =10')

    # Vraie solution
    X = np.linspace(1, 2, 100)
    Y = np.sqrt(X)
    plt.plot(X, Y, 'r', label='sqrt(x)')

    plt.tight_layout()
    plt.legend()
    # plt.savefig('equadiff-euler-01.png',dpi=600) 
    plt.show()

# exemple1()

# Exemple 2 : y'= 1/2y, y(x0) = y0, solution y(x) = sqrt(x+c)
def exemple2():
    f = lambda x, y: 1/(2*y)    

    x0 = 1
    x1 = 2
    # y0 = 1
    h = 0.01

    for y0 in np.linspace(0.1, 1.2, 20):
        liste_x1, liste_y1 = euler(f, x0, y0, x1, h)
        plt.plot(liste_x1, liste_y1, 'b', label='Euler')

    plt.tight_layout()
    # plt.savefig('equadiff-euler-02.png',dpi=600) 
    plt.show()

# exemple2()


# Exemple 3 : y' = y,  : solution y(x) =exp(x)
def exemple3():
    f = lambda x, y: y   

    x0 = 0
    x1 = 1
    y0 = 1

    h = 0.1
    liste_x1, liste_y1 = euler(f, x0, y0, x1, h)
    plt.plot(liste_x1, liste_y1, 'b', label='Euler n =10')

    h = 0.05
    liste_x1bis, liste_y1bis = euler(f, x0, y0, x1+0.1, h)
    plt.plot(liste_x1bis, liste_y1bis, 'g', label='Euler n=20')

    # Vraie solution
    X = np.linspace(0, 1.1, 100)
    Y = np.exp(X)
    plt.plot(X, Y, 'r', label='exp(x)')

    plt.tight_layout()
    plt.legend()
    # plt.savefig('equadiff-euler-03.png',dpi=600) 
    plt.show()

# exemple3()



# Exemple 4 : parchutiste y' = g - f/m * y^2(t),  y(0)= 0
def exemple4():
    g = 10.0
    m = 60.0
    kf = 1.0
    f = lambda t, y: g - kf/m * y**2

    t0 = 0     # temps initial
    t1 = 15    # temps final
    y0 = 0     # vitesse initiale

    h = 0.01
    liste_x1, liste_y1 = euler(f, t0, y0, t1, h)
    plt.plot(liste_x1, liste_y1, 'b', label='Euler n =10')

    plt.tight_layout()
    # plt.legend()
    # plt.savefig('equadiff-euler-04.png',dpi=600) 
    plt.show()

exemple4()