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
    if a < 0:
        a = abs(a) # convert negative number to positive for checking
    root = round(a**(1/3)) # calculate cube root and round to nearest integer
    if root**3 == a: # check if cube of root is equal to a
        return True
    else:
        return False
