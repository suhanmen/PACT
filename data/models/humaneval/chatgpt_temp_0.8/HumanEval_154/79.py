def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    If b is a rotation of a, then concatenating a with itself will contain b.
    """
    if b in a+a:
        return True
    else:
        return False
