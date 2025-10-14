def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
