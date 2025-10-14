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
    if a == 0: # handle special case of 0
        return True
    
    if a < 0:
        a = -a # handle negative numbers by converting to positive
    
    # iterate through all numbers from 1 to the square root of a
    # and check if any of them cubed is equal to a
    for i in range(1, int(a**(1/3))+1):
        if i**3 == a:
            return True
    
    return False # if no perfect cube is found, return False
