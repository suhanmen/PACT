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
    # Check if the cube root of a is an integer
    if a >= 0:
        root = int(a ** (1/3))
        return root ** 3 == a
    else:
        root = int((-a) ** (1/3))
        return root ** 3 == -a
