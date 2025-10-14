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
    if a == 0:  # 0 is a cube of 0, so return True
        return True
    else:
        cuberoot = round(a ** (1/3))  # calculate the cube root of a and round to nearest integer
        return cuberoot ** 3 == a  # check if cuberoot cubed is equal to a
