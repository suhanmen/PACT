def iscube(a):
    # Take the absolute value of the input, since the cube of a negative number is still a cube
    a = abs(a)
    
    # Find the cube root of the input and round it to the nearest integer
    cube_root = round(a**(1/3))
    
    # Check if the cube of the integer cube root is equal to the input
    return cube_root**3 == a
