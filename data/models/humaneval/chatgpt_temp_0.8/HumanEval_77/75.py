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
    # Taking the absolute value of a so that negative numbers can be checked as well
    a = abs(a)
    
    # Taking the cube root of a and checking if it is an integer
    if int(a**(1/3))**3 == a:
        return True
    else:
        return False
