# Solutions numérique des équations différentielles
# Euler, RK2, RK4

import numpy as np

# Méthode d'Euler
def euler(f, x0, y0, x1, n):
    h = (x1-x0)/n
    x = x0
    y = y0
    while x < x1:
        y = y + h * f(x, y)
        x = x + h
    return y


# Méthode Runge-Kutta d'ordre 2
def rungekutta2(f, x0, y0, x1, n):
    h = (x1-x0)/n
    x = x0
    y = y0
    while x < x1:
        k1 = f(x, y)
        k2 = f(x + h, y + k1*h)
        y = y + h/2 * (k1 + k2)       
        x = x + h
    return y


# Méthode de Runge-Kutta d'ordre 4
def rungekutta4(f, x0, y0, x1, n):
    h = (x1-x0)/n
    x = x0
    y = y0
    while x < x1:
        k1 = f(x, y)
        k2 = f(x + h/2, y + k1*h/2)
        k3 = f(x + h/2, y + k2*h/2)
        k4 = f(x + h, y + k3*h)
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
    return y
    

# Exemple 1 : y' = y, y(0) = 1 : solution y(x) =exp(x)
def exemple1(n):
    f = lambda x, y: y
    x0 = 0
    y0 = 1
    x1 = 1
    print("y' = y, y(0) = 1")
    print("nb itération = ", n)
    print("Méthode d'Euler")
    print("y(1) approché = ", euler(f, x0, y0, x1, n))
    print("Méthode de Runge-Kutta d'ordre 2")
    print("y(1) approché = ", rungekutta2(f, x0, y0, x1, n))
    print("Méthode de Runge-Kutta d'ordre 4")
    print("y(1) approché = ", rungekutta4(f, x0, y0, x1, n))
    print("y(1) exact    = ", np.exp(1))

# exemple1(h=0.01)


# Exemple 2 : y' = 1/(2*y), y(1) = 1, solution y(x) = sqrt(x)
def exemple2(n):
    f = lambda x, y: 1/(2*y)
    x0 = 1
    y0 = 1
    x1 = 2
    print("y' = y, y(0) = 1")
    print("nb itérations = ", n)
    print("Méthode d'Euler")
    print("y(2) approché = ", euler(f, x0, y0, x1, n))
    print("Méthode de Runge-Kutta d'ordre 2")
    print("y(2) approché = ", rungekutta2(f, x0, y0, x1, n))
    print("Méthode de Runge-Kutta d'ordre 4")
    print("y(2) approché = ", rungekutta4(f, x0, y0, x1, n))
    print("y(2) exact    = ", np.sqrt(2))

    print(euler(f, x0, y0, x1, n))
    print(rungekutta2(f, x0, y0, x1, n))
    print(rungekutta4(f, x0, y0, x1, n))

    return



exemple2(10)
exemple2(100)

