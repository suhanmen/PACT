def cycpattern_check(a , b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    
    if len(a) < len(b):
        return False
    
    # Double the first word to make it easier to check for all rotations of the second word
    a = a+a
    
    # Check if any rotation of the second word is a substring of the first word
    for i in range(len(b)):
        if b[i:]+b[:i] in a:
            return True
    
    return False
