def median(l: list):
    """
    Return median of elements in the list l.
    """
    # First, sort the list
    sorted_list = sorted(l)
    
    # Calculate the middle index
    n = len(sorted_list)
    mid = n // 2
    
    # If the list is odd length, return the middle element
    if n % 2 == 1:
        return sorted_list[mid]
    # If the list is even length, return the average of the middle two elements
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
