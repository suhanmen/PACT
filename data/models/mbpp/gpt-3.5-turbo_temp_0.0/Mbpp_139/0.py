import math

def circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)