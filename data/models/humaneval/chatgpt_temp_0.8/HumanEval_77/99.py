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
    if a < 0:  # handle negative input
        a = -a
    if a == 0:  # handle zero input
        return True
    for i in range(1, a):
        if i**3 == a:
            return True
        elif i**3 > a:
            return False
    return False
