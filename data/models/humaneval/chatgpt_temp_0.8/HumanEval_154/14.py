# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    """
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        return False
    for i in range(len_a):
        if a[i] == b[0]:
            if a[i:i+len_b] == b:
                return True
            if a[i:] + a[:i] == b:
                return True
    return False
