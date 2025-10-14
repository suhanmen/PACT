# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""
    b_len = len(b)
    for i in range(len(a)):
        if a[i:i+b_len] == b:
            return True
    for i in range(1, b_len):
        if b[i:] + b[:i] in a:
            return True
    return False
