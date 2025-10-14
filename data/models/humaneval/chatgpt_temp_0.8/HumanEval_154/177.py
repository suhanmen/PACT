def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    
    # Check for base case
    if len(b) > len(a):
        return False
    
    # Concatenate a with itself to handle all possible rotations
    a = a + a
    
    # Check if b or any of its rotations is a substring of a
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            return True
    
    return False
