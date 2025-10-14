def iscube(a):
    # Check if a is negative and adjust the sign of a accordingly
    if a < 0:
        a = -a
    
    # Find the cube root of a, round it to the nearest integer, and cube it
    cube_root = round(a**(1/3))
    cube = cube_root**3
    
    # Return True if the cube is equal to a, False otherwise
    return cube == a
