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
    if a == 0:  # special case for 0
        return True
    if a < 0:  # check if a is negative
        a = abs(a)  # convert negative a to positive
        
    # use the cube root function to check if a is a cube
    return round(a**(1/3))**3 == a
