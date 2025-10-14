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
    # Find the largest side
    max_side = max(a, b, c)
    
    # Calculate the sum of squares of other two sides
    sum_squares = 0
    if max_side == a:
        sum_squares = b**2 + c**2
    elif max_side == b:
        sum_squares = a**2 + c**2
    else:
        sum_squares = a**2 + b**2
        
    # Check if the sum of squares of other two sides is equal to the square of the largest side
    if max_side**2 == sum_squares:
        return True
    else:
        return False
