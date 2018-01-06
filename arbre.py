from turtle import *
from random import uniform
from math import *


# Alea
def alea(v, pMin, pMax):
    return v * (1 + uniform(pMin, pMax) / 100)


def arbre(generation, longueur, branches, epaisseur, croissance=1.0, niveau=1):
    x, y = pos()
    h = heading()
    e = pensize()
    pc = pencolor()
    aleaMin = (-60 + niveau * 10) * croissance
    aleaMax = niveau * 20 * croissance
    branchesLocales = max(round(uniform(branches - 2, branches + 2 + niveau * 2)), 2)
    if epaisseur >= 1:
        pensize(alea(epaisseur, -20 * croissance, 20 * croissance))
    if generation <= 0:
        pencolor("green")
        fd(alea(longueur, aleaMin, aleaMax))
    else:
        # trunc
        pencolor("#722904")
        fd(alea(longueur, aleaMin, aleaMax))
        angle = 100 / (branchesLocales - 1)
        # branches
        lt(alea(50, -20, 20))
        for i in range(branchesLocales):
            arbre(generation - 1, longueur / 2.1, branches, epaisseur / 2.7, croissance, niveau + 1)
            rt(alea(angle, -20, +20))
    goto(x, y)
    setheading(h)
    pensize(e)
    pencolor(pc)


reset()
speed(0)
tracer(0, 0)
ht()
penup()
generation = 0
L = 280
branches = 3
epaisseur = 50
goto(0, -300)
width(1)
pendown()
lt(90)
arbre(6, L, branches, epaisseur, 1.0)
update()
Screen().mainloop()
