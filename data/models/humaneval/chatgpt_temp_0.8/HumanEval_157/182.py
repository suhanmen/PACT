def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Check if any of the sides are 0 or negative
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Check if the sum of any two sides is less than or equal to the third side
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    
    # Check if the triangle is a right-angled triangle
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
