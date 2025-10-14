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
    
    # Calculate the squares of the three sides
    a_squared = a ** 2
    b_squared = b ** 2
    c_squared = c ** 2
    
    # Check if the sum of the squares of the two shorter sides is equal to the square of the longest side
    if a_squared + b_squared == c_squared or a_squared + c_squared == b_squared or b_squared + c_squared == a_squared:
        return True
    else:
        return False
