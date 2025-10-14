def cycpattern_check(a , b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    for i in range(len(b)):  # iterate through all possible rotations of b
        if b[i:] + b[:i] in a:  # check if the rotated b is a substring of a
            return True
    return False
