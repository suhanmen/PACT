def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list in ascending order
    l.sort()
    # Get the length of the list
    n = len(l)
    # Calculate the middle index
    mid = n // 2
    # Check if the length is even or odd
    if n % 2 == 0:
        # If even, return the average of the middle two elements
        return (l[mid - 1] + l[mid]) / 2
    else:
        # If odd, return the middle element
        return l[mid]
