def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    # Remove duplicates
    lst = list(set(lst))
    
    if len(lst) < 2:
        return None
    
    # Sort the list and return the second element
    lst.sort()
    return lst[1]
