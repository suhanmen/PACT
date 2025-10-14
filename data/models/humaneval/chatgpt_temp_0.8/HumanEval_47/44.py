def median(l: list):
    """Return median of elements in the list l."""
    sorted_l = sorted(l)  # sort the list in ascending order
    n = len(sorted_l)
    if n % 2 == 0:
        # if the list has an even number of elements, take the mean of the two middle elements
        return (sorted_l[n//2 - 1] + sorted_l[n//2]) / 2
    else:
        # if the list has an odd number of elements, return the middle element
        return sorted_l[n//2]
