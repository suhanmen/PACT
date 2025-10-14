"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""


import math

def area_tetrahedron(edge_length):
    """
    Calculate the area of a regular tetrahedron with the given edge length.

    :param edge_length: The length of an edge of the tetrahedron
    :return: The surface area of the tetrahedron
    """
    # Calculate the area of one equilateral triangle face
    triangle_area = math.sqrt(3) / 4 * edge_length ** 2
    
    # A tetrahedron has 4 equilateral triangle faces
    total_area = 4 * triangle_area
    
    return total_area

# Example usage:
# edge_length = 3
# print(area_tetrahedron(edge_length))
