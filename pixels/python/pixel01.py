from math import *

from matplotlib import pyplot as plt
import matplotlib.patches as patches

### Affichage
def affiche_pixels(liste_pixels, plot_true_line=True):

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    # ax = fig.add_subplot(111)


    # Pixels tous noirs
    if len(liste_pixels[0])==2:

        xmin = min([x for (x,y) in liste_pixels])
        xmax = max([x for (x,y) in liste_pixels])
        ymin = min([y for (x,y) in liste_pixels])
        ymax = max([y for (x,y) in liste_pixels])

        for (i,j) in liste_pixels:
            rect = patches.Rectangle((i, j), 1, 1, color='blue')
            ax.add_patch(rect)

    # Pixels niveaux de gris
    if len(liste_pixels[0])==3:

        xmin = min([x for (x,y,c) in liste_pixels])
        xmax = max([x for (x,y,c) in liste_pixels])
        ymin = min([y for (x,y,c) in liste_pixels])
        ymax = max([y for (x,y,c) in liste_pixels])

        for (i,j,c) in liste_pixels:
            rect = patches.Rectangle((i, j), 1, 1, color=str(1-c))
            ax.add_patch(rect)



    # Vrai segment
    if plot_true_line:

        # Grille    
        for i in range(xmin, xmax+1):
            plt.vlines(i, ymin, ymax+1)
        for j in range(ymin, ymax+1):
            plt.hlines(j, xmin, xmax+1)

        plt.plot([xmin+0.5,xmax+0.5],[ymin+0.5,ymax+0.5],color="red")

    # plt.tight_layout()    
    # plt.savefig('nomfichier.png')  

    plt.xlim([xmin, xmax+1])
    plt.ylim([ymin, ymax+1])

    # plt.xlabel("Axe x")
    # plt.ylabel("Axe y")

    plt.show()


# Test
# affiche_pixels([(0,1),(1,2),(2,3),(3,4)])
# affiche_pixels([(0,1,0.1),(1,2,0.5),(2,3,0.2),(3,4,0.0)])

def affiche_pixels_cercle(liste_pixels, x0, y0, r, plot_true_circle=True):

    fig = plt.figure()
    ax = plt.axes(aspect='equal')
    # ax = fig.add_subplot(111)


    # Grille
    xmin = min([x for (x,y) in liste_pixels])
    xmax = max([x for (x,y) in liste_pixels])
    ymin = min([y for (x,y) in liste_pixels])
    ymax = max([y for (x,y) in liste_pixels])    


    # for i in range(xmin, xmax+1):
    #     plt.vlines(i, ymin, ymax+1)
    # for j in range(ymin, ymax+1):
    #     plt.hlines(j, xmin, xmax+1)


    for (i,j) in liste_pixels:
        rect = patches.Rectangle((i, j), 1, 1, color='blue')
        ax.add_patch(rect)


    # Vrai cercle
    if plot_true_circle:
        circ = patches.Circle((x0+0.5, y0+0.5), r, color='red', fill=None)
        ax.add_patch(circ)

    # plt.tight_layout()    
    # plt.savefig('nomfichier.png')  

    plt.xlim([xmin, xmax+1])
    plt.ylim([ymin, ymax+1])

    # plt.xlabel("Axe x")
    # plt.ylabel("Axe y")

    plt.show()



def segment_reel(x1, y1, x2, y2):
    """ Renvoie les pixels reliant (x1,y1) à (x2,y2).
    On suppose x1 < x2 et y1 < y2  et pente < 1"""

    pixels = []
    alpha = (y2-y1)/(x2-x1)
    for i in range(x1, x2+1):
        j = round(alpha*(i-x1)+y1)
        pixels.append( (i,j) )

    return pixels


# Test  
pix1 = segment_reel(0, 0, 17, 5)
# affiche_pixels(pix1)


def segment_reel_bis(x1, y1, x2, y2):
    """ Renvoie les pixel reliant (x1,y1) à (x2,y2).
    On suppose x1 < x2 et y1 < y2 et pente < 1"""

    pixels = []
    c = (y2-y1)/(x2-x1) 

    y = y1
    for i in range(x1, x2+1):
        j = round(y)
        pixels.append( (i,j) )
        y = y + c

    return pixels

# Test  
pix2 = segment_reel_bis(0, 0, 8, 3)
# affiche_pixels(pix2)
print(pix1==pix2)



def segment_bresenham(x1, y1, x2, y2):
    """ Renvoie les pixels reliant (x1,y1) à (x2,y2).
    On suppose x1 < x2 et y1 < y2  et pente < 1"""


    p = 2*(y2-y1)
    m = 2*(y2-y1)- 2*(x2-x1)

    d = 2*(y2-y1) - (x2-x1)

    pixels = []
    j = y1

    for i in range(x1, x2+1):
        pixels.append( (i, j) )
        if d < 0:     
            print(i,j,d,d+p)
            d = d+p   # same j
        else:
            print(i,j,d,d+m)

            j = j+1
            d = d+m

    return pixels

# Test  
pix3 = segment_bresenham(0, 0, 8, 5)
affiche_pixels(pix3)


print(pix1==pix3)

# pix4 = segment_bresenham(0, 0, 151, 67)
# affiche_pixels(pix4, plot_true_line=False)

def segment_antialiasing(x1, y1, x2, y2):
    """ Renvoie les pixels reliant (x1,y1) à (x2,y2).
    On suppose x1 < x2 et y1 < y2 et pente < 1"""

    pixels = []

    c = (y2-y1)/(x2-x1) 

    y = y1
    for i in range(x1, x2+1):
        j = floor(y)   # partie entière
        fy = y-j       # partie décimale
        pixels.append( (i,j,1-fy) )
        pixels.append( (i,j+1,fy) )

        y = y + c

    return pixels

# Test  
pix4 = segment_antialiasing(0, 0, 23, 16)
# affiche_pixels(pix4)



def arc_bresenham(x0, y0, r):
    """ Renvoie un arc de cercle de centre (x0, y0) de rayon r."""

    i = 0
    j = r
    d = 3-2*r
    pixels = []
    while i <= j:
        pixels.append( (i+x0, j+y0) )

        if d<0:
            d = d + 4*i+6
        else:
            d = d + 4*i-4*j+10
            j = j-1

        i = i+1

    return pixels

# Test  
# pix = arc_bresenham(0, 0, 50)
# affiche_pixels(pix)

def cercle_bresenham(x0, y0, r):
    """ Renvoie un arc de cercle de centre (x0, y0) de rayon r."""

    i = 0
    j = r
    d = 3-2*r
    pixels = []
    while i <= j:
        pixels.append( (i+x0, j+y0) )
        pixels.append( (j+x0, i+y0) )
        pixels.append( (-i+x0, j+y0) )
        pixels.append( (-j+x0, i+y0) )
        pixels.append( (i+x0, -j+y0) )
        pixels.append( (j+x0, -i+y0) )
        pixels.append( (-i+x0, -j+y0) )
        pixels.append( (-j+x0, -i+y0) )


        if d<0:
            d = d + 4*i+6
        else:
            d = d + 4*i-4*j+10
            j = j-1

        i = i+1



        # if m>0:
        #     j = j-1
        #     m = m-8*j
        # else:
        # i = i+1
        # m = m + 8*i+4

    return pixels


# Test  
x0, y0, r = 0, 0, 17
pix = cercle_bresenham(x0, y0, r)
# affiche_pixels_cercle(pix, x0, y0, r)