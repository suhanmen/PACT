"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""


import math

def surface_Area(base_edge, height):
    # Calculate the slant height of the pyramid
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    # Calculate the base area
    base_area = base_edge ** 2
    # Calculate the lateral surface area (4 times the area of one triangle)
    lateral_area = 4 * (base_edge * slant_height) / 2
    # Calculate the total surface area
    total_surface_area = base_area + lateral_area
    return round(total_surface_area)

# Example usage
# surface_Area(3, 4) should return 33
