"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""


import math

def lateralsurface_cone(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_height
    return lateral_surface_area

# Example usage:
# lateral_surface_area = lateralsurface_cone(5, 12)
# print(lateral_surface_area)
