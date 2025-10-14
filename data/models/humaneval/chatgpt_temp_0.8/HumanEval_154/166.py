# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    # If either word is empty, return False
    if not a or not b:
        return False
    
    # If the length of b is greater than a, return False
    if len(b) > len(a):
        return False
    
    # Check if any rotation of b is a substring of a
    for i in range(len(b)):
        if b in a:
            return True
        b = b[1:] + b[0]
    
    return False
