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
    a_square = a ** 2
    b_square = b ** 2
    c_square = c ** 2
    
    # Check if the sum of squares of two shorter sides equals the square of the longest side
    if a_square + b_square == c_square or a_square + c_square == b_square or b_square + c_square == a_square:
        return True
    else:
        return False
