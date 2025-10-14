def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""
    
    # Concatenate 1st word with itself to check for cyclic pattern
    a = a + a
    
    # Check if second word or any of its rotations is a substring in the first word
    if b in a:
        return True
    for i in range(1, len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
