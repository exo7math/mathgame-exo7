# Polynômes de Tchebychev

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

# Polynôme T_n de Tchebychev
def T(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return 2*x*T(n-1, x) - T(n-2, x)

# Exemple 1 : afficher les premiers polynômes de Tchebychev
def exemple1():
    # macoul = ['blue', 'red', 'green', 'black', 'orange']
    # for i in range(1,5):
    #     f = lambda x: T(i, x)
    #     trace(f, -1.2, 1.2, color=macoul[i]  , label='T_'+str(i))

    i = 6
    f = lambda x: T(i, x)
    trace(f, -1.2, 1.2, color='red', label='T_'+str(i))
    plt.axis('equal')
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.5, 1.5)
    plt.legend()
    plt.grid(True, which='both')    
    plt.tight_layout()   
    # plt.savefig('approx-tchebychev-01-'+str(i)+'.png',dpi=600) 
    plt.show()


# exemple1()


# Exemple 2 : approximation de 0 sur [-1,1]
def exemple2():
    macoul = ['blue', 'red', 'green', 'orange','black']
    for i in range(2,7):
        f = lambda x: 1/2**i * T(i, x)
        trace(f, -1.1, 1.1, color=macoul[i-2], label='T_'+str(i)+'/2^'+str(i-1))
    plt.axis('equal')
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.5, 1.5)
    plt.legend()
    plt.grid(True, which='both')    
    plt.tight_layout()   
    # plt.savefig('approx-tchebychev-02.png',dpi=600) 
    plt.show()

# exemple2()


# Liste des racines de T_n
def racines(n):
    list_rac = []
    for k in range(n):
        x = np.cos((2*k+1)*np.pi/(2*n))
        list_rac.append(x)
    return list_rac

# Exemple 3 : racines de T_n
def exemple3(n):
    f = lambda x: T(n, x)
    liste_rac = racines(n)
    trace(f, -1.1, 1.1, color='blue')
    plt.plot(liste_rac, [0]*len(liste_rac), 'o', color='red')
    plt.show()

# exemple3(5)


# Coefficient c(i, n) de la série de Tchebychev
def coefficient(i, n, f):
    liste_rac = racines(n)
    if i == 0:
        coeff = sum(f(x) for x in liste_rac)
    if i > 0:
        coeff = 2*sum(f(x)*T(i, x) for x in liste_rac)        
    return 1/n*coeff


# Développement en série de Tchebychev
def serie_Tchebychev(n, f):
    def F(x):
        somme = 0
        for i in range(n):
            somme += coefficient(i, n, f)*T(i, x)
        return somme
    return F

# Exemple 4 : approximation de 1/(1+5x^2 +2x) sur [-1,1]
def exemple4(n):
    f = lambda x: 1/(1+5*x**2+2*x)
    F = serie_Tchebychev(n, f)
    trace(f, -1.1, 1.1, color='blue', label='f')
    trace(F, -1.1, 1.1, color='red', label='n = '+str(n))

    plt.axis('equal')
    plt.xlim(-1.2, 1.2)
    plt.ylim(-0.2, 2)
    plt.legend()
    plt.grid(True, which='both')    
    plt.tight_layout()   
    plt.savefig('approx-tchebychev-03-'+str(n)+'.png',dpi=600) 
    plt.show()  

# exemple4(3)


# Exemple g = sin(x) sur [0,pi/2]
def exemple5(): 
    n = 3
    g = lambda x: np.sin(x)
    f = lambda x: np.sin( (x+1)/2*np.pi/2 )

    liste_rac = racines(n)
    for i in range(n):
        print('omega_i =', liste_rac[i], '  f(omega_i) =', f(liste_rac[i]))

    for i in range(n):
        print('i =', i, '  c_i =', coefficient(i, n, f))

    F = serie_Tchebychev(3, f)

    G = lambda x: F(4*x/np.pi-1)
    trace(g, 0, np.pi/2, color='blue', label='g ')
    trace(G, 0, np.pi/2, color='red', label='n = 3')

    plt.axis('equal')
    plt.xlim(0,np.pi/2)
    plt.ylim(0, 1.1)
    plt.legend()
    plt.grid(True, which='both')    
    plt.tight_layout()   
    # plt.savefig('approx-tchebychev-04.png',dpi=600) 
    # plt.show()    

    H = lambda x: g(x) - G(x)
    trace(H, 0, np.pi/2, color='red', label='erreur n = 3')

    # plt.axis('equal')
    plt.xlim(0,np.pi/2)
    plt.ylim(-0.2, 0.2)
    plt.legend()
    plt.grid(True, which='both')    
    plt.tight_layout()   
    # plt.savefig('approx-tchebychev-05.png',dpi=600) 
    plt.show()      



exemple5()
