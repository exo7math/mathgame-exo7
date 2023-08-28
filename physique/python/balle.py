# Réflexion et réfraction de rayons

### Partie A
### Lancer d'une balle (sans frottements)

import matplotlib.pyplot as plt
import numpy as np

### Trajectoire d'une balle lancée avec angle alpha et vitesse v0 
### Méthode par équation globale
def lancer_balle(alpha, v0):
    g = 9.81
    t = np.linspace(0, 2*v0*np.sin(alpha)/g, 100)
    x = v0*np.cos(alpha)*t
    y = v0*np.sin(alpha)*t - 0.5*g*t**2
    return x, y



def afficher_balle(alpha, v0):
    x, y = lancer_balle(alpha, v0)
    plt.plot(x, y)
    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('balle1.png', dpi=300)    
    plt.show()

# afficher_balle(np.pi/3, 10)

def afficher_balle_bis():
    v0 = 10
    for alpha in np.linspace(0, np.pi/2-0.1, 10):
        x, y = lancer_balle(alpha, v0)
        plt.plot(x, y)
    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('balle2.png', dpi=300)    
    plt.show()

# afficher_balle_bis()

def afficher_balle_ter():
    alpha = np.pi/3
    for v0 in np.linspace(3, 10, 10):
        x, y = lancer_balle(alpha, v0)
        plt.plot(x, y)
    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('balle3.png', dpi=300)    
    plt.show()

# afficher_balle_ter()



### Partie B
### Lancer d'une balle (sans ou avec frottements)

### Trajectoire d'une balle lancée avec angle alpha et vitesse v0 
### SANS frottements
### Méthode par éléments différentiels

def lancer_balle_bis(alpha, v0):
    g = 9.81
    dt = 0.01
    x, y = 0, 0
    list_x = [0]
    list_y = [0]
    vx = v0*np.cos(alpha)
    vy = v0*np.sin(alpha)
    while list_y[-1] >= 0:
        x = x + vx*dt
        y = y + vy*dt
        list_x.append(x)
        list_y.append(y)
        vy += -g*dt
    return list_x, list_y

def afficher_balle_bis(alpha, v0):
    list_x, list_y = lancer_balle_bis(alpha, v0)
    plt.plot(list_x, list_y)
    plt.axis('equal')
    plt.show()

# afficher_balle_bis(np.pi/3, 10)


### Trajectoire d'une balle lancée avec angle alpha et vitesse v0 
### AVEC frottements  du type - kf v^{ef}
### Méthode par éléments différentiels

def lancer_balle_frottement(alpha, v0, kf, ef):
    g = 9.81
    m = 1 # masse
    dt = 0.01
    x, y = 0, 0
    list_x = [0]
    list_y = [0]
    vx = v0*np.cos(alpha)
    vy = v0*np.sin(alpha)
    while list_y[-1] >= 0:
        x = x + vx*dt
        y = y + vy*dt

        list_x.append(x)
        list_y.append(y)

        theta = np.arctan2(vy,vx) # angle de la vitesse
        nv = np.sqrt(vx**2+vy**2) # norme de la vitesse
        vx += -kf/m * nv**ef * np.cos(theta) * dt # nouvelle vit. en x  après frottements
        vy += -g*dt - kf/m * nv**ef * np.sin(theta) * dt # nouvelle vit. en y après gravité et frott.


    return list_x, list_y


def afficher_balle_frottemnt(alpha, v0, kf, ef):
    list_x, list_y = lancer_balle_frottement(alpha, v0, 0.0, 1.0)  # sans frottement
    plt.plot(list_x, list_y, 'b')
    list_x, list_y = lancer_balle_frottement(alpha, v0, kf, ef)  # avec
    plt.plot(list_x, list_y, 'r')   
    plt.axis('equal')    
    plt.tight_layout()
    plt.savefig('balle-frottements.png', dpi=300)       
    plt.show()

kf, ef = 0.1, 2
afficher_balle_frottemnt(np.pi/3, 10, kf, ef)



### Partie C
### Lancer d'une balle avec rebond

def lancer_balle_avec_rebonds(alpha, v0, c, n):
    """ c coefficient de restitution, n nombre de rebonds"""
    g = 9.81
    dt = 0.01
    x, y = 0, 0
    list_x = [0]
    list_y = [0]
    vx0 = v0*np.cos(alpha)
    vy0 = v0*np.sin(alpha)
    vx, vy = vx0, vy0
    while n > 0:
        x = x + vx*dt
        y = y + vy*dt
        list_x.append(x)
        list_y.append(y)
        vy += -g*dt
        if y < 0:
            y = 0
            vx0 = c*vx0
            vy0 = c*vy0
            vx, vy = vx0, vy0
            n += -1
    return list_x, list_y


def afficher_balle_avec_rebonds(alpha, v0, c, n):
    list_x, list_y = lancer_balle_avec_rebonds(alpha, v0, c, n)
    plt.plot(list_x, list_y)
    plt.axis('off')
    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('balle-rebond.png', dpi=300)    
    plt.show()

# afficher_balle_avec_rebonds(np.pi/2-np.pi/10, 15, 0.8, 7)

