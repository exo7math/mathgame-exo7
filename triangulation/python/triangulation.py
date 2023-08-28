# Triangulation d'un ensemble de points

# Partie A : outils
# Partie B : enveloppe convexe
# Partie C : triangulation d'un ensemble de points
# Partie D : triangulation de Delaunay
# Partie E : cellule de Voronoi

# On suppose que trois points ne sont jamais alignés

# Les algorithmes et leur implémentations présentés ici sont pédagogiques et ne sont en aucun cas optimisés !


import numpy as np
import matplotlib.pyplot as plt
import random

import scipy.spatial # Pour comparer nos résultats avec scipy.spatial.Delaunay

# Données
# points = np.array([[0,0],[1,0],[1,1],[0,1],[0.5,0.5],[0.5,1.5],[1.5,1.5],[1.5,0.5]])  # Basique

N, seed = 50, 17  # Exemple pour enveloppe convexe
N, seed = 10, 19  # Exemple pour triangulation
N, seed = 30, 27  # Exemple pour triangulation
N, seed = 20, 31  # Exemple pour Delaunay
N, seed = 100, 34  # Exemple pour Delaunay
N, seed = 10, 40  # Exemple pour Voronoi
# N, seed = 100, 43  # Exemple pour Voronoi

# N, seed = 7, 12  # Exemple 1
# N, seed = 10, 13  # Exemple 1
random.seed(seed)
points = np.array([[random.random(), random.random()] for i in range(N)])  # Aléatoire


# Partie A : routines préliminaires

# Tri
def trier(points):
    """ Trie les points par abscisse croissante,
     si égalité abscisse ordonne par ordonnée croissante """
    return points[np.lexsort((points[:,1], points[:,0]))]

# newpoints = trier(points)
# print(newpoints)


def determinant(P,Q,R):
    """ Renvoie le déterminant de la matrice (Q-P,R-P)
    si > 0, triangle P Q R est orienté dans le sens trigo, 
    si < 0 dans le sens horaire, 
    si = 0 points alignés """
    return (Q[0]-P[0])*(R[1]-P[1])-(Q[1]-P[1])*(R[0]-P[0])


def barycentrique(P,A,B,C):
    """ Renvoie les coordonnées barycentriques (alpha:beta:gamma) de P dans le triangle ABC """

    aire = determinant(A,B,C)  # aire totale
    
    alpha = determinant(P,B,C)/aire
    beta = determinant(A,P,C)/aire
    gamma = 1-alpha-beta    # gamma = determinant(A,B,P)/aire

    return alpha, beta, gamma


def cercle_circonscrit(A,B,C):
    """ Renvoie le centre et le rayon du cercle circonscrit au triangle ABC """

    M = np.array([  [A[0], A[1], 1],
                    [B[0], B[1], 1],
                    [C[0], C[1], 1],])
    
    S = np.linalg.det(M)
    
    Mx = np.array([ [A[0]**2+A[1]**2, A[1], 1],
                    [B[0]**2+B[1]**2, B[1], 1],
                    [C[0]**2+C[1]**2, C[1], 1],])
    
    My = np.array([ [A[0]**2+A[1]**2, A[0], 1],
                    [B[0]**2+B[1]**2, B[0], 1],
                    [C[0]**2+C[1]**2, C[0], 1],])
    

    if abs(S) < 1.0e-6:
        return (None, np.inf)
    
    # Center of circle
    cx = np.linalg.det(Mx) / (2*S)
    cy = -np.linalg.det(My) / (2*S)
    
    r = np.sqrt((cx - A[0])**2 + (cy - A[1])**2)
    return ((cx, cy), r)


# Test d'affichage
def affiche_cercle_circonscrit(A,B,C):  
    """ Affiche le cercle circonscrit au triangle ABC """
    centre, rayon = cercle_circonscrit(A,B,C)
    print(centre, rayon)
    if centre is not None:
        cercle = plt.Circle(centre, rayon, color='r', fill=False)
        ax = plt.gca()
        ax.add_artist(cercle)
        plt.plot([A[0],B[0],C[0],A[0]],[A[1],B[1],C[1],A[1]],'b')
    plt.axis('equal')
    plt.show()
    return

