def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    if len(a) < len(b):
        return False
    if b in a:
        return True
    for i in range(1, len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
    
