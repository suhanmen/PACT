import math

def lateral_surface_cylinder(radius, height):
    return 2 * math.pi * radius * height

assert math.isclose(lateral_surface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)