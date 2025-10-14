def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""

    # Check if length of b is greater than length of a
    if len(b) > len(a):
        return False

    # Concatenate a with itself to check for cyclic patterns
    new_a = a + a

    # Check if b or any of its rotations is a substring in new_a
    for i in range(len(a)):
        if new_a[i:i+len(b)] == b:
            return True
    return False
