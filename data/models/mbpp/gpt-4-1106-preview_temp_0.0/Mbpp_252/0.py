"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""


import cmath

def convert(complex_number):
    return cmath.polar(complex_number)

# Example usage:
# complex_num = 1 + 1j
# polar_coordinates = convert(complex_num)
# print(polar_coordinates)  # Output will be in the form (magnitude, phase)

assert convert(1) == (1.0, 0.0)
