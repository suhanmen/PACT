def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    if a == 0: # special case for zero
        return True
    else:
        root = round(a ** (1/3)) # find the cube root and round to the nearest integer
        return root ** 3 == a # check if the cube of the root is equal to the input
