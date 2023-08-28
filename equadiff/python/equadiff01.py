# Solutions numérique des équations différentielles
# Version pédagogique pour le cours

import numpy as np

# Méthode d'Euler pour le cours
def euler_cours(f, x0, y0, x1, n):
    x = x0
    y = y0
    h = (x1-x0)/n
    list_y = [y0]
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        list_y.append(y)
    return list_y

# Exemple 1 - Pour le cours  : y' = 1/(2*y), y(1) = 1, solution y(x) = sqrt(x)
def exemple1(n):
    f = lambda x, y: 1/(2*y)
    x0 = 1
    x1 = 2
    y0 = 1
    h = 1/n
    list_y = euler_cours(f, x0, y0, x1, n)

    print("y' = y, y(0) = 1")
    print("n = ", n)
    print("Méthode d'Euler")
    print(list_y)
    print("y(2) approché = ", list_y[-1])
    print("y(2) exact    = ", np.sqrt(2))

exemple1(n=100)
