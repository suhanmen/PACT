"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""


import math

def radian_degree(degree):
    return degree * (math.pi / 180)

# Example usage:
# result = radian_degree(90)
# print(result)
