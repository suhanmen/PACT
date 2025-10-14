def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    s = sorted(l)
    if n % 2 == 0:
        # If the list has an even number of elements, take the average of the middle two
        return (s[n // 2 - 1] + s[n // 2]) / 2
    else:
        # If the list has an odd number of elements, just take the middle one
        return s[n // 2]

