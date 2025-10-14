import math

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    if a+b>c and a+c>b and b+c>a:  # checking if the three sides form a valid triangle
        s = (a+b+c)/2  # calculating the semi-perimeter
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))  # using Heron's formula to calculate the area of the triangle
        return round(area,2)  # rounding off the area to 2 decimal places
    else:
        return -1  # return -1 if the three sides do not form a valid triangle
