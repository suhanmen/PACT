def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    
    n = len(a)
    m = len(b)
    
    if n < m:
        return False
    
    b += b
    
    for i in range(n):
        if b == a[i:i+m]:
            return True
    
    return False
