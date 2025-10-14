def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)  # Sort the list in ascending order
    n = len(l)
    mid = n // 2  # Find the middle index
    
    # Check if the list has an odd or even number of elements
    if n % 2 == 0:
        # If there are an even number of elements, take the average of the middle two
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2
    else:
        # If there are an odd number of elements, return the middle element
        return sorted_l[mid]
