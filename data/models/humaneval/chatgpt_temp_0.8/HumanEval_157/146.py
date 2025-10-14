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
    # To form a right-angled triangle, the Pythagorean theorem states that 
    # a^2 + b^2 = c^2 where c is the hypotenuse and a and b are the other two sides.
    # Therefore, we first check if c is the hypotenuse.
    if c**2 == a**2 + b**2:
        return True
    # if not, we check if a is the hypotenuse.
    elif a**2 == b**2 + c**2:
        return True
    # if not, we check if b is the hypotenuse.
    elif b**2 == a**2 + c**2:
        return True
    # if none of the above conditions are met, the triangle is not right-angled.
    else:
        return False
