def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    
    if len(a) < len(b):
        return False
    
    # Concatenate a with itself to cover cyclic patterns
    a = a + a
    
    for i in range(len(a)-len(b)+1):
        # Check if b is a substring of a or any of its rotations
        if b in a[i:i+len(b)]:
            return True
    
    return False
