
# Landscape generation 2D
# Loop version

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import random

n = 8
N = 2**n # N+1 values
H = 0    # initial value
h = 2.5   # max variation for first middle point
r = 1.0  # rugosity (lower is higher!)

random.seed(2023)  # for reproducibility


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

print(hauteurs)

# Sea level
Hmer = 0.5
mer = Hmer * np.ones((N+1, N+1))
audessusmer = np.maximum(hauteurs,mer)


X, Y = np.meshgrid(range(N+1), range(N+1))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('axe x')
ax.set_ylabel('axe y')
ax.set_zlabel('axe z')
ax.set_zlim(-1,2)
ax.view_init(35, 50)

# ax.plot_surface(X,Y,hauteurs, cmap=cm.viridis, linewidth=0, antialiased=False)
ax.plot_surface(X,Y,audessusmer, cmap=cm.hot, linewidth=0, antialiased=False)

# plt.axis('off')
plt.tight_layout()
# plt.savefig('diamant-carre-03-4.png')
plt.show()


# diamant-carre-01
# n = 8
# N = 2**n # N+1 values
# H = 0    # initial value
# h = 2    # max variation for first middle point
# r = 1.3  # rugosity (lower is higher!)
# random.seed(1240)  # for reproducibility
# ax.view_init(35, -65)

# diamant-carre-02-1
n = 8
N = 2**n # N+1 values
H = 0    # initial value
h = 3    # max variation for first middle point
r = 1.0  # rugosity (lower is higher!)
random.seed(1241)  # for reproducibility
ax.view_init(40, -130)


# diamant-carre-02-2
n = 8
N = 2**n # N+1 values
H = 0    # initial value
h = 2    # max variation for first middle point
r = 1.1  # rugosity (lower is higher!)
random.seed(1242)  # for reproducibility
ax.view_init(40, 15)


# diamant-carre-02-3
n = 8
N = 2**n # N+1 values
H = 0    # initial value
h = 1    # max variation for first middle point
r = 1.2  # rugosity (lower is higher!)
random.seed(1245)  # for reproducibility
ax.view_init(30, 170)


# diamant-carre-03
n = 8
N = 2**n # N+1 values
H = 0    # initial value
h = 2.5   # max variation for first middle point
r = 1.0  # rugosity (lower is higher!)
random.seed(2023)  # for reproducibility
ax.view_init(35, 50)