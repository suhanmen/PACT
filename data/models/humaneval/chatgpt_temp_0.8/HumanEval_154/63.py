# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    for i in range(len(b)):
        # Rotate the word to the right by i positions
        rotated = b[i:] + b[:i]
        # Check if the rotated word is a substring of a
        if rotated in a:
            return True
    # None of the rotations were found in a
    return False
