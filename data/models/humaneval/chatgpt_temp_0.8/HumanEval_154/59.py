# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    n = len(a)
    m = len(b)
    if n < m:
        return False
    
    for i in range(n - m + 1):
        if a[i:i+m] == b:
            return True

    for i in range(1, m):
        if b[i:] + b[:i] in a:
            return True

    return False
