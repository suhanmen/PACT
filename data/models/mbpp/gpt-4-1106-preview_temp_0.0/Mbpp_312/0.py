"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""


import math

def volume_cone(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

# Example usage:
# volume = volume_cone(5, 12)
# print(volume)
