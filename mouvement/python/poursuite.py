
import numpy as np
import matplotlib.pyplot as plt


# Données du problème
vitesse = 0.15    # Vitesse du chat
x0, y0 = 0, 0  # Position initiale du chat
deltat = 0.1   # Pas de temps


def vecteur_unitaire(x1,y1,x2,y2):
    """Retourne le vecteur unitaire (x,y) de la droite passant par les points (x1,y1) et (x2,y2)"""
    norme = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    return (x2-x1)/norme, (y2-y1)/norme 


# Trajectoire de la souris
def souris(t):
    # X, Y = np.cos(t), np.sin(t)  # Cercle
    # X, Y = 5+t, 1+0.5*np.sin(2*t)  # Sinusoide
    X, Y = 10.+0.1*t, 1+t  # Droite
    return X, Y


# Trajectoire du chat
def chat(tmax):
    """Retourne la trajectoire du chat"""
    # Initialisation
    list_x, list_y = [x0], [y0]
    x, y = x0, y0
    t = 0
    while t < tmax:
        vx, vy = vecteur_unitaire(x, y, *souris(t))
        x += vitesse * vx
        y += vitesse * vy
        list_x.append(x)
        list_y.append(y)
        t += deltat

    return np.array(list_x), np.array(list_y)


# Affichage
def affichage(tmax):
    """Affiche la trajectoire du chat et de la souris"""
    # Trajectoire du chat
    Xc, Yc = chat(tmax)
    plt.plot(Xc, Yc, 'o', ls='-', ms=3, markevery=10, color="red", label="chat")
    xc0, yc0 = Xc[0], Yc[0]
    plt.scatter(xc0, yc0, s=25, color="red")    

    # Trajectoire de la souris
    T = np.arange(0, tmax, deltat)
    Xs, Ys = souris(T)
    plt.plot(Xs, Ys, 's', ls='-', ms=3, markevery=10, color="blue", label="souris")
    xs0, ys0 = Xs[0], Ys[0]
    plt.scatter(xs0, ys0, marker='s', s=25, color="blue")  

    # Rayons
    # for i in range(len(T)):
    #     xs, ys = souris(i*deltat)
    #     plt.plot([Xc[i], xs], [Yc[i], ys], color="gray", lw=0.5)


    # Affichage
    plt.axis("equal")
    plt.axis("off")
    plt.legend()
    plt.tight_layout()
    # plt.savefig("poursuite-02.png", dpi=300)
    plt.show()

affichage(11)


# Poursuite 1 : cercle, vitesse = 0.05, deltat = 0.05, tmax = pi/2
# Poursuite 2 : droite, vitess = 0.15, deltat = 0.1, tmax = 11






