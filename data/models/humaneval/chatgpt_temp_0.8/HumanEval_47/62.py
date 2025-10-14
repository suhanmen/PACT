def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    s = sorted(l)
    if n % 2 == 0:
        # if the list has an even number of elements, the median is the average
        # of the two middle elements
        return (s[n // 2 - 1] + s[n // 2]) / 2
    else:
        # if the list has an odd number of elements, the median is the middle element
        return s[n // 2]
