def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    
    # create a variable to store the length of the first word
    n = len(a)
    
    # check if the length of the second word is greater than the first word
    if len(b) > n:
        return False
    
    # check if the second word or any of its rotations is a substring of the first word
    for i in range(n):
        if a[i:] + a[:i] == b:
            return True
    
    return False
