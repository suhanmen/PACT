# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    if len(b) > len(a):
        return False

    # Concatenate a with itself to check for circular patterns
    a = a + a

    # Check if b or any of its rotations are in a
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] in (b, b[::-1]):
            return True

    return False
