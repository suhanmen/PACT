"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""


import math

def angle_complex(complex_number):
    return math.atan2(complex_number.imag, complex_number.real)

# Example usage:
# angle = angle_complex(0 + 1j)
# print(angle)
