from turtle import *
from random import uniform
from math import *

#===================
#  globals parameters
#===================

# Returns v with a random variation, in percentage between min % and max
# Example : get_divergent_value(10, -20, 20) means return a random value 10 +/- 20%
def get_divergent_value(v, percentage_min, percentage_max):
    return v * (1 + uniform(percentage_min, percentage_max) / 100)

# Draws a fractal tree
# forking_angle: average angle in degrees where branches are distributed on each generation
def fractal_tree(generation, branch_length, branch_count, thickness, growth_factor=1.0, forking_angle=100, level=1):
    x, y = pos()
    h = heading()
    e = pensize()
    pc = pencolor()
    percentage_min = (-60 + level * 10) * growth_factor
    percentage_max = level * 20 * growth_factor
    if generation <= 0:
        # Draws tree leaves
        pensize(thickness * 10)
        pencolor("green")
        fd(get_divergent_value(branch_length, percentage_min, percentage_max))
    else:
        # Draws the trunc
        pencolor("#722904")
        thickness_at_end = get_divergent_value(thickness / 2.7, -20 * growth_factor, +20 * growth_factor)
        real_branch_length = get_divergent_value(branch_length, percentage_min, percentage_max)
        if thickness_at_end > thickness: thickness_at_end = max(thickness, 1)
        steps = round(thickness - thickness_at_end) + 1
        step_branch_length = real_branch_length / steps
        pensize(thickness)
        for step in range(steps):
            fd(step_branch_length)
            if thickness > 1: thickness -= 1
            pensize(thickness)
        # Draws branches
        leaf_branching_multiplicator = 2 if generation <= 2 else 1
        forkBranchCount = min(5, max(round(get_divergent_value(branch_count, -80, +200 + level * 50)), 1)) * leaf_branching_multiplicator
        angle = 0 if forkBranchCount == 1 else forking_angle / (forkBranchCount - 1)
        if angle > 0: lt(get_divergent_value(forking_angle / 2, -20, 20))
        for i in range(forkBranchCount):
            fractal_tree(generation - 1, branch_length / 2.1, branch_count, thickness_at_end, growth_factor, forking_angle, level + 1)
            rt(get_divergent_value(angle, -20, +20))
    goto(x, y)
    setheading(h)
    pensize(e)
    pencolor(pc)

# Main program calling the fractal_tree with given parameters
# set up the turtle for the tree draw
reset()
speed(0)
tracer(0, 0) # no screen update, delay = 0 (faster drawing config)
ht()   # hide turtle
penup()
goto(0, -300)
width(1)
pendown()
lt(90)
# Fractal tree draw
fractal_tree(generation=6, branch_length=280, branch_count=3, thickness=50)
# Fractal tree draw
update()
Screen().mainloop()
