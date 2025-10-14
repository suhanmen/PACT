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
    if a == 0 or a == 1: # 0 and 1 are already cubes
        return True
    
    # Check for other positive integers
    for i in range(abs(a)):
        if i**3 == abs(a):
            return True
    
    # Check for negative integers
    for i in range(abs(a)):
        if ((-i)**3) == abs(a):
            return True
    
    # If no cube found, return False
    return False
