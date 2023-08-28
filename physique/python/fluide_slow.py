# Ecoulement d'un fluide
# Méthode de Boltzmann
# D'après Philip Mocz
# https://medium.com/swlh/create-your-own-lattice-boltzmann-simulation-with-python-8759e8b53b1c
# Version non optimisée mais plus lisible


import numpy as np
import matplotlib.pyplot as plt

Nx = 400   # Résolution en x
Ny = 100  # Résolution en y
Nv = 9     # Nombre de vitesses
rho0 = 100 # Densité moyenne
tau = 0.6  # Temps de collision
Nt = 50    # Nombre de pas de temps


X, Y = np.meshgrid(range(Nx), range(Ny), indexing='ij') # Grille de coordonnées (x,y)

poids = np.array([4/9,1/9,1/36,1/9,1/36,1/9,1/36,1/9,1/36]) # Somme des poids vaut 1

# Vecteurs vitesse v = (vx, vy) indexé de 0 à 8
# v = 0 : (0,0)
# v=1 : (0,1) ; v=2 : (1,1) ; v=3 : (1,0) ; v=4 : (1,-1)
# v=5 : (0,-1) ; v=6 : (-1,-1) ; v=7 : (-1,0) ; v=8 : (-1,1)
vx = np.array([0, 0, 1, 1, 1, 0,-1,-1,-1])
vy = np.array([0, 1, 1, 0,-1,-1,-1, 0, 1])


F = np.ones((Nx,Ny,Nv)) # Initialisation de la fonction de distribution à F(x,y,v) = 1 partout
np.random.seed(31415)                # Graine du générateur aléatoire
F += 0.01*np.random.randn(Nx,Ny,Nv)  # Ajout d'un petit bruit aléatoire
F[:,:,3] += 2 * (1+0.2*np.cos(2*np.pi*X/Nx*4))  # Ajout d'un flux vers la droite sur la composante v=3 cad v = (1,0)
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
FF = np.zeros((Nx,Ny,Nv)) # Copie de F pour éviter les effets de bords


# Boucle principale
for it in range(Nt):

    # Mouvement naturel : une mini-particule suit sont vecteur vitesse
    for x in range(Nx):
        for y in range(Ny):
            for i in range(Nv):
                FF[(x+vx[i])%Nx,(y+vy[i])%Ny,i] = F[x,y,i] # Mini-particules suivent leur vecteur vitesse (vx[i],vy[i])
                # pass
                # Exemple 
                # F[(x+0)%Nx,(y+1)%Ny,1] = F[x,y,1]  # Mini-particules suivent leur vecteur vitesse (0,1)

    F[:,:,:] = FF # Copie de FF dans F


    # Densité rho et quantité de mvt rho u = rho (ux, uy) et vitesse moyenne u = (ux, uy)
    rux = F[:,:,2] + F[:,:,3] + F[:,:,4] - F[:,:,6] - F[:,:,7] - F[:,:,8] # Quantité de mouvement en x : somme des vx*F(x,y,v)
    ruy = F[:,:,1] + F[:,:,2] - F[:,:,4] - F[:,:,5] - F[:,:,6] + F[:,:,8] # Quantité de mouvement en y : somme des vy*F(x,y,v)
    rho = np.sum(F,2)  # Densité
    ux = rux / rho  # Vitesse moyenne en x
    uy = ruy / rho  # Vitesse moyenne en y

    # Fonction d'équilibre
    Feq = np.zeros((Nx,Ny,Nv))
    for i in range(Nv):
        Feq[:,:,i] = poids[i] * rho * (1 + 3*(ux*vx[i] + uy*vy[i]) + 9/2*(ux*vx[i] + uy*vy[i])**2 - 3/2*(ux**2 + uy**2))

    # Formule principale d'itération
    FF[:,:,:] = F -(1.0/tau) * (F - Feq)
    # FF = F

    # Bords réfléchissants
    for x in range(Nx):
        for y in range(Ny):
            if obstacle[x,y]:
                FF[x,y,0] = F[x,y,0]
                FF[x,y,1] = F[x,y,5]  # mini-particule allant vers la haut rebondit vers le bas
                FF[x,y,2] = F[x,y,6]
                FF[x,y,3] = F[x,y,7]  # mini-particule allant vers la droite rebondit vers la gauche
                FF[x,y,4] = F[x,y,8]  
                FF[x,y,5] = F[x,y,1]
                FF[x,y,6] = F[x,y,2]
                FF[x,y,7] = F[x,y,3]
                FF[x,y,8] = F[x,y,4]

    F[:,:,:] = FF
    
    # Affichage
    if (it%10 == 0) or (it == Nt-1):
        print('t =',it)
        plt.cla()
        ux[obstacle] = 0
        uy[obstacle] = 0
        vortex = np.zeros((Nx,Ny))
        # vortex = (np.roll(ux, -1, axis=0) - np.roll(ux, 1, axis=0)) - (np.roll(uy, -1, axis=1) - np.roll(uy, 1, axis=1))

        for x in range(Nx):
            for y in range(Ny):
                vortex[x,y] = (uy[(x+1)%Nx,y] - uy[(x-1)%Nx,y]) - (ux[x,(y+1)%Ny] - ux[x,(y-1)%Ny])  

                if obstacle[x,y]:
                    vortex[x,y] = np.nan

        # vortex = (np.roll(uy, -1, axis=0) - np.roll(uy, 1, axis=0)) - (np.roll(ux, -1, axis=1) - np.roll(ux, 1, axis=1))
        # vortex[obstacle] = np.nan

                
        # vortex[obstacle] = np.nan
        vortex = np.ma.array(vortex, mask=obstacle)
        # print(vortex.shape)
        # print(vortex)
        plt.imshow(vortex.T, cmap='bwr')
        plt.imshow(~obstacle.T, cmap='gray', alpha=0.3)
        plt.clim(-.1, .1)
        ax = plt.gca()
        ax.invert_yaxis()
        # ax.get_xaxis().set_visible(False)
        # ax.get_yaxis().set_visible(False)	
        ax.set_aspect('equal')	
        plt.pause(0.001)

plt.show()