import math

def surfacearea_sphere(radius):
    return 4 * math.pi * radius**2

assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)