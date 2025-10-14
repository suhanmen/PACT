"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""


import math

def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        area = (angle / 360) * math.pi * radius ** 2
        return area

# Example usage:
# area = sector_area(4, 45)
# print(area)
