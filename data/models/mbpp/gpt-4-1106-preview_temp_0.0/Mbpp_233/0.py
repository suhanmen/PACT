"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""


import math

def lateralsurface_cylinder(radius, height):
    """
    Calculate the lateral surface area of a cylinder.
    :param radius: The radius of the cylinder
    :param height: The height of the cylinder
    :return: The lateral surface area of the cylinder
    """
    return 2 * math.pi * radius * height

# Example usage:
# assert math.isclose(lateralsurface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
