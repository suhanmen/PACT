import math

def volume_cone(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)