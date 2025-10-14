def median(l: list):
    """
    Return median of elements in the list l.
    """
    n = len(l)
    s = sorted(l)
    if n % 2 == 0:
        return (s[n//2-1] + s[n//2])/2
    else:
        return s[n//2]
