# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    n = len(a)
    m = len(b)
    if m > n:
        return False
    for i in range(n):
        if a[i:i+m] == b:
            return True
    for i in range(n-m):
        if a[i:i+m] == b:
            return True
    return False
