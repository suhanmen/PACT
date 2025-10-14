# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    if len(a) < len(b):
        return False

    a *= 2
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True

    return False
