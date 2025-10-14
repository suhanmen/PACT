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
    # Check if the sum of squares of two shorter sides is equal to the square of the longest side
    sides = [a, b, c]
    hypotenuse = max(sides)
    sides.remove(hypotenuse)
    if hypotenuse**2 == sides[0]**2 + sides[1]**2:
        return True
    else:
        return False
