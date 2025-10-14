def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""

    # If the length of b is greater than the length of a, return False
    if len(b) > len(a):
        return False

    # Concatenate a with itself to check for all possible rotations of a
    a_concat = a + a

    # If b is a substring in a or any of its rotations, return True
    if b in a or b in a_concat[1:] or b in a_concat[:-1]:
        return True

    return False
