# IFS 

import matplotlib.pyplot as plt
import random

# Depuis Mooc 'Sage"'
## TP6 -- Calcul formel

# IFS

# Transformation affine
def transformation(x,y,a,b,c,d,e,f):
    xx = a*x + b*y + e
    yy = c*x + d*y + f
    return xx, yy
    


# Au hasard : renvoie l'indice en fonction d'une liste de proba
def hasard(pliste):
    x = random.random()
    k = 0
    while k < len(pliste) and x > pliste[k]:
        x = x - pliste[k]
        k = k + 1
    if k >= len(pliste):
        k = k - 1
    return k
    

# Test    
#pliste = [0.25,0.5,0.25]
#for i in range(5):
#    print(hasard(pliste))


# Trace une ifs
# En entrée une liste de transformations et des probas
# Chaque transformation est du type [a,b,c,d,e,f,p] 
def ifs(transfoliste, nbiter):
    pliste = [transfo[6] for transfo in transfoliste] # Les proba
    x=0; y=0 #x=random(); y=random()   # Point initial (au pif)
    listepoints = []
    for i in range(nbiter):                  # Itération
        k = hasard(pliste)                   # On choisit un tranfo au hasard
        # k = hasard_bis(len(pliste))
        transfo = (transfoliste[k])[0:6]     # Voici la transfo
        x,y = transformation(x, y, *transfo)   # L'image du point
        if i > 100:                          # On n'affiche pas les tous premiers points 
            listepoints.append((x, y))
    return listepoints
    
    
# La fougère
fougere = [
[0, 0,  0,  0.16,   0,  0,  0.01],
[0.85,  0.04,   -0.04,  0.85,   0,  1.60,   0.85],
[0.20,  -0.26,  0.23,   0.22,   0,  1.60,   0.07],
[-0.15, 0.28,   0.26,   0.24,   0,  0.44,   0.07]
]

# Le triangle de Sierpinski
sierpinski = [
[0.5,0,0,0.5,0,0,0.33],
[0.5,0,0,0.5,0.5,0,0.33],
[0.5,0,0,0.5,0.25,0.43,0.34]
]

# Hippocampe
hippocampe= [
[0.82,  0.28,  -0.21,  0.86,  -1.88,  0.11, 0.8],
[0.08,  0.52,  -0.46,  -0.37,  0.78,  8.09, 0.2]
]

# Spirale Paul Bourke                                                                                       
spirale = [
[0.787879,-0.424242,0.242424,0.859848,1.758647,1.408065,0.896],
[-0.121212,0.257576,0.151515,0.053030,6.721654,1.377236,0.052],
[0.181818,-0.136364,0.090909,0.181818,6.086107,1.568035,0.052]
]

# Maple leaf - Paul Bourke
maple = [
[0.14, 0.01, 0.00, 0.51,-0.08,-1.31, 0.10],
[0.43, 0.52,-0.45, 0.50, 1.49,-0.75, 0.30],
[0.45, -0.49,  0.47,  0.47, -1.62, -0.74,  0.30],
[0.490, 0.000, 0.000, 0.510, 0.020, 1.620,  0.30]
]

# Feuille 1 - Paul Bourke

feuille1 = [
[0.0100, -0.4100,  0.3900,  0.0000, -0.2800, -0.1850, 0.25],
[0.7000,  0.3300, -0.3500,  0.7000,  0.1850,  0.0150, 0.65],
[0.0000,  0.1750,  0.0130,  0.4600, -0.0950, -0.2850, 0.1]
]


# Feuille 2 - Paul Bourke

feuille2 = [
[0.0000, 0.2439, 0.0000, 0.3053, 0.0000, 0.0000, 0.05],
[0.7248,  0.0337, -0.0253,  0.7426,  0.2060,  0.2538, 0.55],
[0.1583, -0.1297,  0.3550,  0.3676,  0.1383,  0.1750, 0.20], 
[0.3386,  0.3694,  0.2227, -0.0756,  0.0679,  0.0826, 0.20]
] 


# Enigme du tp : 6039 à deviner

enigme = [
# Chiffre 6
[0.143,0,0,0.143,0,0,0.0435],
[0.143,0,0,0.143,1,3,0.0435],
[0.143,0,0,0.143,1,6,0.0435],
[0,-0.143,0.143,0,1,1,0.0435],
[0,-0.143,0.143,0,1,4,0.0435],
[0,-0.143,0.143,0,4,0,0.0435],
# Chiffre 0
[0.143,0,0,0.143,5.666,0,0.0435],
[0,-0.143,0.143,0,9.666,3,0.0435],
[0.143,0,0,0.143,6.666,6,0.0435],
[0,-0.143,0.143,0,6.666,1,0.0435],
[0,-0.143,0.143,0,6.666,4,0.0435],
[0,-0.143,0.143,0,9.666,0,0.0435],
# Chiffre 3
[0.143,0,0,0.143,11.33,0,0.0435],
[0.143,0,0,0.143,12.33,3,0.0435],
[0.143,0,0,0.143,11.33,6,0.0435],
[0,-0.143,0.143,0,15.33,0,0.0435],
[0,-0.143,0.143,0,15.33,4,0.0435],
# Chiffre 9
[0.143,0,0,0.143,17,0,0.0435],
[0.143,0,0,0.143,18,3,0.0435],
[0.143,0,0,0.143,17,6,0.0435],
[0,-0.143,0.143,0,21,4,0.0435],
[0,-0.143,0.143,0,18,3,0.0435],
[0,-0.143,0.143,0,21,0,0.0430],
]
 
monifs = ifs(fougere,100000)


# monifs = ifs(sierpinski,100000)
# monifs = ifs(hippocampe,100000)
# monifs = ifs(spirale,50000)
# monifs = ifs(enigme,100000)
# monifs = ifs(maple,200000)
# monifs = ifs(feuille1, 100000)
# monifs = ifs(feuille2, 100000)

# Affichage
liste_x = [p[0] for p in monifs]
liste_y = [p[1] for p in monifs]

fig = plt.figure()
ax = plt.axes(aspect='equal')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 11)

plt.axis('off')
plt.tight_layout()
# ax.plot(liste_x, liste_y,color='black',marker=',',lw=0, linestyle="")
plt.scatter(liste_x, liste_y, color='black', marker='o', linewidth = 0, s=0.3)
plt.savefig('fougere.png', dpi=600)
plt.show()  


# Pour forum 
carre = [
[0,-1/4,1/4,0,0,1/2,0.25], # carré sur le côté gauche
[-1/4,0,0,-1/4,1/2,0,0.25], # carré sur dessous
[0,1/4,-1/4,0,1,1/2,0.25], # carré sur le côté droit
[1/4,0,0,1/4,1/2,1,0.25] # carré sur le dessus`
] 

#monifs = ifs(carre,1000)
#G = points(monifs,size=1)
#G.show(aspect_ratio=1,axes=False)  
