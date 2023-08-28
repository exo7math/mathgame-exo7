
##############################
# L-système
##############################

from turtle3d import *

pi = np.pi

##############################
# Activité 1 - Remplacer
##############################

def remplacer(mot,regles):
    """ Substitution de lettre par un ensemble de règles
    Chaque règle est du type (lettre : motif) """

    nouv_mot = ""
    for l in mot:
        if l in regles:
            nouv_mot = nouv_mot + regles[l]
        else:
            nouv_mot = nouv_mot + l

    return nouv_mot

# Test
# mot1 = "FrGrG"
# regles = {"F" :"FrGlFlGrF",
#           "G" : "GG" }
# mot2 = remplacer(mot1,regles)
# mot3 = remplacer(mot2,regles)
# print(mot1)
# print(mot2)
# print(mot3)


def iterer_lsysteme(mot, regles, k):
    
    for i in range(k):
        mot = remplacer(mot, regles)

    return mot



##############################
# Activité 2 - Tracer un L-système
##############################

##################################################
## Question 1 ##

def tracer_lsysteme(mot, angle=pi/2, echelle=1):

    t = Turtle3D()
    pile = []

    for c in mot:
        if c == "F" or c == "G":  # forward
            t.forward(1*echelle)

        if c == "f":   # forward without drawing
            t.up()
            t.forward(1*echelle)
            t.down()

        if c == "+":  # left
            t.turn(angle)

        if c == "-":  # right
            t.turn(-angle)

        if c == "&":  # pitch/vers le bas
            t.pitch(-angle)

        if c == "^":  # pitch/vers le haut
            t.pitch(angle)

        if c == "<":  # roll
            t.roll(-angle)

        if c == ">":  # right
            t.roll(angle)

        if c == "|":  # right
            t.turn(pi)           
            
        if c == "[":
            pile.append([t.get_pos(), t.get_u(), t.get_v()])

        if c == "]":
            t.up()
            pos, u, v = pile.pop()
            t.set_pos(pos)
            t.set_u(u)
            t.set_v(v)
            t.down()


        # print("pos =", t.get_pos())
        # print("u = ",t.get_u())
        # print("v = ",t.get_v())
        # print("w = ",t.get_w())
        # print(t.segments)

    t.show()
    return

## Test
# tracer_lsysteme("FF", angle=pi/6, echelle=1)
# tracer_lsysteme("B-F+CFC+F-D&F^D-F+&&CFC+F+B>>")
# tracer_lsysteme("-F+F+F-&F∧-F+&CFC+F+B>>")
# tracer_lsysteme("^<XF^<XFX-F^>>XFX&F+>>XFX-F>X->")
# tracer_lsysteme(r"FfF+FF[+FFF][-FF]F",angle=pi/2,echelle=1)


# Flocon de Koch 2D vu dans l'espace
regles = {"F" : "F+F-F-F+F"}
mot = "F"
mot = iterer_lsysteme(mot, regles, 3)
# tracer_lsysteme(mot)


# Hilbert
n = 3
angle = pi/2
mot = "X"
hilbert = {"X" : "^<XF^<XFX-F^>>XFX&F+>>XFX-F>X->"}
mot = iterer_lsysteme(mot, hilbert, n)
# tracer_lsysteme(mot, echelle=1/7)  # echelle = 1, 1/3, 1/7, 1/14


# variante Hilbert  ('/' = '>')
mot = "A"
hilbert = { 'A': 'B-F+CFC+F-D&F^D-F+&&CFC+F+B>>',
            'B': 'A&F^CFB^F^D^^-F-D^|F^B|FC^F^A>>',
            'C': '|D^|F^B-F+C^F^A&&FA&F^C+F+B^F^D>>',
            'D': '|CFB-F+B|FA&F^A&&FB-F+B|FC>>' }

mot = iterer_lsysteme(mot, hilbert, 2)
# tracer_lsysteme(mot)


# Plante 1
axiom = "^^^^F"
plante1 = {'F' : 'F[&+F]F[->F]F[+^F]F'}
mot = iterer_lsysteme(axiom, plante1, 3)
tracer_lsysteme(mot, angle=pi/8, echelle=0.25)


# Plante 2
#Allen 26: tree with leaves  "`" control the color/size but not use there, "L" is for the leaves
axiom = "^^^^A"
plante2 = {'A': '[&FLA]>>>>>[&FLA]>>>>>>>`[&FLA]', 
                    'F': 'S>>>>>F',
                    'S': 'F',
                    'L': '[Q^^Q][Q<<Q]'}

mot = iterer_lsysteme(axiom, plante2, 6)
# tracer_lsysteme(mot, angle=pi/7)