# A = np.array([0,0])
# B = np.array([1.5,0])
# C = np.array([0.5,1.5])
# affiche_cercle_circonscrit(A,B,C)


# Partie B : algorithme de l'emballage 

def enveloppe(points):
    """ Renvoie l'enveloppe convexe des points """
    # Tri des points
    points = trier(points)
    # Initialisation
    n = len(points)
    enveloppe = [points[0]]   # point le plus à gauche
    p = 0  # index point de départ

    while True: 
        q = (p+1) % n  # index du point suivant
        for r in range(n):  # On cherche le point suivant de l'enveloppe
            if r!=p and r!=q and determinant(points[p],points[q],points[r]) > 0:
                q = r

        p = q  # On recommence à partir de là
        if p == 0:  # Si on est revenu au point de départ
            break   # On a fait le tour, on arrête
        enveloppe.append(points[q])  # On ajoute le point suivant

    return np.array(enveloppe)


def index_enveloppe(points):
    """ Variante qui renvoie les index des points formant l'enveloppe convexe"""
    # Tri des points
    points = trier(points)
    # Initialisation
    n = len(points)
    index_enveloppe = [0]   # point le plus à gauche
    p = 0  # index point de départ

    while True:  # Tant qu'on a pas fait le tour
        q = (p+1) % n  # index du point suivant
        for r in range(n):  # On cherche le point suivant de l'enveloppe
            if r!=p and r!=q and determinant(points[p],points[q],points[r]) > 0:
                q = r

        p = q  # On recommence à partir de là
        if p == 0:  # Si on est revenu au point de départ
            break   # On a fait le tour, on arrête
        index_enveloppe.append(q)  # On ajoute le point suivant

    return index_enveloppe


# Affichage des points
def affiche_enveloppe(points):
    """ Affiche les points """
    plt.scatter(points[:,0], points[:,1], color='blue')
    conv = enveloppe(points)
    plt.fill(conv[:,0], conv[:,1], edgecolor='red', fill=False, linewidth=2)

    # points = trier(points)
    # for i in range(len(points)):
    #     plt.text(points[i,0], points[i,1], str(i))

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    # plt.savefig('enveloppe.png', dpi=300)
    plt.show()

# affiche_enveloppe(points)


# Partie C : triangulation d'un ensemble de points

def quel_triangle(P, triangles, points):
    """ Renvoie l'indice du triangle contenant le point P
    ou None si le point n'est pas dans un triangle """
    for i in range(len(triangles)):
        A = points[triangles[i][0]]
        B = points[triangles[i][1]]
        C = points[triangles[i][2]]
        bar = barycentrique(P,A,B,C)
        if bar is not None:
            alpha, beta, gamma = barycentrique(P,A,B,C)
            if alpha >= 0  and beta >= 0  and gamma >= 0:
                return i
    return None


def triangulation(points):
    """ Calcule une triangulation 
    renvoie une liste de triplets d'indices de points, 
    un triplet correspond à un triangle """

    points = trier(points)  # Tri des points
    index_bord = index_enveloppe(points)  # Enveloppe convexe

    # print(index_bord)
    
    n = len(points)  # Nombre de points
    if n < 3:  # Si moins de 3 points
        return []  # Pas de triangle
    

    index_points_restant = [i for i in range(n) if i not in index_enveloppe(points)]  # Index des points intérieurs
    
    if len(index_points_restant) == 0:  # Si tous les points sont sur l'enveloppe

        # On commence par fixer un point (le premier de l'enveloppe convexe)
        # et on forme des triangles avec les points restants de l'enveloppe convexes
        triangles = [[index_bord[0], index_bord[i], index_bord[i+1]] for i in range(1,len(index_bord)-1)]

        return triangles
    
    p = random.choice(index_points_restant)  # On prend un point restant (qu'on retire de la liste)
    index_points_restant.remove(p)

    # On forme des triangles avec le points et les points de l'enveloppe convexe

    b = len(index_bord)
    triangles = [ [p, index_bord[i], index_bord[i+1]] for i in range(0,b-1)] 
    triangles.append( [p, index_bord[b-1], index_bord[0]] )

    while len(index_points_restant) > 0:
        p = index_points_restant.pop()  # On prend un point restant (qu'on retire de la liste)
        P = points[p]  # On récupère ses coordonnées
        indT = quel_triangle(P, triangles, points)  # On cherche le triangle contenant P
        # print(indT)
        a, b, c = triangles[indT]  # On récupère les indices des points du triangle

        # On calcule les coordonnées barycentriques de P dans le triangle
        A, B, C = points[a], points[b], points[c]

        triangles.pop(indT)  # On retire ce triangle de la liste
        triangles.append([a,b,p])  # On ajoute les 3 triangles formés par P
        triangles.append([b,c,p])
        triangles.append([c,a,p])

    return triangles


