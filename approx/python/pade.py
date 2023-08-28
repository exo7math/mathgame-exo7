# Approximant de Padé

import matplotlib.pyplot as plt
import numpy as np

# Affiche le graphe de la fonction f sur [a,b] avec N points
def trace(f, a, b, N=100, color='blue', label=''):
    list_x, list_y = [], []
    for x in np.linspace(a, b, N):
        list_x.append(x)
        list_y.append(f(x))
    plt.plot(list_x, list_y, color=color, label=label)
    return

# Exemple Padé pour f = exp(x)
def exemple1():
    f = lambda x: np.exp(x)
    trace(f, -2, 3, color='red', label='f(x) = exp(x)')

    g4 = lambda x: 1 + x + 1/2*x**2 + 1/6*x**3 + 1/24*x**4  # Dl ordre 4
    trace(g4, -2, 3.3, color='green', label="DL d'ordre 4")

    p22 = lambda x: (12 + 6*x + x**2)/(12 - 6*x + x**2)   # padé ordre (2,2)
    trace(p22, -2, 4, color='orange', label="Padé d'ordre (2,2)")

    plt.legend()
    # plt.axis('equal')
    plt.xlim(-2, 4)
    # plt.ylim(0.5, 1.5)
    plt.legend()
    plt.grid(True, which='both')    
    plt.tight_layout() 
    # plt.savefig('approx-pade-01.png',dpi=600) 
    plt.show()

exemple1()


# Exemple erreur f = exp(x)
def exemple2():

    g4 = lambda x: np.exp(x) - (1 + x + 1/2*x**2 + 1/6*x**3 + 1/24*x**4)  # Dl ordre 4
    trace(g4, -1, 1, color='green', label="erreur DL d'ordre 4")

    p22 = lambda x: np.exp(x) - (12 + 6*x + x**2)/(12 - 6*x + x**2)   # padé ordre (2,2)
    trace(p22, -1, 1, color='orange', label="erreur Padé d'ordre (2,2)")

    plt.legend()
    # plt.axis('equal')
    plt.xlim(-1, 1)
    # plt.ylim(0.5, 1.5)
    plt.legend()
    plt.grid(True, which='both')    
    plt.tight_layout() 
    # plt.savefig('approx-pade-02.png',dpi=600) 

    plt.show()

# exemple2()

s