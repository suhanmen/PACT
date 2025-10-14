# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    # Concatenate string a with itself to check for all possible rotations
    a = a + a
    # Check if string b is a substring of a
    if b in a:
        return True
    else:
        return False
