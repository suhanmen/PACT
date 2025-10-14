import math

def volume_cylinder(radius, height):
    volume = math.pi * radius**2 * height
    return volume

assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)