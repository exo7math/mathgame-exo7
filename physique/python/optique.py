# Réflexion et réfraction de rayons

### Partie A
### Réflexion d'un rayon

import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

# Réflexion dans un rectangle
def reflexion_rectangle(x0, y0, theta, a, b, nbreflex = 10):
    """ Trace un rayon partant du point (x, y) et d'angle theta
    dans un rectangle de largeur a et de hauteur b
    nbreflex est le nombre de réflexions à tracer
    """

    liste_x = [x0]
    liste_y = [y0]
    x = x0
    y = y0

    for i in range(nbreflex):
            
        # Calcule de l'intersection avec le rectangle
        # Intersection avec face 0 : bas (y=0)
        tb = -y / np.sin(theta)
        # Intersection avec face 1 : droite (x=a)
        td = (a - x) / np.cos(theta)
        # Intersection avec face 2 : haut (y=b)
        th = (b - y) / np.sin(theta)
        # Intersection avec face 3 : gauche (x=0)
        tg = -x / np.cos(theta)
        # Quelle face touchée en premier ?
        # Correspond au plus petit paramètre t positif
        t = min([t for t in [tb, td, th, tg] if t > 0])
        rang = [tb, td, th, tg].index(t)

        # Coordonnées de l'intersection
        match rang:
            case 0:
                x = x + t * np.cos(theta)
                y = 0
                theta = -theta 

            case 1:
                x = a
                y = y + t * np.sin(theta)
                theta = np.pi - theta

            case 2:
                x = x + t * np.cos(theta)
                y = b
                theta = -theta

            case 3:
                x = 0
                y = y + t * np.sin(theta)
                theta = np.pi - theta

        liste_x.append(x)
        liste_y.append(y)


    # Le rectangle
    plt.plot([0, a, a, 0, 0], [0, 0, b, b, 0], 'k')

    # Le point initial
    plt.plot([x0], [y0], 'ro')

    # Le rayon
    plt.plot(liste_x, liste_y, 'b')

    # plt.plot([x, x + np.cos(theta)], [y, y + np.sin(theta)], 'r')

    plt.axis('off')
    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('optique-4.png', dpi=300)
    plt.show()
    return

# reflexion_rectangle(0.4, 0.5, np.pi / 7, 4, 2, 100)  


### Partie B
### Réfraction d'un rayon


# Réfraction le long d'une droite
def refraction_droite(x1, y1, theta1, n1, n2):
    """ Trace un rayon partant du point (x, y) et d'angle theta avec la verticale
    dans un milieu de réfraction n1 et sortant dans un milieu de réfraction n2
    la séparation du milieu est la droite (y = 0)
    """
    xm = y1 * np.tan(theta1)
    ym = 0

    # Loi de Snell-Descartes n1 sin(theta1) = n2 sin(theta2)
    theta2 = np.arcsin(n1 * np.sin(theta1) / n2)

    y2 = -(y1 - ym)
    x2 = xm - y2 * np.tan(theta2)


    # La frontière
    plt.plot([0,4], [0,0], 'g')

    # Le point initial
    plt.plot([x1], [y1], 'ro')

    # Le point d'intersection
    plt.plot([xm], [ym], 'ro')

    # Le point image
    plt.plot([x2], [y2], 'ro')

    # Le rayon
    plt.plot([x1, xm, x2], [y1, ym, y2], 'b')


    plt.axis('off')
    plt.axis('equal')
    # plt.savefig('refraction-2.png', dpi=300)   
    plt.tight_layout()

    plt.show()
    return


# refraction_droite(0, 2, np.pi / 4, n1 = 1, n2 = 1.5)

# Réfraction pour le cours
def refraction_cours():
    """ Trace un rayon partant du point (x, y) et d'angle theta avec la verticale
    dans un milieu de réfraction n1 et sortant dans un milieu de réfraction n2
    la séparation du milieu est la droite (y = 0)
    """
    x1, y1 = 0, 2
    n1 = 1
    n2 = 1.5

    for theta1 in np.linspace(np.pi/3, np.pi/8,10):
        xm = y1 * np.tan(theta1)
        ym = 0

        # Loi de Snell-Descartes n1 sin(theta1) = n2 sin(theta2)
        theta2 = np.arcsin(n1 * np.sin(theta1) / n2)

        y2 = -(y1 - ym)
        x2 = xm - y2 * np.tan(theta2)


        # La frontière
        plt.plot([0,4], [0,0], 'g')

        # Le point initial
        # plt.plot([x1], [y1], 'ro')

        # Le point d'intersection
        # plt.plot([xm], [ym], 'ro')

        # Le point image
        # plt.plot([x2], [y2], 'ro')

        # Le rayon
        plt.plot([x1, xm, x2], [y1, ym, y2], 'b')

    
    plt.axis('off')
    plt.axis('equal')
    # plt.savefig('refraction-2.png', dpi=300)   
    plt.tight_layout()

    plt.show()
    return

# refraction_cours()



# Indice de réfraction en fonction de la longueur d'onde dans le verre
def indice_verre(mylambda):
    """ Retourne l'indice de réfraction du verre pour une longueur d'onde mylambda en micrometres
        https://en.wikipedia.org/wiki/Cauchy%27s_equation
    """
    return 1.4580 + 0.0354 / (mylambda ** 2)


