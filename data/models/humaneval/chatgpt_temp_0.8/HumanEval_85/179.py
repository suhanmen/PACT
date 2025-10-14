def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices.
    
    Args:
    lst: A list of integers
    
    Returns:
    The sum of the even elements at odd indices in lst
    
    Examples:
    add([4, 2, 6, 7]) ==> 2 
    """
    
    total = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total
