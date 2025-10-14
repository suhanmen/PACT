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
    cube_root = abs(a) ** (1/3) # get the cube root of the absolute value of a
    return round(cube_root) ** 3 == abs(a) # check if the cube of the rounded cube root is equal to the absolute value of a
