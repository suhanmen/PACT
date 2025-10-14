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

    # Handle special cases
    if a == 0:
        return True
    
    # Iterate over possible cube roots until we reach or exceed the absolute value of a
    for i in range(abs(a)):
        if i**3 == abs(a):
            return True
        elif i**3 > abs(a):
            return False
    
    # If we haven't found a cube root yet, it doesn't exist
    return False