def wavelength_to_rgb(wavelength, gamma=0.8):
    """"
    https://stackoverflow.com/questions/44959955/matplotlib-color-under-curve-based-on-spectral-color
    taken from http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
    This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).
    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    Additionally alpha value set to 0.5 outside range
    """
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 750:
        A = 1.
    else:
        A=0.5
    if wavelength < 380:
        wavelength = 380.
    if wavelength >750:
        wavelength = 750.
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R,G,B,A)



# Réfraction le long d'une droite de la lumière
def refraction_droite_lumiere(x1, y1, theta1, n1=1):

    xm = y1 * np.tan(theta1)
    ym = 0

    # Le point initial
    plt.plot([x1], [y1], 'ro')

    # Le point d'intersection
    plt.plot([xm], [ym], 'ro')

    # Le rayon (début)
    plt.plot([x1, xm], [y1, ym], 'b')


    for mylambda in np.arange(0.4, 0.8, 0.01):

        n2 = indice_verre(mylambda)

        # Loi de Snell-Descartes n1 sin(theta1) = n2 sin(theta2)
        theta2 = np.arcsin(n1 * np.sin(theta1) / n2)

        y2 = -(y1 - ym)
        x2 = xm - y2 * np.tan(theta2)

        # Le point image
        # plt.plot([x2], [y2], 'ro')

        # Le rayon (fin)
        couleur = wavelength_to_rgb(mylambda * 1000)
        plt.plot([xm, x2], [ym, y2], color=couleur)


    plt.axis('equal')
    plt.tight_layout()

    plt.show()
    return   

# refraction_droite_lumiere(0, 2, np.pi / 5)    


def intersection_droite (xA, yA, xB, yB, xC, yC, xD, yD):
    """ Retourne les coordonnées du point d'intersection entre les droites AB et CD
    """
    det = (yD - yC) * (xB - xA) - (xD - xC) * (yB - yA)
    if det == 0: # Les droites sont parallèles
        return (None, None)
    else:
        num = (xD - xC) * (yA - yC) - (yD - yC) * (xA - xC)
        ua = num / det
        x = xA + ua * (xB - xA)
        y = yA + ua * (yB - yA)
        return (x, y)




# Réfraction dans un prisme
def refraction_prisme(x1=-2, y1=0.25, alpha=0):
    """ Le prisme est un triangle equilatéral, de base 2, centré sur (x=0)
    alpha est l'angle avec horizontale
    """

    n1 = 1  # Indice de réfraction de l'air

    # Intersection avec la première face du prisme 
    # qui passe par les point (-1,0) et (0,sqrt(3))
    x2, y2 = intersection_droite(x1, y1, x1 + np.cos(alpha), y1 + np.sin(alpha), -1, 0, 0, np.sqrt(3))
    theta1 = np.pi/6 + alpha  # Angle avec la normale à la face


    for mylambda in np.arange(0.4, 0.8, 0.01):

        # rayon dans le prisme
        n2 = indice_verre(mylambda)
        # n2 = 1

        # Loi de Snell-Descartes n1 sin(theta1) = n2 sin(theta2)
        theta2 = np.arcsin(n1 * np.sin(theta1) / n2)


        alpha2 = -np.pi/6 + theta2

        # intersection rayon avec la second face
        x3, y3 = intersection_droite(x2, y2, x2 + np.cos(alpha2), y2 + np.sin(alpha2) , 0, np.sqrt(3), 1, 0)

        # Le point de sortie
        # plt.plot([x3], [y3], 'ro')

        # Le rayon (milieu)
        couleur = wavelength_to_rgb(mylambda * 1000)
        plt.plot([x2, x3], [y2, y3], color=couleur)
        
        # Le rayon (fin)
        theta2bis = -np.pi/6 + alpha2  # angle entrée avec la normale à la seconde face
        # print(theta2bis)
        theta3 = np.arcsin(n2 * np.sin(theta2bis) / n1)  # angle sortie avec la normale à la seconde face
        alpha3 = np.pi/6 + theta3 # angle sortie avec l'horizontale
        x4 = x3 + 1.5*np.cos(alpha3)
        y4 = y3 + 1.5*np.sin(alpha3)
        # plt.plot([x4], [y4], 'bo')

        # Le rayon (fin)
        couleur = wavelength_to_rgb(mylambda * 1000)
        plt.plot([x3, x4], [y3, y4], color=couleur, linewidth=4)





    # Affiche le prisme
    plt.plot([-1, 0, 1, -1], [0, np.sqrt(3), 0, 0], 'k')

    # Le point initial
    # plt.plot([x1], [y1], 'ro')

    # Le point d'intersection avec la première face
    # plt.plot([x2], [y2], 'ro')

    # Le rayon (début)
    plt.plot([x1, x2], [y1, y2], 'b')



    plt.axis('off')
    plt.axis('equal')
    plt.tight_layout()
    # plt.savefig('prisme.png', dpi=600)

    plt.show()
    return  


# Vérifier les angles de sorties
refraction_prisme(alpha=0.4)