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
        a = -a
    if a in [0, 1]:
        return True
    low, high = 0, a
    while low <= high:
        mid = (low + high) // 2
        if mid ** 3 == a:
            return True
        elif mid ** 3 < a:
            low = mid + 1
        else:
            high = mid - 1
    return False
