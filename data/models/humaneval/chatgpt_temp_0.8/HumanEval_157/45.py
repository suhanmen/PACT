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
    # Check if any of the sides is zero or negative
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Check if the triangle satisfies the Pythagorean theorem
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return True
    
    # If none of the above conditions are met, the triangle is not a right-angled triangle
    return False
