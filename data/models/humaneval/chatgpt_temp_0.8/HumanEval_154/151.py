def cycpattern_check(a , b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    # Check if the length of the 2nd word is greater than the 1st word
    if len(b) > len(a):
        return False

    # Concatenate the first word with itself to handle cyclic patterns
    a = a + a

    # Check if the second word or any of its rotations is a substring in the first word
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            return True

    return False
