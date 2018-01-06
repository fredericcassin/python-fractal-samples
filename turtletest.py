from turtle import *
from math import *

def segment_fractal(niveau, nombre, longueur, spin, ratio):
    if niveau <= 0:
        fd(longueur)
        return
    l = (longueur / nombre) * ratio
    s = (longueur - l) / 2
    n = niveau - 1
    segment_fractal(n, nombre, s, spin, ratio)
    lt(spin * (180 - 360 / nombre))
    for i in range(nombre - 1):
        segment_fractal(n, nombre, l, spin, ratio)
        rt(spin * (360 / nombre))
    lt(180)
    segment_fractal(n, nombre, s, spin, ratio)

def poly_fractal(niveau, nombre, longueur, spin, ratio):
    for cote in range(nombre):
        segment_fractal(niveau, nombre, longueur, spin, ratio)
        lt(360 / nombre)

reset()
speed(0)
tracer(0, 0)
ht()
penup()
spin = 1; nombre = 4; ratio = 1
L = 500 / nombre * ratio / (sqrt(sqrt(ratio)))
if ratio >= 1:
    L = L / ratio
goto(-L / 2, -spin * L / 2)
width(1)
pendown()
poly_fractal(2, nombre, L, spin, ratio)
update()
Screen().mainloop()