def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    cube_root = abs(a) ** (1/3) # Get the cube root of the absolute value of the input
    return int(cube_root) ** 3 == abs(a) # Check if the cube of the integer value of the cube root equals the absolute value of the input
