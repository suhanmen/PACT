def cycpattern_check(a , b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.

    Examples:
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """

    # Check if the length of b is greater than a
    if len(b) > len(a):
        return False

    # Concatenate a with itself to handle circular patterns
    a += a

    # Check if b is a substring of any rotation of a
    for i in range(len(a) - len(b) + 1):
        if b in a[i:i+len(b)]:
            return True
    
    return False
