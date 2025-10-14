# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    for i in range(len(b)):
        if a.find(b) != -1:
            return True
        b = b[1:] + b[0]  # rotate b
    return False
