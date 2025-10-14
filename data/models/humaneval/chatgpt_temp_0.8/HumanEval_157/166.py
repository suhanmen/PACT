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
    # Find the longest side of the triangle
    longest_side = max([a, b, c])
    
    # Check if the three sides form a right-angled triangle
    if a*a + b*b + c*c - longest_side*longest_side == longest_side*longest_side:
        return True
    else:
        return False
