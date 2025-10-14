"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""


import math

def otherside_rightangle(a, b):
    # Assuming a and b are the lengths of the two legs of the right angled triangle
    # The third side, which is the hypotenuse, can be found using the Pythagorean theorem
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

# Example usage:
# third_side = otherside_rightangle(7, 8)
# print(third_side)  # Output should be approximately 10.63014581273465
