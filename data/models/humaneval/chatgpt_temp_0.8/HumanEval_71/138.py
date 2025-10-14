import math

def triangle_area(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        # Calculate the semi-perimeter of the triangle
        s = (a + b + c) / 2
        # Calculate the area of the triangle using Heron's Formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # Round the area to 2 decimal points and return it
        return round(area, 2)
    else:
        return -1
