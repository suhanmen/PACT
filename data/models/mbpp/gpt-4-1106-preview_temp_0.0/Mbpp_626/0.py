"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""


import math

def triangle_area(radius):
    if radius <= 0:
        return None
    # The largest triangle inscribed in a semicircle is a right-angled triangle
    # with the diameter as its base and the radius as its height.
    # Area of a triangle = 0.5 * base * height
    # Diameter of the semicircle = 2 * radius
    # Therefore, the area of the triangle = 0.5 * (2 * radius) * radius
    return 0.5 * 2 * radius * radius

# Example usage:
# print(triangle_area(5))  # Should output 25.0

# Test case
assert triangle_area(-1) == None
