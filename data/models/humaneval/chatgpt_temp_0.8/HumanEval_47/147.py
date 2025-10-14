def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    s = sorted(l)
    if n % 2 == 0:
        # if the list has an even number of elements,
        # return the average of the two middle elements
        return (s[n//2-1] + s[n//2]) / 2
    else:
        # if the list has an odd number of elements,
        # return the middle element
        return s[n//2]
