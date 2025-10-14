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
    
    if len(a) < len(b):  # if the length of a is less than b, then b cannot be a substring of a or its rotations
        return False
    
    for i in range(len(b)):
        if b in a:  # if b is a substring of a, return True
            return True
        b = b[-1] + b[:-1]  # rotate b by one character
    
    return False  # if no rotation of b is a substring of a, return False
