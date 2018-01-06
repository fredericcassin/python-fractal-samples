from turtle import *
from math import *

def dragon(generation, longueur, spin):
    if generation <= 0:
        fd(longueur)
        return
    lt(spin * 45)
    dragon(generation - 1, longueur / sqrt(2), 1)
    rt(spin * 90)
    dragon(generation - 1, longueur / sqrt(2), -1)
    lt(spin * 45)

reset()
speed(0)
tracer(0, 0)
ht()
penup()
generation = 16
L = 500
goto(-L / 2, 0)
width(1)
pendown()
dragon(generation, L, 1)
update()
Screen().mainloop()