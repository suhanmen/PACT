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

    Parameters:
    a (str): the first word
    b (str): the second word

    Returns:
    bool: True if the second word or any of its rotations is a substring in the first word, False otherwise.
    """
    if len(a) < len(b):
        return False
    if b in a:
        return True
    for i in range(1, len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
