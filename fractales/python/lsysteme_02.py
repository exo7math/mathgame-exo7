
##############################
# L-système
##############################

from turtle import *


##############################
# Activité 1 - Tracer un L-système
##############################


def trace_lsysteme(mot,angle=90,echelle=1):

    speed("fastest")
    width(2)
    color('blue')
    up()
    goto(-150,-150)
    down()

    for c in mot:
        if c == "F" or c == "G":
            forward(100*echelle)
        if c == "+":
            left(angle)
        if c == "-":
            right(angle) 

    exitonclick()

    return

## Test ##
# trace_lsysteme("F+F-FF-F-F")


##############################
# Activité 2 - Une seule règle : le flocon re Koch
##############################

# Un L-système
# un mot de départ
# des règles de remplacement

##################################################
## Question 1 ##

def remplacer_1(mot,lettre,motif):
    nouv_mot = ""
    for l in mot:
        if l == lettre:
            nouv_mot = nouv_mot + motif
        else:
            nouv_mot = nouv_mot + l

    return nouv_mot

## Test ##
# print("--- Remplacer une lettre ---")
# mot = "F-FF+"
# nouv_mot = remplacer_1(mot,"F","F+")
# print(mot)
# print(nouv_mot)


##################################################
## Question 2 ##

def iterer_lsysteme_1(depart,regle,k):
    mot = depart
    lettre = regle[0]
    motif = regle[1]

    for i in range(k):
        mot = remplacer_1(mot,lettre,motif)

    return mot

##################################################
## Question 3 ##

## Flocon re Koch
depart_Koch = "F"
regle_Koch = ("F","F+F-F-F+F")

## Test
# for k in range(4):
#     print(k,iterer_lsysteme_1(depart_Koch,regle_Koch,k))
#     print()

# k = 3
# mot = iterer_lsysteme_1(depart_Koch,regle_Koch,k)
# trace_lsysteme(mot,echelle=5/3**k)


##################################################
## Question 4 ##

#####################
## Futres exemples ##

#####################
depart = "F-F-F-F"
regle = ("F","F-F+F+FF-F-F+F")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.05)

#####################
depart = "F-F-F-F"
regle = ("F","F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F")
k = 2
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.07)

#####################
depart = "F-F-F-F"
regle = ("F","FF-F-F-F-FF")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.1)

#####################
depart = "F-F-F-F"
regle = ("F","FF-F--F-F")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.1)

#####################
depart = "F-F-F-F"
regle = ("F","FF-F-F-F-F-F+F")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.1)

#####################
depart = "F-F-F-F"
regle = ("F","FF-F+F-F-FF")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.15)

#####################
depart = "F-F-F-F"
regle = ("F","F-FF--F-F")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.15)

#####################
depart = "F-F-F-F"
regle = ("F","F-F+F-F-F")
k = 4
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.15)



##############################
# Activité 3 - Deux règles : Triangle de Sierpinski
##############################

##################################################
## Question 1 ##

def remplacer_2(mot,lettre1,motif1,lettre2,motif2):
    nouv_mot = ""
    for l in mot:
        if l == lettre1:
            nouv_mot = nouv_mot + motif1
        elif l == lettre2:
            nouv_mot = nouv_mot + motif2
        else:
            nouv_mot = nouv_mot + l

    return nouv_mot

## Test ##
# print("--- Remplacer deux lettres ---")
# mot = "F-G+F"
# nouv_mot = remplacer_2(mot,"F","FG+","G","G-")
# print(mot)
# print(nouv_mot)

# mot1 = remplacer_1(mot,"F","FG+")
# mot2 = remplacer_1(mot1,"G","G-")
# print(mot2)

##################################################
## Question 2 ##

def iterer_lsysteme_2(depart,regle1,regle2,k):
    mot = depart
    lettre1 = regle1[0]
    motif1 = regle1[1]
    lettre2 = regle2[0]
    motif2 = regle2[1]

    for i in range(k):
        mot = remplacer_2(mot,lettre1,motif1,lettre2,motif2)

    return mot


##################################################
## Question 3 ##

## Triangle de Sierpinski
depart_Sierp = "F-G-G"
regle_Sierp_1 = ("F","F-G+F+G-F")
regle_Sierp_2 = ("G","GG")

## Test
# print("--- Sierpinski ---")
# for k in range(3):
#     print(iterer_lsysteme_2(depart_Sierp,regle_Sierp_1,regle_Sierp_2,k))
#     print()

