python
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    s = sorted(l)
    if n % 2 == 0:
        # if there is an even number of values, take the average of the middle two
        m1 = s[n//2 - 1]
        m2 = s[n//2]
        return (m1 + m2) / 2
    else:
        # if there is an odd number of values, take the middle one
        return s[n//2]
