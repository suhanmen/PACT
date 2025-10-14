def right_angle_triangle(a, b, c):
    # Calculate the squares of the sides
    squares = [a**2, b**2, c**2]
    
    # Find the largest side
    max_side = max(squares)
    
    # Check if the Pythagorean theorem holds
    if max_side == squares[0] + squares[1] or \
       max_side == squares[1] + squares[2] or \
       max_side == squares[2] + squares[0]:
        return True
    else:
        return False
