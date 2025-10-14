def median(l: list):
    """Return median of elements in the list l.
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    if n % 2 == 0:
        # if even length, take the average of the middle two elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # if odd length, take the middle element
        return sorted_l[n // 2]
