def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    n = len(a)
    m = len(b)
    
    if m > n:
        return False
    
    b *= 2
    for i in range(n):
        if b[i:i+m] in a:
            return True
    
    return False
