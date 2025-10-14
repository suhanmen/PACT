def right_angle_triangle(a, b, c):
    # Check if the sum of squares of the two shorter sides is equal to the square of the longest side
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False
