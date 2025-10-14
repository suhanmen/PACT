# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    if len(a) < len(b):
        return False

    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True

    return False
