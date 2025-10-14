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
    # check if a, b, and c form a valid triangle
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    
    # find the largest side and its index
    sides = [a, b, c]
    largest_index = sides.index(max(sides))
    
    # check if the Pythagorean theorem holds true for the largest side
    if sides[largest_index]**2 == sides[(largest_index + 1) % 3]**2 + sides[(largest_index + 2) % 3]**2:
        return True
    else:
        return False
