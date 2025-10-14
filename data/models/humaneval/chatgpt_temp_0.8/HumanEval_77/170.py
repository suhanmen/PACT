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
    if a == 0:  # 0 is a special case, since 0^3 = 0
        return True
    i = 1
    while i ** 3 <= abs(a):
        if i ** 3 == abs(a):
            return True
        i += 1
    return False
