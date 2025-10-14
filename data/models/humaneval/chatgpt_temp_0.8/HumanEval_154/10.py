def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""
    if len(a) < len(b):
        return False
    double_a = a + a
    for i in range(len(a)):
        if double_a[i:i+len(b)] == b:
            return True
    return False
