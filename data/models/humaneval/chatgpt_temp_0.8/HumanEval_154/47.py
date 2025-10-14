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
    if len(a) < len(b):  # If b is longer than a, return False
        return False
    for i in range(len(b)):  # Loop through each character in b
        if a.find(b) != -1:  # If b is a substring of a, return True
            return True
        b = b[1:] + b[0]  # Rotate b
    return False  # If no rotation of b is a substring of a, return False
