"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""


import math

def find_Volume(base, height, length):
    # Calculate the area of the triangle base
    triangle_area = 0.5 * base * height
    
    # Calculate the volume of the prism
    volume = triangle_area * length
    return volume

# Example usage:
# volume = find_Volume(10, 8, 6)
# print('The volume of the triangular prism is:', volume)
