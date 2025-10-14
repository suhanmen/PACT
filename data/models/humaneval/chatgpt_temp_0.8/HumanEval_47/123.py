def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list in ascending order
    l.sort()
    
    # Calculate the middle index 
    mid = len(l) // 2
    
    # If the length of the list is even, take the average of the middle two elements 
    if len(l) % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2
    # If the length of the list is odd, return the middle element 
    else:
        return l[mid]
