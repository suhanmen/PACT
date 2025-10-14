# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""
    if len(a) < len(b):
        return False
    return b in (a + a)[1:-1]
