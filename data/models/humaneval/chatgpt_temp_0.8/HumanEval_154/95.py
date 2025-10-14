def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    n = len(a)
    m = len(b)
    if m > n:
        return False
    for i in range(n):
        if a[i:i+m] == b:
            return True
    for i in range(n-m):
        if sorted(a[i:i+m]) == sorted(b):
            return True
    return False
