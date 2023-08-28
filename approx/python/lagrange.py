# Polynômes d'interpolation de Lagrange

import matplotlib.pyplot as plt
import numpy as np

# Affiche le graphe de la fonction f sur [a,b] avec N points
def trace(f, a, b, N=100, color='blue'):
    list_x, list_y = [], []
    for x in np.linspace(a, b, N):
        list_x.append(x)
        list_y.append(f(x))
    plt.plot(list_x, list_y, color=color)
    return

# Polynôme élémentaire Lagrange
def L(x, i, A):
    p = 1
    for j in range(len(A)):
        if j != i:
            p *= (x-A[j])/(A[i]-A[j])
    return p

# Polynôme d'interpolation de Lagrange
def P(x, A, B):
    # A = liste des abscisses
    # B = liste des ordonnées
    p = 0
    for i in range(len(A)):
        p += B[i]*L(x, i, A)
    return p


# Exemple
def exemple1():
    A = [0, 1, 2, 4, 6]
    B = [1, 2, -2, 3, 1]
    f = lambda x: P(x, A, B)
    trace(f, min(A)-0.5, max(A)+0.5, color='blue')
    plt.plot(A, B, 'o', color='red')

    # plt.legend()
    plt.grid(True, which='both')
    plt.tight_layout()
    # plt.savefig('approx-lagrange-01.png',dpi=600) 
    plt.show()

exemple1()


# Exemple
def exemple2():
    A = [0, 1, 3]
    B = [2, 1, 4]
    f = lambda x: P(x, A, B)
    trace(f, min(A)-1, max(A)+1, color='blue')
    plt.plot(A, B, 'o', color='red')

    # plt.legend()
    plt.grid(True, which='both')
    plt.tight_layout()
    # plt.savefig('approx-lagrange-02.png',dpi=600) 
    plt.show()

# exemple2()


# Exemple
def exemple3():
    A = [0, 1, 3, 6] 
    B = [0, 0.9, 3.1, 5.9]
    f = lambda x: P(x, A, B)
    trace(f, min(A)-5, max(A)+5, color='blue')
    plt.plot(A, B, 'o', color='red')

    # plt.legend()
    plt.grid(True, which='both')
    plt.tight_layout()
    # plt.savefig('approx-lagrange-03.png',dpi=600) 
    plt.show()

# exemple3()