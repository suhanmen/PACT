def median(l: list):
    """Return median of elements in the list l."""
    sorted_list = sorted(l)
    n = len(sorted_list)
    if n % 2 == 0:
        # If there are an even number of elements, return the average of the middle two
        return (sorted_list[n//2-1] + sorted_list[n//2]) / 2
    else:
        # If there are an odd number of elements, return the middle one
        return sorted_list[n//2]
