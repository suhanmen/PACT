def iscube(a):
    # Get the cube root of the absolute value of a
    cube_root = abs(a) ** (1/3)
    # Check if the cube root is an integer
    return int(cube_root + 0.5) ** 3 == abs(a)
