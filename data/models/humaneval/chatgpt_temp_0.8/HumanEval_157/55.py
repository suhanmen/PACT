def right_angle_triangle(a, b, c):
    # Find the longest side of the triangle
    longest_side = max(a, b, c)
    
    # Check if the Pythagorean theorem holds true for the triangle
    if longest_side**2 == (a**2 + b**2 + c**2 - longest_side**2):
        return True
    else:
        return False
