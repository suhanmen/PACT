def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    # Find the smallest element
    smallest = min(lst)
    
    # Remove the smallest element
    lst.remove(smallest)
    
    # Find the 2nd smallest element
    second_smallest = min(lst) if len(lst) > 0 else None
    
    return second_smallest
