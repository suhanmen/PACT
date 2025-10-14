"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""


import math

def surfacearea_cylinder(radius, height):
    base_area = math.pi * (radius ** 2)
    side_area = 2 * math.pi * radius * height
    surface_area = (2 * base_area) + side_area
    return round(surface_area, 2)

# Example usage:
# surface_area = surfacearea_cylinder(10, 5)
# print(surface_area)
