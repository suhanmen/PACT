def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    
    # Check if b is a substring of a
    if b in a:
        return True
    
    # Check if any rotation of b is a substring of a
    for i in range(1, len(b)):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    
    # If no substring or rotation is found, return False
    return False
