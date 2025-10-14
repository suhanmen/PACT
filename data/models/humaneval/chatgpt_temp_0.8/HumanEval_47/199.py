def median(l: list):
    """Return median of elements in the list l."""
    sorted_l = sorted(l)
    n = len(sorted_l)
    if n % 2 == 0:
        # If the list has an even length, return the average of the middle two elements.
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the list has an odd length, return the middle element.
        return sorted_l[n // 2]
