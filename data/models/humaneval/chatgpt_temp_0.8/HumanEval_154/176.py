# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    # concatenate the first word to itself to check for cyclic patterns
    a += a
    # iterate through all possible rotations of the second word
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
