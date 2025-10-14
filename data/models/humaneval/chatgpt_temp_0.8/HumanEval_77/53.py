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
    x = abs(a) # Take absolute value to handle negative numbers
    c = int(x ** (1/3)) # Take the cube root and convert to integer
    return c**3 == x # Check if c cubed equals x
