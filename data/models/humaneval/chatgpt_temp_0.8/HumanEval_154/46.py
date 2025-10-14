# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
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
    if len(a) < len(b):
        return False
    
    # Concatenate a with itself to check for cyclic patterns
    a_concat = a + a
    
    # Check if b or any of its rotations is a substring of a_concat
    for i in range(len(b)):
        if b[i:] + b[:i] in a_concat:
            return True
    
    return False
