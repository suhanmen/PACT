def iscube(a):
    cube_root = abs(a) ** (1/3) # find the cube root of the absolute value of a
    return int(cube_root) ** 3 == abs(a) # check if the cube of the integer value of cube_root equals a
