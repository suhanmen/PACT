# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    n = len(a)
    m = len(b)
    if m > n:
        return False
    for i in range(n):
        if a[i:i + m] == b:
            return True
    for i in range(m, n):
        if a[i:i + m] + a[:i - m] == b:
            return True
    return False
