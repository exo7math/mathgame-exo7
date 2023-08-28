# Ecoulement d'un fluide
# Méthode de Boltzmann
# D'après Philip Mocz
# https://medium.com/swlh/create-your-own-lattice-boltzmann-simulation-with-python-8759e8b53b1c
# Ici version optimisée qui utilise davantage les routines numpy, voir
# https://github.com/pmocz/latticeboltzmann-python

import numpy as np
import matplotlib.pyplot as plt

Nx = 400   # Résolution en x
Ny = 100  # Résolution en y
Nv = 9     # Nombre de vitesses
rho0 = 100 # Densité moyenne
tau = 0.6  # Temps de collision
Nt = 1000    # Nombre de pas de temps


X, Y = np.meshgrid(range(Nx), range(Ny), indexing='ij') # Grille de coordonnées (x,y)

poids = np.array([4/9,1/9,1/36,1/9,1/36,1/9,1/36,1/9,1/36]) # Somme des poids vaut 1

# Vecteurs vitesse v = (vx, vy) indexé de 0 à 8
# v = 0 : (0,0)
# v=1 : (0,1) ; v=2 : (1,1) ; v=3 : (1,0) ; v=4 : (1,-1)
# v=5 : (0,-1) ; v=6 : (-1,-1) ; v=7 : (-1,0) ; v=8 : (-1,1)
vx = np.array([0, 0, 1, 1, 1, 0,-1,-1,-1])
vy = np.array([0, 1, 1, 0,-1,-1,-1, 0, 1])
idxs = np.arange(Nv)

F = np.ones((Nx,Ny,Nv)) # Initialisation de la fonction de distribution à F(x,y,v) = 1 partout
np.random.seed(31415)                # Graine du générateur aléatoire
F += 0.01*np.random.randn(Nx,Ny,Nv)  # Ajout d'un petit bruit aléatoire
F[:,:,3] += 2 * (1+0.4*np.cos(2*np.pi*X/Nx*4))#  Ajout d'un flux vers la droite sur la composante v=3 cad v = (1,0)
rho = np.sum(F,2)   # Calcul de la densité rho(x,y) = somme sur v de F(x,y,v)
for i in range(Nv):
    F[:,:,i] *= rho0 / rho           # On multiplie F(x,y,v) par rho0/rho(x,y) pour tout x,y
                                     # Ainsi la densité moyenne en (x,y) est égale à rho0

# Obstacle : vaut 1 (True) si on est dans l'obstacle, 0 (False) sinon
obstacle = (X - Nx/4)**2 + (Y - Ny/2)**2 < (Ny/4)**2   # Cylindre de rayon Ny/4 centré en (Nx/4,Ny/2)

# Test de l'obstacle
# print(obstacle.shape)
# plt.scatter([0],[0], c='r', s=100)
# plt.scatter([100],[50], c='b', s=100)
# plt.imshow(obstacle.T, cmap='gray', alpha=0.3)
# ax = plt.gca()
# ax.invert_yaxis()
# plt.show()


fig = plt.figure(figsize=(10,5), dpi=80)

# Boucle principale
for it in range(Nt):


    # Mouvement naturel : une mini-particule suit sont vecteur vitesse
    for i, dx, dy in zip(idxs, vx, vy):
        F[:,:,i] = np.roll(F[:,:,i], dx, axis=0)
        F[:,:,i] = np.roll(F[:,:,i], dy, axis=1)

    # Obstacle
    bordF = F[obstacle,:]
    bordF = bordF[:,[0,5,6,7,8,1,2,3,4]]

 	# Densité et vitesses 
    rho = np.sum(F,2)
    ux  = np.sum(F*vx,2) / rho
    uy  = np.sum(F*vy,2) / rho   
    
    # Fonction d'équilibre
    Feq = np.zeros(F.shape)
    for i, cx, cy, w in zip(idxs, vx, vy, poids):
        Feq[:,:,i] = rho * w * ( 1 + 3*(cx*ux+cy*uy)  + 9*(cx*ux+cy*uy)**2/2 - 3*(ux**2+uy**2)/2 )
    
    # Action des collisitions
    F += -(1.0/tau) * (F - Feq)
    
    # Apply boundary 
    F[obstacle,:] = bordF

    # Affichage
    if (it%10 == 0) or (it == Nt-1):
    # if (it == Nt-1):    # décommenter8 pour sauver la dernière image
        print('t =',it)
        plt.cla()
        ux[obstacle] = 0
        uy[obstacle] = 0

        # Vortex
        vortex = np.zeros((Nx,Ny))
        vortex = (np.roll(uy, -1, axis=0) - np.roll(uy, 1, axis=0)) - (np.roll(ux, -1, axis=1) - np.roll(ux, 1, axis=1))
        vortex[obstacle] = np.nan
        vortex = np.ma.array(vortex, mask=obstacle)
        plt.imshow(vortex.T, cmap='bwr')
        plt.imshow(~obstacle.T, cmap='gray', alpha=0.3)
        plt.clim(-.1, .1)

        # Vitesse
        # vitesse = np.sqrt(ux**2 + uy**2)
        # vitesse[obstacle] = np.nan
        # vitesse = np.ma.array(vitesse, mask=obstacle)
        # plt.imshow(vitesse.T, cmap='jet')
        # plt.imshow(~obstacle.T, cmap='gray', alpha=0.3)
        # plt.clim(0, 1.0)

        # Densité
        # densite = rho
        # densite[obstacle] = np.nan
        # densite = np.ma.array(densite, mask=obstacle)
        # plt.imshow(densite.T, cmap='jet')
        # plt.imshow(~obstacle.T, cmap='gray', alpha=0.3)
        # plt.clim(0, 2.0)   


        ax = plt.gca()
        ax.invert_yaxis()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)	
        ax.set_aspect('equal')	
        plt.pause(0.001)

plt.tight_layout()
# plt.savefig('fluide-vortex-4000.png', dpi=600)
plt.show()