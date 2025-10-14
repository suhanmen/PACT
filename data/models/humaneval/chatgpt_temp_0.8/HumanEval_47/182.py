def median(l: list):
    """
    Return median of elements in the list l.
    """
    sorted_list = sorted(l)
    length = len(sorted_list)
    midpoint = length // 2
    
    if length % 2 == 0:
        return (sorted_list[midpoint-1] + sorted_list[midpoint]) / 2
    else:
        return sorted_list[midpoint]
