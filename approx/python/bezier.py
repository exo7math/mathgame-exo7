# Courbes de Bézier

import matplotlib.pyplot as plt
import numpy as np

# Coefficients binomiaux
def binomial(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    if k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

# Polynôme de Bernstein
# Bien sûr une mise en oeuvre efficace ne devrait pas calculer ces polynômes plusieurs fois
def bernstein(n, k, t):
    return binomial(n, k) * t**k * (1 - t)**(n - k)

# Courbe de Bézier
def bezier(points, t):
    n = len(points) - 1
    return sum([bernstein(n, k, t) * points[k] for k in range(n + 1)])

# Tracer la courbe de Bézier
def trace_bezier(points, N=100, construction=False):

    list_x, list_y = [], []
    for t in np.linspace(0, 1, N):
        x,y = bezier(points, t)
        list_x.append(x)
        list_y.append(y)
    
    plt.plot(list_x, list_y, color='red', lw=3)

    if construction:
        plt.plot(points[:,0], points[:,1], color='gray')
        plt.plot(points[:,0], points[:,1], 'o', color='black')

    return


# Exemples
def exemple1():
    points = np.array([(0, 0), (0, 1), (2, 0)])
    trace_bezier(points)
    plt.axis('equal')
    plt.show()   

def exemple2():
    points = np.array([(0, 0), (1, 0), (2,2), (2, 0)])
    trace_bezier(points)
    plt.axis('equal')
    plt.show() 

def exemple3():
    points = np.array([(0,-1), (1,-1), (2,2), (2, 0), (3,-1), (4,3)])
    trace_bezier(points, construction=True)

    plt.axis('off')
    plt.tight_layout() 
    # plt.savefig('approx-bezier-01.png',dpi=600) 
    plt.show() 


exemple3()


# Dérivée du polynôme de Bernstein
def diff_bernstein(n, k, t):
    if k==0:
        diff = -n * (1-t)**(n-1)
    elif k==n:
        diff = n * t**(n-1)
    else:
        diff = binomial(n, k) * ( k * t**(k-1)*(1-t)**(n-k) - (n-k) * t**k * (1 - t)**(n - k - 1) )
    return diff

# Courbe de Bézier et vecteurs tangent et normal
def bezier_vecteurs(points, t):
    n = len(points) - 1
    x,y = bezier(points, t)
    vect_tangent = sum([diff_bernstein(n, k, t) * points[k] for k in range(n + 1)])
    vect_tangent_normalized = vect_tangent / np.linalg.norm(vect_tangent)
    vect_normal = np.array([-vect_tangent_normalized[1], vect_tangent_normalized[0]])
    return x,y, vect_tangent_normalized, vect_normal 


# Tracer la courbe de Bézier
def trace_bezier_vecteurs(points, N=50, construction=False, epsilon = 1):

    list_x, list_y = [], []
    for t in np.linspace(0, 1, N):
        x, y = bezier(points, t)
        list_x.append(x)
        list_y.append(y)

    plt.plot(list_x, list_y)

    for t in np.linspace(0, 1, N//5):
        x, y, vect_tangent, vect_normal = bezier_vecteurs(points, t)

        plt.arrow(x, y, epsilon*vect_tangent[0], epsilon*vect_tangent[1], color='green', width=.02)
        plt.arrow(x, y, epsilon*vect_normal[0], epsilon*vect_normal[1], color='blue', width=.02)    

    if construction:
        plt.plot(points[:,0], points[:,1], color='red')
        plt.plot(points[:,0], points[:,1], 'o', color='orange')

    return 

def exemple4():
    points = np.array([(0, 0), (1, 0), (1, 3), (5,2), (5,-2)])
    x, y, vect_tangent, vect_normal = bezier_vecteurs(points, 0)
    print(vect_tangent, vect_normal)

    G = trace_bezier_vecteurs(points, construction=True, epsilon = 0.5)
    plt.axis('equal')
    plt.show() 

# exemple4()


# Courbe de Bézier récursive
def bezier_recursif(points, t):
    n = len(points) - 1
    if n == 0:
        return points[0]
    else:
        return (1 - t) * bezier_recursif(points[:n], t) + t * bezier_recursif(points[1:], t)  


# Tracer la courbe de Bézier version récursive
def trace_bezier_recursif(points, N=100, construction=False):
    
    list_x, list_y = [], []
    for t in np.linspace(0, 1, N):
        x,y = bezier_recursif(points, t)
        list_x.append(x)
        list_y.append(y)
    
    plt.plot(list_x, list_y)

    if construction:
        plt.plot(points[:,0], points[:,1], color='red')
        plt.plot(points[:,0], points[:,1], 'o', color='orange')

    return

def exemple5():
    points = np.array([(0, 0), (1, 0), (2,2), (2, 0), (1,-1)])
    G = trace_bezier_recursif(points, construction=True)
    plt.axis('equal')
    plt.show() 

# exemple5()