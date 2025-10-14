# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    for i in range(len(b)):
        if b in a:
            return True
        b = b[1:] + b[0] # rotate b
    return False
    
print(cycpattern_check("abcd","abd")) # False
print(cycpattern_check("hello","ell")) # True
print(cycpattern_check("whassup","psus")) # False
print(cycpattern_check("abab","baa")) # True
print(cycpattern_check("efef","eeff")) # False
print(cycpattern_check("himenss","simen")) # True
