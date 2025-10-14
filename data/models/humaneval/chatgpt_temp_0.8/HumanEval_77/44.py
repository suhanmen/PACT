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
    elif a < 0:
        a = -a

    # Using the cube root function to check if the cube of a number is equal to a.
    if round(a**(1/3))**3 == a:
        return True
    else:
        return False
