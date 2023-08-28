
# Landscape generation 2D
# Loop version

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import random

import imageio

n = 8
N = 2**n # N+1 values
H = 1    # initial value
h = 2    # max variation for first middle point
r = 1.3  # rugosity (lower is higher!)

# random.seed(1236)  # for reproducibility

random.seed(1236)  # for reproducibility

hauteurs = np.zeros((N+1, N+1))
hauteurs[0,0] = H
hauteurs[N,0] = H
hauteurs[N,N] = H
hauteurs[0,N] = H


for i in range(n):

    k = 2**(n-i-1)

    ### Diamond value (center of each square)
    x = 0
    for j in range(2**i):
        y = 0
        for jj in range(2**i):

            variation = h/(2**(r*i)) * (2*random.random()-1)
            hauteurs[x+k,y+k] = (hauteurs[x,y] + hauteurs[x,y+2*k] + hauteurs[x+2*k,y] + hauteurs[x+2*k,y+2*k])/4 + variation
            
            y = y + 2*k

        x = x + 2*k

    ### Square values (midpoints of each edge)
    x = 0
    for j in range(2**i):
        y = 0
        for jj in range(2**i):

            variation = h/(2**(r*i)) * (2*random.random()-1)
            hauteurs[x+k,y] = (hauteurs[x,y] + hauteurs[x+2*k,y] + hauteurs[x+k,y+k] + hauteurs[x+k,(y-k)%(N)])/4 + variation

            variation = h/(2**(r*i)) * (2*random.random()-1)
            hauteurs[x,y+k] = (hauteurs[x,y] + hauteurs[x,y+2*k] + hauteurs[x+k,y+k] + hauteurs[(x-k)%(N),y+k])/4 + variation

            # Last column = First column
            if y == 0:
                hauteurs[x+k,N] = hauteurs[x+k,0]                

            # Last line = First line
            if x == 0:
                hauteurs[N,y+k] = hauteurs[0,y+k]

            y = y + 2*k

        x = x + 2*k

# print(hauteurs)

# # Sea level
Hmer = 1.8
mer = Hmer * np.ones((N+1, N+1))
audessusmer = np.maximum(hauteurs,mer)


X, Y = np.meshgrid(range(N+1), range(N+1))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('axe x')
ax.set_ylabel('axe y')
ax.set_zlabel('axe z')
ax.view_init(36, 25)

# ax.plot_surface(X,Y,hauteurs, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.plot_surface(X,Y,audessusmer, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# plt.axis('off')
plt.tight_layout()
# plt.savefig('hauteurs-04.png')
plt.show()

# h = hauteurs
h = audessusmer

hmin = np.min(h)
hmax = np.max(h)
h = 255/(hmax-hmin)*(h-hmin)

h = np.clip(h,0,255)   # limite les valeurs entre 0 et 255
h = h.astype(np.uint8)  # conversion en entier
# imageio.imwrite('hauteurs-05.png', h)