# Affichage triangulation
def affiche_triangulation(points):
    """ Affiche les points et la triangulation """
    
    points = trier(points)
    
    # for i in range(len(points)):
    #     plt.text(points[i,0], points[i,1], str(i))   

    plt.scatter(points[:,0], points[:,1], color='blue')

    triangles = triangulation(points)
    # print(triangles)
    # print(points.shape)
    for t in triangles:
        plt.fill(points[t,0], points[t,1], fill=False, linewidth=2)
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    # plt.savefig('triangulation02.png', dpi=300)
    plt.show()

# affiche_triangulation(points)


# Partie D : Triangulation de Delaunay

def dans_cercle(A,B,C,D):
    """ Vérifie si D est à l'intérieur du cercle circonscrit à ABC """
    if determinant(A,B,C) < 0:  
        A, B = B, A    # on s'arrange pour que ABC soit orienté positivement

    M = np.array([ [A[0]**2+A[1]**2, A[0], A[1], 1],
                     [B[0]**2+B[1]**2, B[0], B[1], 1],
                        [C[0]**2+C[1]**2, C[0], C[1], 1],
                            [D[0]**2+D[1]**2, D[0], D[1], 1] ])
    
    return np.linalg.det(M) > 0


# Test
# A = np.array([0,0])
# B = np.array([1,0])
# C = np.array([0,1])
# D = np.array([1,3])
# # A, B = B, A
# print(dans_cercle(A,B,C,D))



def mauvaise_arete(points, triangles):
    """ Renvoie une arête interne nécessitant un basculement 
    sous la forme d'une liste ((a,b,c,d),t,tt) 
    où a,b,c,d sont les indices des points du quadrilatères 
    et b,c est l'arête à basculer en a,d,
     t et tt sont les indices des triangles partageant l'arête b,c """

    for t in triangles:
        for tt in triangles:
            if len(set(t).intersection(set(tt))) == 2:  # On cherche les triangles partageant une arête
                b,c = set(t).intersection(set(tt))
                a = set(t).difference(set(tt)).pop()
                d = set(tt).difference(set(t)).pop()

                A, B, C, D = points[a], points[b], points[c], points[d]
                if dans_cercle(A,B,C,D):  # On vérifie si le quadrilatère est convexe
                    # print(a,b,c,d)
                    return ((a,b,c,d),t,tt)  # On ne garde que les arêtes nécessitant un basculement

    return None  # Si aucune arête n'est mauvaise, on renvoie None


# Test  
# points = np.array([[0,0], [1.2,0], [0,1], [1,1.2]])
# triangles = [[0,1,2], [1,2,3]]
# print(mauvaise_arete(points, triangles))

def delaunay(points, triangles):
    """ Renvoie une triangulation de Delaunay à partir d'une triangulation quelconque """

    abasculer = mauvaise_arete(points, triangles)
    while abasculer != None:
        (a,b,c,d), t, tt = abasculer
        triangles.remove(t)
        triangles.remove(tt)
        triangles.append([a,d,b])
        triangles.append([a,d,c])
        abasculer = mauvaise_arete(points, triangles)

    return triangles


# Affichage triangulation de Delaunay
def affiche_delaunay(points):
    """ Affiche les points et la triangulation avant et après les basculements"""

    # Points
    points = trier(points)

    triangles = triangulation(points)
    newtriangles = delaunay(points,triangles)

    for t in newtriangles:
        plt.fill(points[t,0], points[t,1], fill=False, linewidth=1)

    plt.scatter(points[:,0], points[:,1], color='blue')
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    # plt.savefig('delaunay02.png', dpi=300)
    plt.show()
    return

