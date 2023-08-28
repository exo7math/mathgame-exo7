# Développements limités

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


# Exemple tracé de f = 1/sqrt(x) et de ses DL
def exemple1():
    f = lambda x: 1/np.sqrt(x)
    trace(f, 0.5, 1.5, color='red', label='f')
    g0 = lambda x: 1  # Dl ordre 0
    trace(g0, 0.5, 1.5, color='green')

    g1 = lambda x: 1-1/2*(x-1)  # Dl ordre 1
    trace(g1, 0.5, 1.5, color='orange', label='DL1')

    # g2 = lambda x: 1-1/2*(x-1)+3/8*(x-1)**2  # Dl ordre 2
    # trace(g2, 0.5, 1.5, color='purple', label='DL2')

    plt.legend()
    plt.grid(True, which='both')
    # plt.savefig('approx-dl-01.png',dpi=600) 
    plt.show()

# exemple1()

# Calculs numériques
def exemple1bis():
    f = lambda x: 1/np.sqrt(x)

    g3 = lambda x: 1-1/2*(x-1)+3/8*(x-1)**2-5/16*(x-1)**3  # Dl ordre 3

    x = 1.1
    print("f(x)=", f(x))
    print("g3(x)=", g3(x))

# exemple1bis()

# Exemple calcul de l'erreur
def exemple2():
    # eg0 = lambda x: 1/np.sqrt(x) - 1  # Dl ordre 0
    # trace(eg0, 0.5, 1.5, color='green', label='erreur ordre 0')

    eg1 = lambda x: 1/np.sqrt(x) - (1-1/2*(x-1))  # Dl ordre 1
    trace(eg1, 0.5, 1.5, color='orange', label='erreur ordre 1')

    # eg2 = lambda x: 1/np.sqrt(x) - (1-1/2*(x-1)+3/8*(x-1)**2)  # Dl ordre 2
    # trace(eg2, 0.5, 1.5, color='purple', label='erreur ordre 2')

    plt.legend()
    plt.grid(True, which='both')
    # plt.savefig('approx-dl-02.png',dpi=600) 
    plt.show()

# exemple2()


# Exemple tracé de f = sinus et de ses DL en x=0 et pi/4
def exemple3():
    f = lambda x: np.sin(x)
    trace(f, 0, np.pi/2, color='red', label='f')

    g3 = lambda x: x - 1/6*x**3  # Dl ordre 3
    trace(g3, 0, np.pi/2, color='purple', label='DL3 en 0')

    invrac2 = 1/np.sqrt(2)
    pi4 = np.pi/4

    g3 = lambda x: invrac2*(1+(x-pi4) - 1/2*(x-pi4)**2 -1/6*(x-pi4)**3)  # Dl ordre 3
    trace(g3, 0, np.pi/2, color='magenta', label='DL3 en pi/4')   

    plt.legend()
    plt.grid(True, which='both')
    plt.savefig('approx-dl-03.png',dpi=600) 
    plt.show()

exemple3()

# erreur entre f = sinus et de ses DL en en x=0 et x=pi/4
def exemple4():
    f = lambda x: np.sin(x)

    eg3 = lambda x: f(x) - (x - 1/6*x**3)  # erreur Dl ordre 3
    trace(eg3, 0, np.pi/2, color='purple', label='erreur DL3 en 0')

    invrac2 = 1/np.sqrt(2)
    pi4 = np.pi/4

    eg3 = lambda x: f(x) - (invrac2*(1+(x-pi4) - 1/2*(x-pi4)**2 -1/6*(x-pi4)**3))  # erreur Dl ordre 3
    trace(eg3, 0, np.pi/2, color='magenta', label='erreur DL3 en pi/4')

    plt.legend()
    plt.grid(True, which='both')
    plt.savefig('approx-dl-04.png',dpi=600) 
    plt.show()

exemple4()

# Exemple tracé des erreurs f = sinus et de ses DL en x=pi/4
def exemple5():
    invrac2 = 1/np.sqrt(2)
    pi4 = np.pi/4

    eg1 = lambda x: np.sin(x)-invrac2*(1+(x-pi4))   # Dl ordre 1
    trace(eg1, 0, np.pi/2, color='orange')

    eg2 = lambda x: np.sin(x)-invrac2*(1+(x-pi4) - 1/2*(x-pi4)**2)   # Dl ordre 2
    trace(eg2, 0, np.pi/2, color='purple')   

    eg3 = lambda x: np.sin(x)-invrac2*(1+(x-pi4) - 1/2*(x-pi4)**2 -1/6*(x-pi4)**3)  # Dl ordre 3
    trace(eg3, 0, np.pi/2, color='magenta')

    plt.show()

# exemple5()


# Mesure du temps entre sinus et DL ordre 3 en x=pi/4
def exemple6():
    import random
    import time

    pi4 = np.pi/4
    pi5 = np.pi/5
    invrac2 = 1/np.sqrt(2)

    # Fonction sinus
    t0 = time.time()
    for i in range(1000000):
        np.sin(random.random())
    t1 = time.time()

    print(np.sin(pi5))
    print("Temps sinus :", t1-t0)

    # DL ordre 3
    g3 = lambda x: invrac2*(1+(x-pi4) - 1/2*(x-pi4)**2 -1/6*(x-pi4)**3)  # Dl ordre 3

    t0 = time.time()
    for i in range(1000000):
        g3(random.random())
    t1 = time.time()

    print(g3(pi5))
    print("Temps DL3", t1-t0)



# exemple6()