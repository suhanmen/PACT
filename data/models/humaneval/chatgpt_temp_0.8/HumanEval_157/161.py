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
    # Check if the given sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    # Check if one angle is 90 degree
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return True
    else:
        return False
