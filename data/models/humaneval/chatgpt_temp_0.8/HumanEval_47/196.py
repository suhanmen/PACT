def median(l: list):
    """
    Return median of elements in the list l.
    """
    sorted_l = sorted(l)
    length = len(l)
    if length % 2 == 0:
        # if length of list is even, average the two middle elements
        mid = length // 2
        return (sorted_l[mid-1] + sorted_l[mid]) / 2
    else:
        # if length of list is odd, return the middle element
        return sorted_l[length // 2]
