def median(l: list):
    """Return the median of elements in the list l."""
    n = len(l)
    s = sorted(l)
    m = n // 2
    if n % 2 == 0:
        return (s[m - 1] + s[m]) / 2
    else:
        return s[m]
