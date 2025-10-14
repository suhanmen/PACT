import math

def volume_sphere(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)