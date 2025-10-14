# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    for i in range(len(b)):
        if a.find(b[i:] + b[:i]) != -1:
            return True
    return False
