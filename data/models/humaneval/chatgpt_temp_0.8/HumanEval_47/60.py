def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Step 1: Sort the list
    l.sort()

    # Step 2: Find the middle index or indices of the list
    n = len(l)
    mid = n // 2
    
    # Step 3: Calculate median based on the length of the list
    if n % 2 == 0:
        return (l[mid-1] + l[mid]) / 2
    else:
        return l[mid]
