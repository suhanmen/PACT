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
    # Take the cube root of the absolute value of the input
    root = abs(a) ** (1/3)
    
    # Check if the cube root is an integer (i.e., the input is a cube)
    return int(root + 0.5) ** 3 == abs(a)