# k = 4
# mot = iterer_lsysteme_2(depart_Sierp,regle_Sierp_1,regle_Sierp_2,k)
# trace_lsysteme(mot,angle=-120,echelle=5/2**k)

##################################################
## Question 4 ##

#####################
## Autres exemples ##

#####################
## Courbe du dragon
depart_dragon = "FX"
regle_dragon_1 = ("X","X+YF+")
regle_dragon_2 = ("Y","-FX-Y")

k = 8
mot = iterer_lsysteme_2(depart_dragon,regle_dragon_1,regle_dragon_2,k)
# print(mot)
# trace_lsysteme(mot,echelle=2/k)

#####################
## Variante Sierpinski (angle = 60)
depart = "F"
regle1 = ("F","G-F-G")
regle2 = ("G","F+G+F")
angle = 60

k = 4
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme(mot,angle=60,echelle=2/k**2)


#####################
## Courbe de Gosper
depart = "F"
regle1 = ("F","F+G++G-F--FF-G+")
regle2 = ("G","-F+GG++G+F--F-G")

k = 3
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme(mot,angle=60,echelle=2/k**2)


##############################
# Activité 4 - Tracer un L-système avec pile
##############################


##################################################
## Question 1 ##

def trace_lsysteme_pile(mot,angle=90,echelle=1):
    tracer(n=0, delay=0)
    # speed("fastest")
    width(2)
    color('blue')
    up()
    goto(0,-300)
    down()

    pile = []

    for c in mot:
        if c == "F" or c == "G":
            forward(100*echelle)
        if c == "f":
            up()
            forward(100*echelle)
            down()
        if c == "+":
            left(angle)
        if c == "-":
            right(angle)
        if c == "[":
            pile = pile + [(position(),heading())]
        if c == "]":
            up()
            pos, direc = pile.pop()
            goto(pos)
            setheading(direc)
            down()

    hideturtle()
    update()
    exitonclick()

    return

## Test
# trace_lsysteme_pile("FfF+FF[+FFF][-FF]F",angle=90,echelle=1)
# trace_lsysteme_pile("F+F[+FFF]F[-FF]F",angle=90,echelle=1)

##################################################
## Question 2 ##

# Plante
depart_plante = "+++X"
regle_plante_1 = ("X","F[+X][X]F[+X]-FX")
regle_plante_2 = ("F","FF")


k = 5
mot = iterer_lsysteme_2(depart_plante,regle_plante_1,regle_plante_2,k)
# trace_lsysteme_pile(mot,angle=30,echelle=1/k**(3/2))



#####################
## Exemples avec up-down ##
depart = "F-F-F-F"
regle1 = ("F","F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF")
regle2 = ("f","ffffff")
k = 2
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,echelle=0.1)



#####################
## Autres exemples de plantes ##


# #####################
# Plante 1
depart = "+++F"
regle = ("F","F[+F]F[-F][F]")
k = 4
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.2)


# #####################
# Plante 2
depart = "+++F"
regle = ("F","F[+F]F[-F]F")
k = 4
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.075)

# ####################
# Plante 3
depart = "+++F"
regle = ("F","FF-[-F+F+F]+[+F-F-F]")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.2)


# #####################
# angle = 25.7
depart = "+++X"
regle1 = ("X","F[+X]F[-X]FX")
regle2 = ("F","FF")
k = 5
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.07)


# #####################
# Plante 4
depart = "++++F"
regle1 = ("F","F[-G][+G]")
regle2 = ("G","F[-G]F[+F-G]")
k = 6
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,angle=22.5,echelle=0.25)



#####################
# angle = 30
depart = "X"
regle1 = ("X","F-[[X]+X]+F[+FX]-X")
regle2 = ("F","FF")
k = 4
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.15)


#####################
# Plante 5
depart = "+++YYY"
regle1 = ("X","X[-FFF][+FFF]FX")
regle2 = ("Y","YFX[+Y][-Y]")
k = 5
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.05)



#####################
# Plante 6
depart = "++++X"
regle1 = ("X","F[+X]F[-X]+X")
regle2 = ("F","FF")
k = 7
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
trace_lsysteme_pile(mot,angle=22.5,echelle=0.025)



#####################
#####################
# Courbe de Hilbert
# Pour les illustrations du livre
  # \rule{L -> +RF-LFL-FR+}
  # \rule{R -> -LF+RFR+FL-}}
# angle = 30
depart = "X"
regle1 = ("X","+YF-XFX-FY+")
regle2 = ("Y","-XF+YFY+FX-")
k = 4
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,angle=90,echelle=0.15)