# Création du logo mathgame en svg

import drawsvg as draw
import numpy as np

def draw_face(d, face, col='#ee2244'):
    """ Draw one face of a cube """
    d.append(draw.Lines(face[0][0], face[0][1],
                        face[1][0], face[1][1],
                        face[2][0], face[2][1],
                        face[3][0], face[3][1],
                        close=True,
                        fill=col,
                        fill_opacity=1,
                        stroke_width=1.5,
                        stroke='#444444'))
    
    return

def perspective_lineaire(P,C):
    """ Calcule l'image du point P sur le plan (Oyz) c-à-d (x=0), par la persepective linéaire centrée en C """
    x, y, z = P
    xc, yc, zc = C

    if x == xc:
        return (+inf,+inf,0)

    k = -xc/(x-xc)
    X = k*(y-yc) + yc
    Y = k*(z-zc) + zc

    return (X,Y)

def projection_orthogonale(x,y,z,phi,mylambda):
    """ Projection orthogonale de (x,y,z) sur le plan orthogonal au vecteur dirigé 
    par latitude phi et longitude lambda """

    M1 = np.matrix([[0, 0, 0], [0, 1, 0], [0, 0, 1]])  # projection sur (Oyz) (donc (x=0))
    M2 = np.matrix([[np.cos(-phi), 0, np.sin(-phi)], [0, 1, 0], [-np.sin(-phi),0,np.cos(-phi)]])  # rotation axe y du plan d'angle -phi
    M3 = np.matrix([[np.cos(-mylambda), -np.sin(-mylambda), 0], [np.sin(-mylambda), np.cos(-mylambda), 0], [0, 0, 1]])  # rotation axe z du plan d'angle -lambda

    M = M1 * M2 * M3

    # print(M)

    vX = np.array([[x],[y],[z]])
    vY = M * vX
    X, Y, Z = vY.item(0), vY.item(1), vY.item(2), 
    return (X,Y,Z)



def perspective(P):
    """ Perspective projection of a 3D point """

    # Perspecitve 1 : linear perspective
    # C =(10, -3, 5)
    # Q = perspective_lineaire(P, C)

    #  Orthogonal projection
    # phi, mylambda = 0.30, 0.25
    phi, mylambda = 0.25, 0.25

    Q = projection_orthogonale(*P, phi, mylambda)

    return Q[1], Q[2]


def perspective_cube(scale=1, T=(0, 0, 0)):
    """ Draw a cube using a perspective projection 
    The cube is centered at (0,0,0) and has edge length 1
    A scale factor can be applied to the cube and (after scaling) a translation T """

    # 8 vertices defining a cube centered at (0,0,0)
    vertices = [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]

    # Dividing by 2 to have edge length 1
    vertices = [[X/2 for X in P] for P in vertices]

    # Scaling
    vertices = [[scale * X for X in P] for P in vertices]

    # Translation
    vertices = [ [P[0]+T[0], P[1]+T[1], P[2]+T[2]] for P in vertices]


    # 6 faces
    comb_faces = [
        [0, 1, 2, 3],
        # [4, 5, 6, 7],
        # [0, 1, 5, 4],
        [1, 2, 6, 5],
        [2, 3, 7, 6],
        # [3, 0, 4, 7]
    ]

    proj_vertices = [perspective(v) for v in vertices]
    proj_faces = [[proj_vertices[i] for i in face] for face in comb_faces]

    # print(proj_vertices)
    # print(proj_faces)

    return proj_faces

     
# perspective_cube()
    
def translate(cube, T):
    """ Translate a projected cube """    
    tcube = []
    for face in cube:
        tface = [ [P[0]+T[0], P[1]+T[1]]  for P in face]
        tcube.append(tface)
    return tcube

def scale(cube, s):
    """ Scale a projected cube """
    scube = []
    for face in cube:
        sface = [[s * Q for Q in vertices] for vertices in face]
        scube.append(sface)
    return scube



def draw_cube(d, cube):
    """ Draw a cube """
    cols = ['#aa2244', '#ee2244', '#772244', '#ffff00', '#ff00ff', '#00ffff']
    for i, face in enumerate(cube):
        draw_face(d, face, cols[i])
    return

def pixel_art():
    """ Pixel art 3D """

    # Four pixels define by their center (in plane (x=0))
    # pix = [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1]]

    # Space invaders
    # invader = [
    #         [0,0,1,0,0,0,0,0,1,0,0],
	# 		[1,0,0,1,0,0,0,1,0,0,1],
	# 		[1,0,1,1,1,1,1,1,1,0,1],
	# 		[1,1,1,0,1,1,1,0,1,1,1],
	# 		[1,1,1,1,1,1,1,1,1,1,1],
	# 		[0,1,1,1,1,1,1,1,1,1,0],
	# 		[0,0,1,0,0,0,0,0,1,0,0],
	# 		[0,1,0,0,0,0,0,0,0,1,0]]
    invader = [
            [0,0,1,0,0,0,0,1,0,0],
			[1,0,0,1,0,0,1,0,0,1],
			[1,0,1,1,1,1,1,1,0,1],
			[1,1,1,0,1,1,0,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[0,1,1,1,1,1,1,1,1,0],
			[0,0,1,0,0,0,0,1,0,0],
			[0,1,0,0,0,0,0,0,1,0]]   

    # invader.reverse()

    pix = []
    for j in range(len(invader)):
        for i in reversed(range(len(invader[j]))):
            if invader[j][i] == 1:
                pix.append([0, i, j])

    # pix = [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1]]
    pix.reverse()

    return pix


def draw_logo():
    d = draw.Drawing(800, 700, origin=(-375,-300))
    
    pix = pixel_art()
    delta = 0.0  # gap between pixels cubes
    list_cubes = []
    for T in pix:
        cube = perspective_cube(1-delta, T)
        cube = translate(cube, (-4, -3))
        list_cubes.append(cube)

    # cube = perspective_cube()
    for cube in list_cubes:
        scube = scale(cube, 70)
        draw_cube(d, scube)

    d.set_pixel_scale(1)
    d.save_svg('logo_mathgame_output.svg')
    return

draw_logo()




    
    