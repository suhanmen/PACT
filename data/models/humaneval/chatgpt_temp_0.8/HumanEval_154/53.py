# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its 
    rotations is a substring in the first word.

    Examples:
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """

    # concatenate the first word with itself to check for cyclic patterns
    a = a + a

    # check if any rotation of the second word is a substring in the first word
    for i in range(len(b)):
        if a.find(b[i:]) != -1 or a.find(b[:i]) != -1:
            return True

    return False