# Affichage triangulation via librairie scipy
def affiche_scipy_delaunay(points):
    """ Affiche les points et la triangulation """

    ### Triangulation de Delaunay
    plt.scatter(points[:,0], points[:,1], color='blue')
    
    scipy_triangles = scipy.spatial.Delaunay(points)
    plt.triplot(points[:,0], points[:,1], scipy_triangles.simplices)

    plt.axis('equal')
    # plt.set_xlim(-0.1,1.1)
    # plt.set_ylim(-0.1,1.1)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    return


# Test
# points = np.array([[0,0], [1.2,0], [0,1], [1,1.3]])
# affiche_delaunay(points)
# affiche_scipy_delaunay(points) # pour comparer avec la librairie scipy

# Partie E : diagramme de Voronoi

def dual(points, triangles):
    """ Renvoie le dual d'une triangulation, sous la forme
    d'une liste  (sommet, liste de sommets voisins) """ 

    # Centre des cercles circonscrits
    centres = [cercle_circonscrit(points[t[0]], points[t[1]], points[t[2]])[0] for t in triangles]
    voisins = [[] for _ in range(len(centres))]

    # Arêtes du dual
    for i in range(len(triangles)):
        t = triangles[i]
        for j in range(len(triangles)):
            tt = triangles[j]
            if len(set(t).intersection(set(tt))) == 2:
                voisins[i].append(centres[j])

    graphe_dual = [ [centres[i], voisins[i]] for i in range(len(centres))]
    return graphe_dual



def affiche_voronoi(points):
    """ Affiche les celulles de Voronoi d'un ensemble de points """

    points = trier(points)
    triangles = triangulation(points)
    newtriangles = delaunay(points,triangles)
    graphe_dual = dual(points, newtriangles)


    for t in newtriangles:
        plt.fill(points[t,0], points[t,1], fill=False, linewidth=1)

    plt.scatter(points[:,0], points[:,1], color='black')

    for c, vois in graphe_dual:
        for v in vois:
            plt.plot([c[0], v[0]], [c[1], v[1]], color='green')
        plt.scatter(c[0], c[1], color='green')


    # plt.set_xlim(-0.1,1.1)
    # plt.set_ylim(-0.1,1.1)
    plt.axis('equal')
    plt.axis('off')   

    plt.tight_layout()
    # plt.savefig('voronoi01a.png', dpi=300)
    plt.show()
    return
 

# Test  
# points = np.array([[0,0], [1.5,0], [0.3,0.7], [1,1.1]])
# triangles = [[0,1,2], [1,2,3]]


# https://stackoverflow.com/questions/20515554/ by pv
# because scipy.spatial.voronoi_plot_2d does not work for me
def voronoi_finite_polygons_2d(vor, radius=None):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.   """

    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge

            t = vor.points[p2] - vor.points[p1] # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]

        # finish
        new_regions.append(new_region.tolist())

    return new_regions, np.asarray(new_vertices)


def affiche_scipy_voronoi(points):
    vor = scipy.spatial.Voronoi(points)
    regions, vertices = voronoi_finite_polygons_2d(vor)

    # colorize
    for region in regions:
        polygon = vertices[region]
        plt.fill(*zip(*polygon), alpha=0.4, color=np.random.rand(3,))

    plt.scatter(points[:,0], points[:,1], color='black', s=20)

    # Pour voir l'intégralité des cellules
    # plt.xlim(vor.min_bound[0] - 0.1, vor.max_bound[0] + 0.1)
    # plt.ylim(vor.min_bound[1] - 0.1, vor.max_bound[1] + 0.1)
    # plt.axis('equal')

    # Pour voir les cellules qui sont dans le carré
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.3, 1.3)

    plt.axis('off')
    plt.tight_layout()
    plt.savefig('voronoi01b.png', dpi=300)
    plt.show()
    return

# affiche_voronoi(points)
affiche_scipy_voronoi(points)
