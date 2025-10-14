def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def is_rotation(s1, s2):
        return len(s1) == len(s2) and s2 in s1+s1

    for i in range(len(b)):
        if is_rotation(a, b[i:] + b[:i]):
            return True
    return False
