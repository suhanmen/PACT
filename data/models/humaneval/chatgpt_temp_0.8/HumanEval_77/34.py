def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    if a == 0:
        return True
    elif a > 0:
        cube_root = int(a**(1/3))
        if cube_root**3 == a:
            return True
        else:
            return False
    else: # a < 0
        cube_root = int((-a)**(1/3))
        if cube_root**3 == -a:
            return True
        else:
            return False
