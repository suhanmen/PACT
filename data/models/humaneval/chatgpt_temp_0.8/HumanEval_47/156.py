def median(l: list):
    """
    Return median of elements in the list l.
    """
    l.sort() # sort the list in ascending order
    n = len(l)
    mid = n // 2 # find the middle index
    
    if n % 2 == 0:
        # if the length of the list is even, return the average of the middle two elements
        return (l[mid - 1] + l[mid]) / 2
    else:
        # if the length of the list is odd, return the middle element
        return l[mid]
        
