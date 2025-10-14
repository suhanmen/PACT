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
    # find the largest side
    hypotenuse = max(a,b,c)
    # find the sum of squares of the other two sides
    sum_of_squares = 0
    if a != hypotenuse:
        sum_of_squares += a**2
    if b != hypotenuse:
        sum_of_squares += b**2
    if c != hypotenuse:
        sum_of_squares += c**2
    # check if it is a right-angled triangle
    if hypotenuse**2 == sum_of_squares:
        return True
    else:
        return False
