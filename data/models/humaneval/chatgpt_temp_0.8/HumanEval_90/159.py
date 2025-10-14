def next_smallest(lst):
    
    # Remove duplicates and sort the list
    lst = sorted(set(lst))
    
    # Check if there are at least two elements in the list
    if len(lst) < 2:
        return None
    
    # Return the second smallest element
    return lst[1]
