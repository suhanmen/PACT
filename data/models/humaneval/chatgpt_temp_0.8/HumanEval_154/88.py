def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    
    if len(a) < len(b):
        return False
    
    for i in range(len(b)):
        if b in a:
            return True
        b = b[-1] + b[:-1]
    
    return False
