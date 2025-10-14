# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    """
    n = len(a)
    m = len(b)
    
    if m > n:
        return False
    
    for i in range(n):
        if a[i:i+m] == b or a[i:i+m] == b[::-1]:
            return True
        
    return False
