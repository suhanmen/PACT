def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    
    # check if b is a substring of a
    if b in a:
        return True
    
    # check if any of the rotations of b is a substring of a
    for i in range(1, len(b)):
        if b[i:] + b[:i] in a:
            return True
    
    # if no substring found, return False
    return False
