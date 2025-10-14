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
    # Find the longest side
    max_side = max([a, b, c])
    # Calculate the sum of squares of the other two sides
    sum_squares = 0
    if a != max_side:
        sum_squares += a**2
    if b != max_side:
        sum_squares += b**2
    if c != max_side:
        sum_squares += c**2
    # Check if the sum of squares of the other two sides is equal to the square of the longest side
    if sum_squares == max_side**2:
        return True
    else:
        return False
