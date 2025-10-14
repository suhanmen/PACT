def right_angle_triangle(a, b, c):
    # Check if any of the sides are zero or negative
    if (a <= 0) or (b <= 0) or (c <= 0):
        return False
    
    # Sort the sides by length
    sides = sorted([a, b, c])
    
    # Check if the sum of the squares of the two shorter sides is equal
    # to the square of the longest side
    if (sides[0]**2 + sides[1]**2 == sides[2]**2):
        return True
    else:
        return False
